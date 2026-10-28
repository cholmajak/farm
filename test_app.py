"""
GreenHarvest Farm Management System (FMS) - Automated Test Suite
Tests MongoDB integration, authentication, RBAC permissions, financial calculations, and CRUD flows.
"""

import pytest
from app import create_app
from database import get_db, get_dashboard_metrics

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SECRET_KEY": "test-secret-key"
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_database_connection(app):
    """Verify PyMongo successfully connects to MongoDB and collections are populated."""
    with app.app_context():
        db = get_db()
        assert db.users.count_documents({}) >= 3
        assert db.crops.count_documents({}) >= 1
        assert db.inventory.count_documents({}) >= 1
        assert db.livestock.count_documents({}) >= 1

def test_dashboard_metrics_aggregation(app):
    """Test that MongoDB aggregation pipeline accurately computes farm KPIs."""
    with app.app_context():
        metrics = get_dashboard_metrics()
        assert metrics["total_crops"] >= 1
        assert metrics["total_livestock"] >= 1
        assert metrics["total_employees"] >= 1
        assert metrics["total_income"] >= 0
        assert metrics["total_expenses"] >= 0
        # Verify Profit or Loss calculation formula: Income - Expenses
        assert metrics["net_profit"] == metrics["total_income"] - metrics["total_expenses"]

def test_auth_login_success(client):
    """Test valid login creates session with user role."""
    response = client.post('/auth/login', data={
        "identifier": "admin",
        "password": "Admin123!"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Farm Operations Dashboard" in response.data
    assert b"Mukasa John Baptist" in response.data

def test_auth_login_invalid(client):
    """Test invalid credentials are appropriately rejected."""
    response = client.post('/auth/login', data={
        "identifier": "admin",
        "password": "WrongPassword!"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Invalid username/email or password" in response.data

def test_role_based_access_control(client):
    """Test that Farm Worker role cannot access Administrator User Management page."""
    # 1. Login as Worker
    client.post('/auth/login', data={
        "identifier": "worker",
        "password": "Worker123!"
    }, follow_redirects=True)

    # 2. Attempt to access /users (Admin only)
    response = client.get('/users', follow_redirects=True)
    assert response.status_code == 200
    assert b"Access denied: You do not have permission" in response.data

def test_inventory_negative_stock_prevention(app, client):
    """Verify that deducting more stock than available is prevented."""
    # Login as Manager
    client.post('/auth/login', data={
        "identifier": "manager",
        "password": "Manager123!"
    }, follow_redirects=True)

    with app.app_context():
        db = get_db()
        item = db.inventory.find_one({"sku": "FERT-UREA-01"})
        assert item is not None
        current_qty = item.get("quantity_on_hand", 0)

        # Attempt to deduct current_qty + 1000
        excessive_deduction = current_qty + 1000
        res = client.post(f'/inventory/adjust/{str(item["_id"])}', data={
            "adjustment_type": "DEDUCT",
            "quantity": excessive_deduction,
            "reason": "Test excessive deduction"
        }, follow_redirects=True)

        assert b"Cannot deduct" in res.data
        
        # Verify in DB that stock was NOT changed
        rechecked_item = db.inventory.find_one({"_id": item["_id"]})
        assert rechecked_item["quantity_on_hand"] == current_qty

def test_csv_report_export(client):
    """Verify that financial CSV report generates streaming downloadable response."""
    client.post('/auth/login', data={
        "identifier": "admin",
        "password": "Admin123!"
    }, follow_redirects=True)

    res = client.get('/reports/export/csv?type=financial')
    assert res.status_code == 200
    assert res.mimetype == "text/csv"
    assert b"INCOME (Sale)" in res.data or b"EXPENSE" in res.data

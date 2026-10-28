"""
GreenHarvest Farm Management System (FMS) - Database Seeder
Populates MongoDB with realistic Ugandan farm data across all collections.
"""

from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from database import get_db, init_indexes

def seed_database():
    print("Connecting to MongoDB and initializing indexes...")
    init_indexes()
    db = get_db()

    print("Cleaning existing demo collections...")
    collections = [
        'users', 'crops', 'livestock', 'employees', 'inventory', 
        'stock_movements', 'harvests', 'sales', 'expenses', 
        'tasks', 'farm_activities', 'suppliers', 'settings'
    ]
    for coll in collections:
        db[coll].delete_many({})

    # 1. Seed Users (with hashed passwords)
    print("Seeding Users with 3 Role-Based Accounts...")
    users = [
        {
            "full_name": "Mukasa John Baptist",
            "username": "admin",
            "email": "admin@greenharvest.ug",
            "phone": "+256 772 100 200",
            "role": "Administrator",
            "password_hash": generate_password_hash("Admin123!"),
            "is_active": True,
            "created_at": datetime.now(),
            "last_login": datetime.now()
        },
        {
            "full_name": "Namubiru Grace",
            "username": "manager",
            "email": "manager@greenharvest.ug",
            "phone": "+256 701 300 400",
            "role": "Farm Manager",
            "password_hash": generate_password_hash("Manager123!"),
            "is_active": True,
            "created_at": datetime.now(),
            "last_login": datetime.now()
        },
        {
            "full_name": "Okello Patrick",
            "username": "worker",
            "email": "worker@greenharvest.ug",
            "phone": "+256 782 500 600",
            "role": "Farm Worker",
            "password_hash": generate_password_hash("Worker123!"),
            "is_active": True,
            "created_at": datetime.now(),
            "last_login": datetime.now()
        }
    ]
    db.users.insert_many(users)

    # 2. Seed Employees
    print("Seeding Employees...")
    employees = [
        {
            "employee_code": "EMP-0001",
            "full_name": "Sserwadda Ronald",
            "job_title": "Senior Agronomist",
            "department": "Field & Crop Operations",
            "phone": "+256 782 111 222",
            "email": "rsserwadda@greenharvest.ug",
            "national_id": "CM88012345678A",
            "hire_date": "2024-01-15",
            "monthly_salary_ugx": 1200000,
            "status": "Active",
            "duties_assigned": "Supervises crop cycles, soil testing, and spray regimens.",
            "emergency_contact": "Wife: Sarah (+256 700 111 333)",
            "attendance": [
                {"date": "2026-10-25", "status": "Present", "notes": "On duty"},
                {"date": "2026-10-26", "status": "Present", "notes": "On duty"},
                {"date": "2026-10-27", "status": "Present", "notes": "On duty"}
            ],
            "salary_payments": [
                {"period": "September 2026", "date": "2026-09-30", "amount_ugx": 1200000, "notes": "Bank Transfer", "paid_by": "admin"}
            ],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "employee_code": "EMP-0002",
            "full_name": "Okello Patrick",
            "job_title": "Tractor & Machinery Operator",
            "department": "Equipment & Machinery",
            "phone": "+256 782 500 600",
            "email": "pokello@greenharvest.ug",
            "national_id": "CM92087654321B",
            "hire_date": "2024-06-01",
            "monthly_salary_ugx": 800000,
            "status": "Active",
            "duties_assigned": "Operates Massey Ferguson tractor, disc plowing, harrowing, and trailer hauling.",
            "emergency_contact": "Brother: Denis (+256 772 444 555)",
            "attendance": [
                {"date": "2026-10-26", "status": "Present", "notes": "Plowing block B"},
                {"date": "2026-10-27", "status": "Present", "notes": "Tractor maintenance"}
            ],
            "salary_payments": [
                {"period": "September 2026", "date": "2026-09-30", "amount_ugx": 800000, "notes": "Mobile Money", "paid_by": "admin"}
            ],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "employee_code": "EMP-0003",
            "full_name": "Atuhaire Brenda",
            "job_title": "Dairy Unit Supervisor",
            "department": "Livestock & Dairy",
            "phone": "+256 701 999 888",
            "email": "batuhaire@greenharvest.ug",
            "national_id": "CF95045612378C",
            "hire_date": "2025-02-10",
            "monthly_salary_ugx": 950000,
            "status": "Active",
            "duties_assigned": "Manages milking parlor, milk hygiene tests, herd vaccination calendar.",
            "emergency_contact": "Sister: Diana (+256 750 333 222)",
            "attendance": [
                {"date": "2026-10-27", "status": "Present", "notes": "Morning milking"}
            ],
            "salary_payments": [],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    ]
    db.employees.insert_many(employees)

    # 3. Seed Crops
    print("Seeding Ugandan Crops...")
    crops = [
        {
            "crop_id": "CRP-2026-001",
            "crop_name": "Matooke (Cooking Banana)",
            "variety": "Mpologoma",
            "field_plot": "East Plantation - Block 1",
            "planting_date": "2025-08-10",
            "expected_harvest_date": "2026-11-15",
            "actual_harvest_date": None,
            "quantity_planted": 800,
            "quantity_planted_unit": "suckers",
            "field_size": 4.5,
            "field_size_unit": "Acres",
            "fertilizer_used": "Well-cured cattle manure (8 tons) + CAN (100 kg)",
            "growth_status": "Fruiting",
            "notes": "Excellent finger development. Mulching with coffee husks completed.",
            "created_by": "manager",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "crop_id": "CRP-2026-002",
            "crop_name": "Robusta Coffee",
            "variety": "NARO Kapeke (Clonal)",
            "field_plot": "Hilltop Valley - Block 3",
            "planting_date": "2024-09-20",
            "expected_harvest_date": "2026-12-05",
            "actual_harvest_date": None,
            "quantity_planted": 1200,
            "quantity_planted_unit": "seedlings",
            "field_size": 3.0,
            "field_size_unit": "Acres",
            "fertilizer_used": "NPK 17:17:17 (150 kg)",
            "growth_status": "Maturing",
            "notes": "Main crop cherry ripening on schedule. Shade trees pruned.",
            "created_by": "manager",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "crop_id": "CRP-2026-003",
            "crop_name": "Hybrid Grain Maize",
            "variety": "Longe 10H (Drought-Tolerant)",
            "field_plot": "North Flatland - Plot 5",
            "planting_date": "2026-03-12",
            "expected_harvest_date": "2026-07-20",
            "actual_harvest_date": "2026-07-25",
            "quantity_planted": 40,
            "quantity_planted_unit": "kg",
            "field_size": 6.0,
            "field_size_unit": "Acres",
            "fertilizer_used": "DAP at planting (100 kg) + Urea top dressing (100 kg)",
            "growth_status": "Harvested",
            "notes": "High yield achieved. Harvested and dried to 13% moisture.",
            "created_by": "manager",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "crop_id": "CRP-2026-004",
            "crop_name": "Tomatoes",
            "variety": "Nuru F1 Hybrid",
            "field_plot": "Greenhouse Plot - Zone A",
            "planting_date": "2026-08-01",
            "expected_harvest_date": "2026-10-30",
            "actual_harvest_date": None,
            "quantity_planted": 3000,
            "quantity_planted_unit": "seedlings",
            "field_size": 1.0,
            "field_size_unit": "Acres",
            "fertilizer_used": "YaraMila Winner + Calcium Nitrate fertigation",
            "growth_status": "Ready for Harvest",
            "notes": "First pick scheduled for Friday. Fruit grading underway.",
            "created_by": "manager",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    ]
    crops_res = db.crops.insert_many(crops)

    # 4. Seed Farm Activities
    print("Seeding Farm Activities...")
    activities = [
        {
            "crop_id": crops_res.inserted_ids[0],
            "crop_readable_id": "CRP-2026-001",
            "crop_name": "Matooke (Cooking Banana) (Mpologoma)",
            "field_plot": "East Plantation - Block 1",
            "activity_type": "Weeding & Mulching",
            "activity_date": "2026-10-18",
            "description": "Desuckering to leave 3 stems per stool and applied coffee husk mulch.",
            "performed_by": "Sserwadda Ronald",
            "created_at": datetime.now()
        },
        {
            "crop_id": crops_res.inserted_ids[1],
            "crop_readable_id": "CRP-2026-002",
            "crop_name": "Robusta Coffee (NARO Kapeke)",
            "field_plot": "Hilltop Valley - Block 3",
            "activity_type": "Pest Control",
            "activity_date": "2026-10-22",
            "description": "Sprayed Duduthrin for coffee twig borer control.",
            "performed_by": "Sserwadda Ronald",
            "created_at": datetime.now()
        }
    ]
    db.farm_activities.insert_many(activities)

    # 5. Seed Livestock
    print("Seeding Livestock...")
    livestock = [
        {
            "tracking_type": "Individual",
            "animal_type": "Dairy Cattle",
            "breed": "Holstein Friesian Cross",
            "tag_number": "COW-0104",
            "quantity": 1,
            "gender": "Female",
            "date_of_birth": "2023-04-10",
            "pen_location": "Dairy Barn Stall 4",
            "health_status": "Healthy",
            "weight_kg": 465.0,
            "purchase_price": 2800000,
            "status": "Active",
            "treatments": [
                {
                    "treatment_type": "Vaccination",
                    "date": "2026-06-15",
                    "medication": "Foot and Mouth (FMD) Quadrivalent",
                    "dosage": "5 ml sub-Q",
                    "administered_by": "Dr. Kasozi (District Vet)",
                    "notes": "Routine biannual booster vaccination"
                },
                {
                    "treatment_type": "Deworming",
                    "date": "2026-09-10",
                    "medication": "Albendazole 10% Drench",
                    "dosage": "30 ml oral",
                    "administered_by": "Atuhaire Brenda",
                    "notes": "Quarterly deworming cycle"
                }
            ],
            "notes": "Average daily milk output: 24 liters across 2 milkings.",
            "created_by": "manager",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "tracking_type": "Individual",
            "animal_type": "Goat",
            "breed": "Boer Purebred Stud",
            "tag_number": "GT-0055",
            "quantity": 1,
            "gender": "Male",
            "date_of_birth": "2024-03-14",
            "pen_location": "Goat Shed Paddock 2",
            "health_status": "Healthy",
            "weight_kg": 68.0,
            "purchase_price": 750000,
            "status": "Active",
            "treatments": [
                {
                    "treatment_type": "Deworming",
                    "date": "2026-08-20",
                    "medication": "Ivermectin 1%",
                    "dosage": "2 ml s/c",
                    "administered_by": "Dr. Kasozi",
                    "notes": "Parasite control"
                }
            ],
            "notes": "Breeding stud buck for flock genetic improvement.",
            "created_by": "manager",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "tracking_type": "Batch",
            "animal_type": "Poultry (Broilers)",
            "breed": "Cobb 500",
            "tag_number": "PLT-BATCH-2026-04",
            "quantity": 485,
            "gender": "Mixed (Batch)",
            "date_of_birth": "2026-09-18",
            "pen_location": "Poultry House Unit 1",
            "health_status": "Healthy",
            "weight_kg": 1.9,
            "purchase_price": 1455000,
            "status": "Active",
            "treatments": [
                {
                    "treatment_type": "Vaccination",
                    "date": "2026-09-25",
                    "medication": "Gumboro (IBD) Intermediate",
                    "dosage": "Drinking water",
                    "administered_by": "Atuhaire Brenda",
                    "notes": "Day 7 booster administered smoothly"
                }
            ],
            "notes": "Week 6 broiler batch. Target weight 2.2 kg expected next week.",
            "created_by": "manager",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    ]
    db.livestock.insert_many(livestock)

    # 6. Seed Inventory Items (including one low-stock item)
    print("Seeding Inventory SKUs & Supplies...")
    inventory_items = [
        {
            "sku": "FERT-UREA-01",
            "name": "Urea Fertilizer (46% Nitrogen)",
            "category": "Fertilizers",
            "unit": "bags (50kg)",
            "quantity_on_hand": 18.0,
            "min_stock_level": 10.0,
            "unit_cost_ugx": 160000,
            "storage_location": "Central Fertilizer Store",
            "supplier": "Grainpulse Uganda Ltd",
            "notes": "High nitrogen granules. Protect from humidity.",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "sku": "FERT-NPK-02",
            "name": "NPK 17:17:17 Basal Fertilizer",
            "category": "Fertilizers",
            "unit": "bags (50kg)",
            "quantity_on_hand": 4.0,  # LOW STOCK (<= 10)
            "min_stock_level": 10.0,
            "unit_cost_ugx": 185000,
            "storage_location": "Central Fertilizer Store",
            "supplier": "Bukoola Chemical Industries",
            "notes": "Restock urgently needed before second planting season.",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "sku": "FEED-DAIRY-01",
            "name": "High Yield Dairy Meal (16% CP)",
            "category": "Animal Feeds",
            "unit": "bags (50kg)",
            "quantity_on_hand": 28.0,
            "min_stock_level": 15.0,
            "unit_cost_ugx": 78000,
            "storage_location": "Feed Silo Bay 1",
            "supplier": "Unga Millers Uganda",
            "notes": "Compounded concentrates for milking dairy herd.",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "sku": "CHEM-PEST-01",
            "name": "Duduthrin 5EC Insecticide",
            "category": "Pesticides",
            "unit": "liters",
            "quantity_on_hand": 2.0,  # LOW STOCK (<= 5)
            "min_stock_level": 5.0,
            "unit_cost_ugx": 48000,
            "storage_location": "Secured Chemical Shed",
            "supplier": "Bukoola Chemical Industries",
            "notes": "Broad-spectrum contact insecticide (Lambda-cyhalothrin).",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "sku": "FUEL-DSL-01",
            "name": "Automotive Diesel Fuel",
            "category": "Fuel and Other Supplies",
            "unit": "liters",
            "quantity_on_hand": 450.0,
            "min_stock_level": 100.0,
            "unit_cost_ugx": 5200,
            "storage_location": "Underground Diesel Tank",
            "supplier": "TotalEnergies Mukono",
            "notes": "For farm tractors, water pump generator, and transport truck.",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    ]
    inv_res = db.inventory.insert_many(inventory_items)

    # 7. Seed Stock Movements
    print("Seeding Stock Movements Audit Trail...")
    movements = [
        {
            "item_id": inv_res.inserted_ids[0],
            "sku": "FERT-UREA-01",
            "item_name": "Urea Fertilizer (46% Nitrogen)",
            "movement_type": "INITIAL_STOCK",
            "quantity": 25.0,
            "previous_stock": 0,
            "new_stock": 25.0,
            "reason": "Initial season procurement",
            "reference": "PO-2026-088",
            "performed_by": "manager",
            "timestamp": datetime.now() - timedelta(days=20)
        },
        {
            "item_id": inv_res.inserted_ids[0],
            "sku": "FERT-UREA-01",
            "item_name": "Urea Fertilizer (46% Nitrogen)",
            "movement_type": "USAGE_OUT",
            "quantity": 7.0,
            "previous_stock": 25.0,
            "new_stock": 18.0,
            "reason": "Applied on Plot 5 Maize and Plantation 1",
            "reference": "Task-102",
            "performed_by": "worker",
            "timestamp": datetime.now() - timedelta(days=5)
        }
    ]
    db.stock_movements.insert_many(movements)

    # 8. Seed Harvests
    print("Seeding Harvest Batches...")
    harvests = [
        {
            "batch_number": "HRV-2026-0001",
            "crop_id": crops_res.inserted_ids[2], # Maize
            "crop_code": "CRP-2026-003",
            "crop_name": "Hybrid Grain Maize (Longe 10H)",
            "field_plot": "North Flatland - Plot 5",
            "harvest_date": "2026-07-25",
            "harvested_quantity": 4500.0,
            "unit": "kg",
            "sold_quantity": 3000.0,
            "available_for_sale": 1500.0,
            "quality_grade": "Grade A (Export / Premium)",
            "storage_location": "Produce Store Silo 2",
            "notes": "Moisture content dried to 12.8%. Well-aerated.",
            "recorded_by": "manager",
            "created_at": datetime.now() - timedelta(days=90)
        },
        {
            "batch_number": "HRV-2026-0002",
            "crop_id": crops_res.inserted_ids[0], # Matooke
            "crop_code": "CRP-2026-001",
            "crop_name": "Matooke (Cooking Banana) (Mpologoma)",
            "field_plot": "East Plantation - Block 1",
            "harvest_date": "2026-10-20",
            "harvested_quantity": 120.0,
            "unit": "bunches",
            "sold_quantity": 80.0,
            "available_for_sale": 40.0,
            "quality_grade": "Grade A (Export / Premium)",
            "storage_location": "Shaded Produce Shed",
            "notes": "Large heavy bunches (30kg+ average).",
            "recorded_by": "manager",
            "created_at": datetime.now() - timedelta(days=7)
        }
    ]
    db.harvests.insert_many(harvests)

    # 9. Seed Sales
    print("Seeding Sales Transactions (in UGX)...")
    sales = [
        {
            "invoice_number": "INV-2026-0001",
            "sale_date": "2026-08-05",
            "customer_name": "Kampala Grain Millers Co.",
            "customer_phone": "+256 772 900 800",
            "product_name": "Hybrid Grain Maize (Longe 10H)",
            "item_source": "harvest",
            "harvest_id": None,
            "quantity": 3000.0,
            "unit": "kg",
            "unit_price": 1400.0,
            "total_amount": 4200000.0, # UGX 4,200,000
            "payment_status": "Paid",
            "payment_method": "Bank Wire / EFT",
            "notes": "Bulk supply delivered by farm truck.",
            "recorded_by": "manager",
            "created_at": datetime.now() - timedelta(days=80)
        },
        {
            "invoice_number": "INV-2026-0002",
            "sale_date": "2026-10-21",
            "customer_name": "Nakasero Fresh Market Traders",
            "customer_phone": "+256 701 445 566",
            "product_name": "Matooke (Cooking Banana)",
            "item_source": "harvest",
            "harvest_id": None,
            "quantity": 80.0,
            "unit": "bunches",
            "unit_price": 32000.0,
            "total_amount": 2560000.0, # UGX 2,560,000
            "payment_status": "Paid",
            "payment_method": "MTN Mobile Money",
            "notes": "80 bunches dispatched early morning.",
            "recorded_by": "manager",
            "created_at": datetime.now() - timedelta(days=6)
        },
        {
            "invoice_number": "INV-2026-0003",
            "sale_date": "2026-10-26",
            "customer_name": "Brookside Dairy Collection Center",
            "customer_phone": "+256 782 333 111",
            "product_name": "Fresh Farm Milk",
            "item_source": "other",
            "harvest_id": None,
            "quantity": 680.0,
            "unit": "liters",
            "unit_price": 1600.0,
            "total_amount": 1088000.0, # UGX 1,088,000
            "payment_status": "Pending",
            "payment_method": "Credit / Invoice",
            "notes": "Weekly milk deliveries. Bi-monthly reconciliation.",
            "recorded_by": "manager",
            "created_at": datetime.now() - timedelta(days=1)
        }
    ]
    db.sales.insert_many(sales)

    # 10. Seed Expenses
    print("Seeding Farm Operating Expenses (in UGX)...")
    expenses = [
        {
            "date": "2026-08-01",
            "category": "Seeds & Planting Materials",
            "amount": 420000.0,
            "description": "Purchased 3,000 Tomato Nuru F1 seedlings from Victoria Seeds",
            "vendor_supplier": "Victoria Seeds Ltd",
            "payment_method": "Cash",
            "receipt_ref": "REC-7712",
            "recorded_by": "manager",
            "created_at": datetime.now() - timedelta(days=85)
        },
        {
            "date": "2026-09-15",
            "category": "Fuel, Oil & Lubricants",
            "amount": 780000.0,
            "description": "150 liters diesel for tractor field tillage & water generator",
            "vendor_supplier": "TotalEnergies Mukono",
            "payment_method": "MTN Mobile Money",
            "receipt_ref": "TOT-8890",
            "recorded_by": "manager",
            "created_at": datetime.now() - timedelta(days=40)
        },
        {
            "date": "2026-09-30",
            "category": "Employee Wages & Salaries",
            "amount": 2000000.0,
            "description": "Staff monthly salaries disbursement for September 2026",
            "vendor_supplier": "Farm Staff Payroll",
            "payment_method": "Bank Transfer / Cheque",
            "receipt_ref": "PAY-2026-09",
            "recorded_by": "admin",
            "created_at": datetime.now() - timedelta(days=27)
        },
        {
            "date": "2026-10-10",
            "category": "Veterinary Services & Medicine",
            "amount": 250000.0,
            "description": "Quarterly herd vaccination and vitamin injections by District Vet",
            "vendor_supplier": "Dr. Kasozi Vet Clinic",
            "payment_method": "Airtel Money",
            "receipt_ref": "VET-102",
            "recorded_by": "manager",
            "created_at": datetime.now() - timedelta(days=17)
        }
    ]
    db.expenses.insert_many(expenses)

    # 11. Seed Tasks
    print("Seeding Farm Tasks...")
    tasks = [
        {
            "title": "Irrigate Greenhouse Tomatoes Zone A",
            "category": "Irrigation & Watering",
            "priority": "High",
            "status": "Pending",
            "due_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "assigned_to": "Okello Patrick",
            "location_field": "Greenhouse Plot - Zone A",
            "description": "Turn on drip manifold for 45 minutes; mix in calcium nitrate booster.",
            "notes": "",
            "created_by": "manager",
            "created_at": datetime.now(),
            "completed_at": None
        },
        {
            "title": "Harvest Ripe Mpologoma Matooke Bunches",
            "category": "Harvesting & Grading",
            "priority": "Urgent",
            "status": "In Progress",
            "due_date": datetime.now().strftime("%Y-%m-%d"),
            "assigned_to": "Sserwadda Ronald",
            "location_field": "East Plantation - Block 1",
            "description": "Select ready bunches marked with yellow ribbons for Nakasero buyer.",
            "notes": "Trailer is pre-positioned at field gate.",
            "created_by": "manager",
            "created_at": datetime.now(),
            "completed_at": None
        },
        {
            "title": "Clean & Disinfect Milking Equipment",
            "category": "General Farm Maintenance",
            "priority": "Medium",
            "status": "Completed",
            "due_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
            "assigned_to": "Atuhaire Brenda",
            "location_field": "Dairy Parlor",
            "description": "Circulate warm caustic soda wash followed by sanitizing rinse.",
            "notes": "Done per hygiene guidelines.",
            "created_by": "manager",
            "created_at": datetime.now() - timedelta(days=2),
            "completed_at": datetime.now() - timedelta(days=1)
        }
    ]
    db.tasks.insert_many(tasks)

    # 12. Seed Farm Settings
    print("Seeding Farm Settings...")
    farm_settings = {
        "type": "farm_profile",
        "farm_name": "GreenHarvest Farm Management System",
        "owner_name": "Mukasa John Baptist",
        "location": "Mukono District, Central Uganda",
        "primary_phone": "+256 772 100 200",
        "email": "contact@greenharvest.ug",
        "currency_code": "UGX",
        "currency_symbol": "USh",
        "timezone": "Africa/Kampala (EAT)",
        "total_land_acres": 150.0,
        "updated_at": datetime.now()
    }
    db.settings.update_one({"type": "farm_profile"}, {"$set": farm_settings}, upsert=True)

    print("=================================================================")
    print("  SEEDING COMPLETE! Database 'farm_management_db' is now populated.")
    print("  Ready for testing:")
    print("  - Admin:   username: admin    password: Admin123!")
    print("  - Manager: username: manager  password: Manager123!")
    print("  - Worker:  username: worker   password: Worker123!")
    print("=================================================================")

if __name__ == '__main__':
    seed_database()

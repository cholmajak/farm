import os
from flask import Flask, render_template, session
from config import Config
from database import init_indexes, close_db

# Import Module Blueprints
from modules.auth import auth_bp
from modules.dashboard import dashboard_bp
from modules.crops import crops_bp
from modules.livestock import livestock_bp
from modules.employees import employees_bp
from modules.inventory import inventory_bp
from modules.harvests import harvests_bp
from modules.sales import sales_bp
from modules.expenses import expenses_bp
from modules.tasks import tasks_bp
from modules.reports import reports_bp
from modules.users import users_bp
from modules.settings import settings_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize MongoDB Indexes
    with app.app_context():
        init_indexes()

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(crops_bp)
    app.register_blueprint(livestock_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(harvests_bp)
    app.register_blueprint(sales_bp)
    app.register_blueprint(expenses_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(settings_bp)

    # Global Template Filters and Context
    @app.template_filter('ugx')
    def ugx_format(value):
        try:
            val = float(value or 0)
            return f"UGX {val:,.0f}"
        except (ValueError, TypeError):
            return f"UGX 0"

    @app.template_filter('number')
    def number_format(value):
        try:
            val = float(value or 0)
            if val.is_integer():
                return f"{int(val):,}"
            return f"{val:,.2f}"
        except (ValueError, TypeError):
            return "0"

    @app.context_processor
    def inject_global_template_vars():
        return {
            "farm_name": Config.FARM_NAME,
            "currency_code": Config.CURRENCY_CODE,
            "currency_symbol": Config.CURRENCY_SYMBOL,
            "current_role": session.get('role', 'Guest'),
            "current_user_name": session.get('full_name', session.get('username', 'Guest')),
            "is_logged_in": 'user_id' in session,
            "str": str
        }


    # Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(403)
    def access_forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    print(f"================================================================")
    print(f"  GreenHarvest Farm Management System (FMS)")
    print(f"  Connected to MongoDB: {Config.MONGO_URI}")
    print(f"  Server starting on: http://127.0.0.1:{port}")
    print(f"================================================================")
    app.run(host='0.0.0.0', port=port, debug=True)

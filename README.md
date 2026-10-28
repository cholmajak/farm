# GreenHarvest Farm Management System (FMS)

A modern, responsive, and secure full-stack **Farm Management System (FMS)** built with **Python (Flask)**, **MongoDB (PyMongo)**, and **Chart.js**, designed to manage crops, livestock, farm personnel, inventory supplies, harvest yields, sales billing, operational expenses, and analytical reports in one centralized application.

---

## 1. System Architecture & Key Highlights

- **Backend:** Python 3.10+ / Flask application structured with modular Blueprints.
- **Database:** MongoDB NoSQL database utilizing PyMongo for schema validation, indexing, and aggregation pipelines.
- **Frontend:** Vanilla HTML5, modern CSS3 responsive design system (Green/White/Gray palette with dark-green sidebar), and JavaScript.
- **Analytics & Visualizations:** Chart.js 4.x for real-time cash flow and harvest yield charts.
- **Localization:** Default currency in **Uganda Shillings (UGX)** with thousands separators and formatted currency cards.
- **Security:** Secure password hashing with Werkzeug (`scrypt`/`pbkdf2`), role-based access control (RBAC), and session protection.

---

## 2. Role-Based Access Control (RBAC)

The system enforces three distinct permission tiers:

| Role | Permitted Access |
| :--- | :--- |
| **Administrator** | Full access to all modules, User Management (create staff accounts, modify roles, reset passwords), and Farm System Profile settings. |
| **Farm Manager** | Manages daily farm operations: Crops, Livestock, Employees, Inventory, Harvests, Sales, Expenses, Tasks, and Reports. |
| **Farm Worker** | Views assigned daily tasks, logs task progress/completion, inspects field activities, and records item usage. |

---

## 3. Project Directory Structure

```text
farm/
│
├── app.py                     # Main Flask application entrypoint & factory
├── config.py                  # Application configuration & environment settings
├── requirements.txt           # Python dependencies
├── .env.example               # Example environment variables
├── .env                       # Active environment configuration
├── seed_data.py               # Comprehensive database seeder with realistic Ugandan data
├── test_app.py                # Automated pytest test suite (7 unit & integration tests)
│
├── database/
│   ├── __init__.py            # Database exports
│   ├── mongo.py               # PyMongo connection pooling & collection indexes
│   └── aggregations.py        # MongoDB aggregation pipelines for dashboard & reports
│
├── modules/
│   ├── auth/                  # Authentication, login, register, session decorators
│   ├── dashboard/             # Dashboard metrics, Chart.js API endpoints
│   ├── crops/                 # Crop cycles, growth stages, agronomic activities
│   ├── livestock/             # Cattle, goats, poultry flocks, medical treatments
│   ├── employees/             # Staff directory, attendance tracking, salary disbursement
│   ├── inventory/             # Stock items, reorder alerts, movement audit logs
│   ├── harvests/              # Harvested yields, quality grading, available produce
│   ├── sales/                 # Billing invoices, customer records, stock depletion
│   ├── expenses/              # Operating expenditures, categories, suppliers
│   ├── tasks/                 # Task assignments, priority flags, due dates
│   ├── reports/               # Analytical summaries, CSV export engine, printable views
│   ├── users/                 # Admin user administration & password resets
│   └── settings/              # Farm enterprise profile & MongoDB diagnostics
│
├── static/
│   ├── css/
│   │   └── main.css           # Modern CSS styling (green theme, responsive tables, cards)
│   ├── js/
│   │   └── main.js            # Sidebar drawer, modals, Chart.js initialization, live search
│   └── images/
│       └── logo.svg           # GreenHarvest brand vector SVG logo
│
└── templates/
    ├── base.html              # Master layout with responsive 13-item sidebar
    ├── auth/                  # login.html, register.html
    ├── dashboard/             # index.html (7 KPI cards, 2 Chart.js graphs, tasks feed)
    ├── crops/                 # index.html, add.html, edit.html, view.html
    ├── livestock/             # index.html, add.html, edit.html, view.html
    ├── employees/             # index.html, add.html, edit.html, view.html
    ├── inventory/             # index.html, add.html, edit.html, movements.html
    ├── harvests/              # index.html, add.html
    ├── sales/                 # index.html, add.html, view.html
    ├── expenses/              # index.html, add.html
    ├── tasks/                 # index.html, add.html
    ├── reports/               # index.html
    ├── users/                 # index.html
    ├── settings/              # index.html
    └── errors/                # 404.html, 403.html, 500.html
```

---

## 4. MongoDB Database Design & Collections

All farm data is stored in MongoDB collections rather than relational tables:

1. **`users`**: User credentials (`password_hash`), RBAC roles (`Administrator`, `Farm Manager`, `Farm Worker`), phone, status.
2. **`crops`**: Crop cycles (`crop_id`, `crop_name`, `variety`, `field_plot`, `field_size`, `planting_date`, `expected_harvest_date`, `growth_status`, `fertilizer_used`).
3. **`livestock`**: Animal records (`tag_number`, `animal_type`, `breed`, `quantity`, `pen_location`, `health_status`, `weight_kg`, `purchase_price`, embedded `treatments`).
4. **`employees`**: Farm staff (`employee_code`, `full_name`, `job_title`, `department`, `phone`, `monthly_salary_ugx`, embedded `attendance` & `salary_payments`).
5. **`inventory`**: Supplies (`sku`, `name`, `category`, `unit`, `quantity_on_hand`, `min_stock_level`, `unit_cost_ugx`, `supplier`).
6. **`stock_movements`**: Immutable audit logs of all additions and usage deductions (`movement_type`, `quantity`, `previous_stock`, `new_stock`, `timestamp`, `performed_by`).
7. **`harvests`**: Produce lots (`batch_number`, `crop_id`, `harvested_quantity`, `sold_quantity`, `available_for_sale`, `quality_grade`).
8. **`sales`**: Invoices in UGX (`invoice_number`, `customer_name`, `product_name`, `quantity`, `unit_price`, `total_amount`, `payment_status`).
9. **`expenses`**: Operating costs (`date`, `category`, `amount`, `description`, `vendor_supplier`, `receipt_ref`).
10. **`tasks`**: Daily assignments (`title`, `category`, `priority`, `status`, `due_date`, `assigned_to`, `location_field`).
11. **`farm_activities`**: Field activity timeline (`crop_id`, `activity_type`, `activity_date`, `description`, `performed_by`).
12. **`settings`**: Farm enterprise metadata (`farm_name`, `location`, `primary_phone`, `currency_code`, `total_land_acres`).

---

## 5. Getting Started & Installation

### Prerequisites
- Python 3.10+ (or Python 3.14)
- MongoDB Community Server or MongoDB Atlas cluster (running on `mongodb://localhost:27017/`)

### Setup Instructions

1. **Clone or Navigate to the Project Directory**:
   ```bash
   cd c:\Users\user\Desktop\farm
   ```

2. **Create and Activate a Virtual Environment**:
   ```powershell
   # Using Python venv
   python -m venv .venv
   .\.venv\Scripts\activate

   # Or using uv (recommended for ultra-fast setup)
   uv venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   # Or with uv:
   uv pip install -r requirements.txt --python .venv\Scripts\python.exe
   ```

4. **Configure Environment Variables**:
   Copy `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
   *Edit `.env` if connecting to MongoDB Atlas (`mongodb+srv://...`).*

5. **Seed the Database with Sample Farm Data**:
   ```powershell
   python seed_data.py
   # Or:
   .\.venv\Scripts\python.exe seed_data.py
   ```

6. **Run the Automated Tests**:
   ```powershell
   pytest -v
   # Or:
   .\.venv\Scripts\python.exe -m pytest test_app.py -v
   ```

7. **Start the Web Application**:
   ```powershell
   python app.py
   # Or:
   .\.venv\Scripts\python.exe app.py
   ```
   Open your browser at: **`http://127.0.0.1:5000`**

---

## 6. Default Demo Credentials

After running `seed_data.py`, use the following accounts to test different roles:

| Role | Username | Password | Notes |
| :--- | :--- | :--- | :--- |
| **Administrator** | `admin` | `Admin123!` | Full control, User Management, System Settings |
| **Farm Manager** | `manager` | `Manager123!` | Operations, Crops, Livestock, Inventory, Sales, Expenses |
| **Farm Worker** | `worker` | `Worker123!` | Assigned tasks, field activities, status toggles |

---

## 7. Key Features Demonstrated

- **Real-Time Financial Formulas**: Profit / Loss = Total Sales (UGX) − Total Expenses (UGX).
- **Negative Stock Protection**: Built-in guard preventing deduction of inventory beyond available stock.
- **Stock Movements Audit Trail**: Every addition or deduction generates an immutable audit record in MongoDB.
- **Automatic Produce Depletion**: When a sale is recorded from a harvest lot, `available_for_sale` is atomically decremented.
- **Interactive Visualizations**: Real-time Chart.js charts connected to live MongoDB aggregation endpoints (`/api/charts/*`).
- **Reports Export Engine**: Dynamic CSV download generation and printable invoice receipts.

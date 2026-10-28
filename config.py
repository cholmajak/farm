import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'agripulse-dev-secret-key-uganda-2026')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/farm_management_db')
    DB_NAME = os.getenv('DB_NAME', 'farm_management_db')
    FARM_NAME = os.getenv('FARM_NAME', 'AgriPulse Smart Farm')
    CURRENCY_CODE = os.getenv('CURRENCY_CODE', 'UGX')
    CURRENCY_SYMBOL = os.getenv('CURRENCY_SYMBOL', 'USh')
    ITEMS_PER_PAGE = int(os.getenv('ITEMS_PER_PAGE', 20))

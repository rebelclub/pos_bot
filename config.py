import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot
BOT_TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID', 0))

# Firebird Database
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3050)),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER', 'SYSDBA'),
    'password': os.getenv('DB_PASSWORD', 'masterkey'),
    'charset': os.getenv('DB_CHARSET', 'UTF8')
}
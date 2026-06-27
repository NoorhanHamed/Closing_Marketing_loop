"""
Project configuration.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

CUSTOMERS_FILE = DATA_DIR / "customers.json"
CONVERSATIONS_FILE = DATA_DIR / "conversations.json"
ORDERS_FILE = DATA_DIR / "orders.json"
MESSAGES_FILE = DATA_DIR / "messages.json"

ATTRIBUTION_CSV = OUTPUT_DIR / "attribution.csv"
ATTRIBUTION_PARQUET = OUTPUT_DIR / "attribution.parquet"
PURCHASE_EVENTS_JSON = OUTPUT_DIR / "purchase_events.json"

# ------------------------------------------------------------------
# Event Settings
# ------------------------------------------------------------------

PURCHASE_STATUS = "delivered"

ACTION_SOURCE = "business_messaging"

MESSAGING_CHANNEL = "whatsapp"



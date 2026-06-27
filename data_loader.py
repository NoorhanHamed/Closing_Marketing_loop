"""
Load raw JSON data.
"""

from config import (
    CUSTOMERS_FILE,
    CONVERSATIONS_FILE,
    ORDERS_FILE,
    MESSAGES_FILE
)

from utils import load_json


def load_data():

    customers = load_json(CUSTOMERS_FILE)

    conversations = load_json(CONVERSATIONS_FILE)

    orders = load_json(ORDERS_FILE)

    messages = load_json(MESSAGES_FILE)

    return (
        customers,
        conversations,
        orders,
        messages
    )
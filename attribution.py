"""
Build the Attribution DataFrame.

This dataframe is the source of truth
for analytics and Meta payload generation.
"""

from datetime import datetime

import pandas as pd


def get_delivered_timestamp(order):

    for item in order["status_history"]:

        if item["to"] == "delivered":

            return datetime.fromisoformat(
                item["at"].replace("Z", "+00:00")
            )

    return None


def build_attribution_dataframe(
    customers,
    conversations,
    orders
):

    customer_lookup = {

        c["id"]: c

        for c in customers
    }

    conversation_lookup = {

        c["id"]: c

        for c in conversations
    }

    rows = []

    for order in orders:

        conversation = conversation_lookup.get(
            order.get("conversation_id")
        )

        if conversation is None:
            continue

        customer = customer_lookup.get(
            order["customer_id"]
        )

        if customer is None:
            continue

        source = conversation.get(
            "source",
            {}
        )

        row = {

            "account_id":
                order["account_id"],

            "customer_id":
                customer["id"],

            "conversation_id":
                conversation["id"],

            "order_id":
                order["id"],

            "order_status":
                order["status"],

            "delivered_at":
                get_delivered_timestamp(order),

            "revenue":
                order["total"],

            "currency":
                order["currency"],

            "payment_method":
                order.get("payment_method"),

            "phone":
                customer.get("phone"),

            "email":
                customer.get("email"),

            "first_name":
                customer.get("first_name"),

            "last_name":
                customer.get("last_name"),

            "city":
                customer.get("city"),

            "country":
                customer.get("country"),

            "ctwa_clid":
                source.get("ctwa_clid"),

            "campaign_id":
                source.get("campaign_id"),

            "ad_id":
                source.get("ad_id"),

            "creative_id":
                source.get("creative_id"),

            "platform":
                source.get("platform")
        }

        rows.append(row)

    return pd.DataFrame(rows)
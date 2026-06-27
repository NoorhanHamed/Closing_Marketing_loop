"""
Convert Attribution DataFrame
into Meta CAPI Purchase payloads.
"""

from config import (
    PURCHASE_STATUS,
    ACTION_SOURCE,
    MESSAGING_CHANNEL,
    WHATSAPP_BUSINESS_ACCOUNT_ID
)

from utils import sha256_hash


def build_purchase_payloads(df):

    payloads = []

    purchases = df[
        df["order_status"] == PURCHASE_STATUS
    ]

    for _, row in purchases.iterrows():

        user_data = {

            "ctwa_clid":
                row["ctwa_clid"],

            "whatsapp_business_account_id":
                WHATSAPP_BUSINESS_ACCOUNT_ID,

            "external_id": [
                sha256_hash(row["customer_id"])
            ]
        }

        if row["phone"]:

            user_data["ph"] = [
                sha256_hash(row["phone"])
            ]

        if row["email"]:

            user_data["em"] = [
                sha256_hash(row["email"])
            ]

        if row["first_name"]:

            user_data["fn"] = [
                sha256_hash(row["first_name"])
            ]

        if row["last_name"]:

            user_data["ln"] = [
                sha256_hash(row["last_name"])
            ]

        if row["city"]:

            user_data["ct"] = [
                sha256_hash(row["city"])
            ]

        if row["country"]:

            user_data["country"] = [
                sha256_hash(row["country"])
            ]

        payload = {

            "event_name":
                "Purchase",

            "event_time":
                int(row["delivered_at"].timestamp()),

            "event_id":
                f"purchase_{row['order_id']}",

            "action_source":
                ACTION_SOURCE,

            "messaging_channel":
                MESSAGING_CHANNEL,

            "user_data":
                user_data,

            "custom_data": {

                "value":
                    float(row["revenue"]),

                "currency":
                    row["currency"],

                "order_id":
                    row["order_id"]
            }
        }

        payloads.append(payload)

    return payloads
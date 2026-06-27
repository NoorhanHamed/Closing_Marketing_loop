"""
Run the complete attribution pipeline.
"""

from attribution import build_attribution_dataframe
from capi_payload import build_purchase_payloads
from config import (
    ATTRIBUTION_CSV,
    ATTRIBUTION_PARQUET,
    PURCHASE_EVENTS_JSON
)
from data_loader import load_data
from utils import (
    save_dataframe,
    save_json,
)


def main():

    (
        customers,
        conversations,
        orders,
        messages
    ) = load_data()

    attribution_df = build_attribution_dataframe(

        customers,

        conversations,

        orders
    )

    save_dataframe(

        attribution_df,

        ATTRIBUTION_CSV,

        ATTRIBUTION_PARQUET
    )

    purchase_payloads = build_purchase_payloads(
        attribution_df
    )

    save_json(

        purchase_payloads,

        PURCHASE_EVENTS_JSON
    )

    print("=" * 60)
    print("Attribution Records :", len(attribution_df))
    print("Purchase Events     :", len(purchase_payloads))
    print("=" * 60)


if __name__ == "__main__":

    main()
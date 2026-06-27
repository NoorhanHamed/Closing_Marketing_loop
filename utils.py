"""
Shared helper functions.
"""

import hashlib
import json
from pathlib import Path
from typing import Any

import pandas as pd


def sha256_hash(value: Any) -> str | None:
    """
    SHA256 hash following Meta normalization.
    """

    if value is None:
        return None

    value = str(value).strip().lower()

    if value == "":
        return None

    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()


def load_json(path: Path):

    with open(path, "r", encoding="utf-8") as f:

        return json.load(f)


def save_json(data, path: Path):

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def save_dataframe(
    df: pd.DataFrame,
    csv_path: Path,
    parquet_path: Path
):

    csv_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        csv_path,
        index=False
    )

    df.to_parquet(
        parquet_path,
        index=False
    )
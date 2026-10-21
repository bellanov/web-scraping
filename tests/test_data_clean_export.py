"""Unit tests for data cleaning and export helpers."""

import pandas as pd

from samples.data_clean_export import export_to_csv


def test_export_to_csv_writes_json_records_as_rows(tmp_path):
    data = {
        "First product": {"price": "$10"},
        "Second product": {"price": "$20"},
    }
    filename = tmp_path / "products.csv"

    export_to_csv(data, filename)

    result = pd.read_csv(filename)
    assert result.to_dict(orient="records") == [
        {"name": "First product", "price": "$10"},
        {"name": "Second product", "price": "$20"},
    ]

import polars as pl
from unittest.mock import patch
from usecase.precess_data import process


@patch("usecase.precess_data.clean_dataframe")
@patch("usecase.precess_data.read_csv")
def test_読み込んだデータのクリーンアップと集計(mock_read_csv, mock_clean_dataframe):
    mock_read_csv.return_value = pl.DataFrame(
        {
            "name": [" Alice", " boB  "],
        }
    )

    mock_clean_dataframe.return_value = pl.DataFrame(
        {
            "name": ["ALICE", "BOB"],
        }
    )

    actual = process("test.csv")

    expected = pl.DataFrame(
        {
            "name": ["ALICE", "BOB"],
        }
    )

    assert actual.equals(expected)

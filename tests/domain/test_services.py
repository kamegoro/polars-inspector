import polars as pl
from domain.models import Dataframe
from domain.services import CleanDataframe
from infrastructure.csv import Csv
from unittest.mock import patch


@patch.object(Csv, "read_csv")
def test_小文字の名前を大文字にする(mock_read_csv):
    mock_read_csv.return_value = pl.DataFrame({"name": ["alice", "bob"]})

    clean_dataframe = CleanDataframe(Csv("test.csv"))
    actual = clean_dataframe.exec()

    expected = Dataframe({"name": ["ALICE", "BOB"]})  # 手動入力の期待値

    assert actual.equals(expected)


@patch.object(Csv, "read_csv")
def test_空白を削除する(mock_read_csv):
    mock_read_csv.return_value = pl.DataFrame({"name": [" ALICE", "BOB "]})

    clean_dataframe = CleanDataframe(Csv("test.csv"))
    actual = clean_dataframe.exec()

    expected = pl.DataFrame({"name": ["ALICE", "BOB"]})

    assert actual.equals(expected)


@patch.object(Csv, "read_csv")
def test_nullをUnknownに変換する(mock_read_csv):
    mock_read_csv.return_value = pl.DataFrame({"name": [None, "BOB"]})

    clean_dataframe = CleanDataframe(Csv("test.csv"))
    actual = clean_dataframe.exec()

    expected = pl.DataFrame({"name": ["Unknown", "BOB"]})

    assert actual.equals(expected)

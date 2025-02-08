import polars as pl
from domain.services import clean_dataframe


def test_小文字の名前を大文字にする():
    df = pl.DataFrame({"name": ["alice", "bob"]})

    actual = clean_dataframe(df)

    expected = pl.DataFrame({"name": ["ALICE", "BOB"]})

    assert actual.equals(expected)


def test_空白を削除する():
    df = pl.DataFrame({"name": [" ALICE", "BOB "]})

    actual = clean_dataframe(df)

    expected = pl.DataFrame({"name": ["ALICE", "BOB"]})

    assert actual.equals(expected)

def test_nullをUnknownに変換する():
    df = pl.DataFrame({"name": [None, "BOB"]})

    actual = clean_dataframe(df)

    expected = pl.DataFrame({"name": ["Unknown", "BOB"]})

    assert actual.equals(expected)
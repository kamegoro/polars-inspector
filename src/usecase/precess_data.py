from infrastructure.file_reader import read_csv
from domain.services import clean_dataframe
from domain.aggregations import group_and_sum
import polars as pl


def process(file_path: str) -> pl.DataFrame:
    df = read_csv(file_path)
    df = clean_dataframe(df)

    return df

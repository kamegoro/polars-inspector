import polars as pl
from port.csv import CsvPort


class Csv(CsvPort):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_csv(self) -> pl.DataFrame:
        return pl.read_csv(self.file_path)

    def write_csv(self, df: pl.DataFrame, file_path: str) -> None:
        return df.write_csv(file_path)

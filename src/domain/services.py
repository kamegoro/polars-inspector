import polars as pl
from port.csv import CsvPort
from domain.dataframe import Dataframe


class CleanDataframe:
    def __init__(self, csv_port: CsvPort):
        self.csv_port = csv_port

    def exec(self) -> Dataframe:
        dataframe = Dataframe(self.csv_port.read_csv())

        return dataframe.with_columns(
            [
                pl.col(col).str.strip_chars().str.to_uppercase().fill_null("Unknown")
                for col in dataframe.columns
                if dataframe[col].dtype == pl.Utf8
            ]
        )

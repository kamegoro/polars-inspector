from abc import ABC, abstractmethod
import polars as pl


class CsvPort(ABC):
    @abstractmethod
    def read_csv(self) -> pl.DataFrame:
        pass

    @abstractmethod
    def write_csv(self, df: pl.DataFrame, file_path: str) -> None:
        pass
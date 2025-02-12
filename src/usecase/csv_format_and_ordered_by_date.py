from port.csv import CsvPort
from domain.models import Dataframe
from domain.services import CleanDataframe
import polars as pl


def csvFormatAndOrderedByDate(csvPort: CsvPort):
    cleanDataframeDomain = CleanDataframe(csvPort)

    result = Dataframe(pl.read_csv("target.csv"))
    cleanDataframeDomain.exec(result)

    None

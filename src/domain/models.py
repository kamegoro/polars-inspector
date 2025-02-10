import polars as pl

class Dataframe(pl.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
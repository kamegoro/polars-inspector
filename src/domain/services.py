import polars as pl


def clean_dataframe(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(pl.col())

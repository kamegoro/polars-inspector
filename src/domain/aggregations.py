import polars as pl


def group_and_sum(df: pl.DataFrame, group_col: str, sum_col: str) -> pl.DataFrame:
    return df.group_by(group_col).agg(pl.col(sum_col).sum())

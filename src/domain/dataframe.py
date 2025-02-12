import polars as pl


class Dataframe(pl.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def read(cls, path: str) -> "Dataframe":
        df = pl.read_csv(path)
        return cls(df)

    def clean(df: "Dataframe") -> "Dataframe":
        return df.with_columns(
            [
                pl.col(col).str.strip_chars().str.to_uppercase().fill_null("Unknown")
                for col in df.columns
                if df[col].dtype == pl.Utf8
            ]
        )

    def sortByDate(df: "Dataframe") -> "Dataframe":
        return df.sort("date")

    def write(df: "Dataframe", path: str) -> None:
        df.write_csv(path)

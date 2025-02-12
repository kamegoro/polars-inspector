from domain.services import CleanDataframe


class Executer:
    def __init__(self, clean_dataframe_domain: CleanDataframe):
        self.clean_dataframe_domain = clean_dataframe_domain

    def process(self) -> None:
        result = self.clean_dataframe_domain.exec()

        result.write_csv(
            "result.csv"
        )  # 別にここで書き出す必要はないが、テストのために書いている 後で別に関数を作ってテストする

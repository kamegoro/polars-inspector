from domain.services import CleanDataframe


class Executer:
    def __init__(self, clean_dataframe_domain: CleanDataframe):
        self.clean_dataframe_domain = clean_dataframe_domain

    def process(self) -> None:
        return self.clean_dataframe_domain.exec()

from domain.dataframe import Dataframe


def csvFormatAndOrderedByDate() -> None:
    dataframe = Dataframe.read("../target.csv")

    dataframe = Dataframe.clean(dataframe)

    dataframe = Dataframe.sortByDate(dataframe)

    dataframe.write(dataframe, "../result.csv")

    return None

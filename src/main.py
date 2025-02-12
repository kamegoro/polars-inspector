from infrastructure.csv import Csv
from usecase.csv_format_and_ordered_by_date import csvFormatAndOrderedByDate


def exec():
    csvInfrascture = Csv(target_file="target.csv")

    csvFormatAndOrderedByDate(csvInfrascture)


if __name__ == "__main__":
    exec()

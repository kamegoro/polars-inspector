from infrastructure.csv import Csv
from domain.services import CleanDataframe
from usecase.precess_data import Executer


def exec():
    csvInfrastructure = Csv("target.csv")
    cleanDataframeDomain = CleanDataframe(csvInfrastructure)
    cleanExecuter = Executer(cleanDataframeDomain)

    cleanExecuter.process()

if __name__ == "__main__":
    exec()
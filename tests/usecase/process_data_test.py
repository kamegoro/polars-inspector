from unittest.mock import patch, Mock
from domain.services import CleanDataframe
from domain.models import Dataframe
from usecase.precess_data import Executer


def test_読み込んだデータのクリーンアップと集計():
    mock_clean_dataframe = Mock(spec=CleanDataframe)
    mock_clean_dataframe.exec.return_value = Dataframe({"name": ["ALICE", "BOB"]})
    cleanExecuter = Executer(mock_clean_dataframe)

    actual = cleanExecuter.process()

    expected = Dataframe({"name": ["ALICE", "BOB"]})

    assert actual.equals(expected)

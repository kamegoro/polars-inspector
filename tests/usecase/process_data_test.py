from unittest.mock import patch, Mock
from domain.services import CleanDataframe
from domain.dataframe import Dataframe
from usecase.precess_data import Executer


@patch.object(Dataframe, "write_csv")
def test_読み込んだデータのクリーンアップと集計(mock_write_csv):
    mock_clean_dataframe = Mock(spec=CleanDataframe)
    mock_clean_dataframe.exec.return_value = Dataframe({"name": ["ALICE", "BOB"]})
    cleanExecuter = Executer(mock_clean_dataframe)

    actual = cleanExecuter.process()

    assert actual is None
    mock_write_csv.assert_called_once_with("result.csv")

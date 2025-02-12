from unittest.mock import Mock, patch
from usecase.csv_format_and_ordered_by_date import csvFormatAndOrderedByDate
from port.csv import CsvPort
from domain.models import Dataframe
from domain.services import CleanDataframe


@patch("usecase.csv_format_and_ordered_by_date.pl.read_csv")
def test_CSVを読み込んで整形されて日付が降順に並び替えられる(mock_read_csv):
    mock_csv_port = Mock(spec=CsvPort)

    base_dataframe = Dataframe({"name": [" aLICE", "Bob"]})

    # csvを読み込んでDataframeを返す
    mock_read_csv.return_value = base_dataframe
    mock_clean_dataframe = Mock(spec=CleanDataframe)

    # dataframeをクリーンする
    mock_clean_dataframe.exec.return_value = Dataframe({"name": ["ALICE", "BOB"]})

    # dataframeの日付順に並び替える
    # dataframeをcsvとして吐き出す

    actual = csvFormatAndOrderedByDate(mock_csv_port)
    expected = None

    assert actual is expected
    mock_read_csv.assert_called_once_with("target.csv")
    mock_clean_dataframe.exec.assert_called_once_with(base_dataframe)

from unittest.mock import patch
from usecase.csv_format_and_ordered_by_date import csvFormatAndOrderedByDate
from domain.dataframe import Dataframe


@patch("domain.dataframe.Dataframe.write")
@patch("domain.dataframe.Dataframe.sortByDate")
@patch("domain.dataframe.Dataframe.clean")
@patch("domain.dataframe.Dataframe.read")
def test_CSVを読み込んで整形されて日付が降順に並び替えられる(mock_read, mock_clean, mock_sortByDate, mock_write):
    base_dataframe = Dataframe({"name": [" aLICE", "Bob"], "date": ["2021-01-01", "2021-01-02"]})
    cleaned_dataframe = Dataframe({"name": ["ALICE", "BOB"], "date": ["2021-01-01", "2021-01-02"]})
    ordered_dataframe = Dataframe({"name": ["ALICE", "BOB"], "date": ["2021-01-02", "2021-01-01"]})

    mock_read.return_value = base_dataframe
    mock_clean.return_value = cleaned_dataframe
    mock_sortByDate.return_value = ordered_dataframe
    mock_write.return_value = None

    actual = csvFormatAndOrderedByDate()
    expected = None

    assert actual is expected
    mock_read.assert_called_once_with("../target.csv")
    mock_clean.assert_called_once_with(base_dataframe)
    mock_sortByDate.assert_called_once_with(cleaned_dataframe)
    mock_write.assert_called_once_with(ordered_dataframe, "../result.csv")
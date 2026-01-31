import pytest

from src import processing


@pytest.mark.parametrize(
    "dicts_list, expected_dicts_list, state_value",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 41435529, "state": "", "date": "2016-11-02T19:31:20.516566"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
            ],
            "EXECUTED",
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 41435529, "state": "", "date": "2016-11-02T19:31:20.516566"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
            ],
            [
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 41435529, "state": "", "date": "2016-11-02T19:31:20.516566"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
            ],
            [{"id": 41435529, "state": "", "date": "2016-11-02T19:31:20.516566"}],
            "",
        ),
        ([], [], "EXECUTED"),
    ],
)
def test_filter_by_state(dicts_list, expected_dicts_list, state_value):
    assert processing.filter_by_state(dicts_list, state=state_value) == expected_dicts_list


@pytest.mark.parametrize(
    "dicts_list, expected_dicts_list",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
            ],
        )
    ],
)
def test_filter_by_state_default(dicts_list, expected_dicts_list):
    assert processing.filter_by_state(dicts_list) == expected_dicts_list


def test_filter_by_state_invalid_elements_type(invalid_elements_data):
    with pytest.raises(ValueError):
        assert processing.filter_by_state(invalid_elements_data)


def test_filter_by_state_invalid_type(dicts_list_invalid_type):
    with pytest.raises(TypeError):
        assert processing.filter_by_state(dicts_list_invalid_type)


@pytest.mark.parametrize(
    "dicts_list, expected_dicts_list, reversion",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 939719585, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.41"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:48.3"},
            ],
            [
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.41"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719585, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:48.3"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
            ],
            True,
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 939719585, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:48.333333"},
            ],
            [
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:48.333333"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719585, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
            ],
            False,
        ),
    ],
)
def test_sort_by_date(dicts_list, expected_dicts_list, reversion):
    assert processing.sort_by_date(dicts_list, sort_reverse=reversion) == expected_dicts_list


@pytest.mark.parametrize(
    "dicts_list, expected_dicts_list",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:48.333333"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
                {"id": 939719585, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
            ],
            [
                {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719585, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:48.333333"},
                {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
            ],
        )
    ],
)
def test_sort_by_date_default_sort_reverse(dicts_list, expected_dicts_list):
    assert processing.sort_by_date(dicts_list) == expected_dicts_list


def test_sort_by_date_invalid_type(dicts_list_invalid_type):
    with pytest.raises(TypeError):
        assert processing.sort_by_date(dicts_list_invalid_type)


@pytest.mark.parametrize(
    "dicts_list",
    [
        ([{"id", 41428829, "state", "EXECUTED", "date", "2019-07-03T18:35:29.364"}]),
        ([["id", 939719570, "state", "EXECUTED", "date", "2018-06-30T02:08:58.425572"]]),
        ([("id", 698729329, "state", "PROCESSED", "data", "2023-12-12T05:48:55.344688")]),
    ],
)
def test_sort_by_date_incorrect_data(dicts_list):
    with pytest.raises(ValueError):
        processing.sort_by_date(dicts_list)


def test_sort_by_date_incorrect_date_value(dicts_list_incorrect_date, capsys):
    processing.sort_by_date(dicts_list_incorrect_date)
    captured = capsys.readouterr()
    console_message = """Транзакция имеет некорректный формат даты
Транзакция имеет некорректный формат даты
Транзакция имеет некорректный формат даты
"""
    assert captured.out == console_message

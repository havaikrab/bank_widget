import pytest

from src import processing

@pytest.mark.parametrize('dicts_list, expected_dicts_list, state_value',[([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                                           {'id': 698729329, 'state': 'PROCESSED', 'date': '2023-12-12T05:48:55.344688'},
                                                                           {'id': 89223248, 'state': 'CANCELED', 'date': '2005-01-12T21:16:25.247425'},
                                                                           {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-03T23:27:01.533689'},
                                                                           {'id': 615064591, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'}],
                                                                          [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                                           {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-03T23:27:01.533689'}],
                                                                          'EXECUTED'),

                                                                         ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                                           {'id': 698729329, 'state': 'PROCESSED', 'date': '2023-12-12T05:48:55.344688'},
                                                                           {'id': 89223248, 'state': 'CANCELED', 'date': '2005-01-12T21:16:25.247425'},
                                                                           {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-03T23:27:01.533689'},
                                                                           {'id': 615064591, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'}],
                                                                          [{'id': 89223248, 'state': 'CANCELED', 'date': '2005-01-12T21:16:25.247425'},
                                                                           {'id': 615064591, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'}],
                                                                          'CANCELED')])
def test_filter_by_state(dicts_list, expected_dicts_list, state_value):
    assert processing.filter_by_state(dicts_list, state=state_value) == expected_dicts_list


@pytest.mark.parametrize('dicts_list, expected_dicts_list',[([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                              {'id': 698729329, 'state': 'PROCESSED', 'date': '2023-12-12T05:48:55.344688'},
                                                              {'id': 89223248, 'state': 'CANCELED', 'date': '2005-01-12T21:16:25.247425'},
                                                              {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-03T23:27:01.533689'},
                                                              {'id': 615064591, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'}],
                                                             [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                              {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-03T23:27:01.533689'}])])
def test_filter_by_state_default(dicts_list, expected_dicts_list):
    assert processing.filter_by_state(dicts_list) == expected_dicts_list

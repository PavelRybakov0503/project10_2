from typing import Any, Dict, List, Union

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def entered_list() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def executed_list() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def date_list() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# def test_filter_by_state(entered_list: list, executed_list: list) -> None:
#     assert filter_by_state(entered_list) == executed_list


def test_filter_by_state(entered_list: list, executed_list: list) -> None:
    assert filter_by_state(entered_list, state="EXECUTED") == executed_list


def test_sort_by_date(entered_list: str, date_list: list[Any]) -> None:
    assert sort_by_date(entered_list) == date_list

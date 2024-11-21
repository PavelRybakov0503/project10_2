from typing import Any

list_of_dicts = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_of_dict: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """
    Функция принимает на вход список словарей и значение для ключа и возвращает новый
    список содержащий только те словари у которых ключ содержит переданное в функцию
    значение.
    """
    return [d for d in list_of_dict if d.get("state") == state]


def sort_by_date(
    list_of_dict: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """
    Функция принимает на вход список словарей и возвращает новый список, в котором исходные
    словари отсортированы по убыванию даты
    """
    sorted_list = sorted(
        list_of_dict,
        key=lambda new_list_of_dict: new_list_of_dict["date"],
        reverse=reverse,
    )
    return sorted_list

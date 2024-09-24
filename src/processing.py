from typing import Any


def filter_by_state(data_list: Any, state: Any) -> list:
    """
    Функция принимает на вход список словарей и значение для ключа и возвращает новый
   список содержащий только те словари у которых ключ содержит переданное в функцию
   значение.
   """
    return [entry for entry in data_list if entry.get('state') == state]


def sort_by_date(data_list: str, reverse: bool = False) -> list:
    """
       Функция принимает на вход список словарей и значение для ключа и возвращает новый
      список содержащий только те словари у которых ключ содержит переданное в функцию
      значение.
      """
    from datetime import datetime
    return sorted(data_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=reverse)

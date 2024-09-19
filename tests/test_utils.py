import os

from unittest.mock import patch

import pytest

from src.utils import financial_transactions, transaction_amount


@pytest.fixture
def path():
    """Возвращает путь к файлу операций JSON в тестовом наборе."""
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


@pytest.fixture
def path_empty_list():
    """Возвращает путь к пустому файлу операций JSON в тестовом наборе."""
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_1.json")
    return PATH_TO_FILE


@pytest.fixture
def path_mistake_json():
    """Возвращает путь к файлу операций JSON с ошибками в тестовом наборе."""
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_2.json")
    return PATH_TO_FILE


@pytest.fixture
def trans():
    """Возвращает пример транзакции для тестов."""
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
         "amount": "31957.58",
         "currency": {
          "name": "руб.",
          "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


@pytest.fixture
def trans_1():
    """Возвращает пример транзакции с валютой, отличной от RUB, для тестов."""
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_financial_transactions_nofile():
    """Проверяет, что функция financial_transactions возвращает пустой список для несуществующего файла."""
    assert financial_transactions('nofile') == []


def test_financial_transactions(path):
    """Проверяет, что первая транзакция из файла операций совпадает с ожидаемой."""
    assert financial_transactions(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_financial_transactions_empty_list(path_empty_list):
    """Проверяет, что функция financial_transactions возвращает пустой список для файла с отсутствующими
     транзакциями."""
    assert financial_transactions(path_empty_list) == []


def test_financial_transactions_mistake_json(path_mistake_json):
    """Проверяет, что функция financial_transactions возвращает пустой список для файла с ошибками формата JSON."""
    assert financial_transactions(path_mistake_json) == []


def test_transaction_amount(trans):
    """Проверяет, что функция transaction_amount возвращает правильное значение суммы транзакции."""
    assert transaction_amount(trans) == '31957.58'


@patch('src.utils.currency_conversion')
def test_transaction_amount_non_rub(mock_currency_conversion, trans_1):
    """Проверяет, что функция transaction_amount корректно обрабатывает транзакцию в валюте, отличной от RUB,
     с учетом мокирования конвертации валют."""
    mock_currency_conversion.return_value = 1000.0
    assert transaction_amount(trans_1) == 1000.0
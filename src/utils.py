import json
import os
import logging
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion

logger = logging.getLogger('utils')
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler('logs/utils.log')
# file_formatter = logging.Formatter('%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s',
# file_handler.setFormatter(file_handler)
# logger.addHandler(file_handler)
#

(logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename="../logs/utils_log.log",
    filemode="w",))
utils_logger = logging.getLogger('utils')

financial_transactions_logger = logging.getLogger()
transaction_amount_logger = logging.getLogger()

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        financial_transactions_logger.info("Открываю файл с транзакциями")
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                financial_transactions_logger.error("Ошибка файла с транзакциями")
                return []
        if not isinstance(transactions, list):
            financial_transactions_logger.error("Список транзакций пуст")
            return []
        financial_transactions_logger.info("Создан список словарей с данными о финансовых транзакциях")
        return transactions
    except FileNotFoundError:
        financial_transactions_logger.error("Файл с транзакциями не найден")
        return []


# def financial_transactions(path: str) -> Any:
#     """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
#     транзакциях."""
#     try:
#         with open(path, encoding="utf-8") as financial_file:
#             try:
#                 transactions = json.load(financial_file)
#             except JSONDecodeError:
#                 return []
#         if not isinstance(transactions, list):
#             return []
#         return transactions
#     except FileNotFoundError:
#         return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        transaction_amount_logger.info("Код валюты в транзакции RUB")
    else:
        amount = currency_conversion([trans])
        transaction_amount_logger.info("Код валюты транзакции не RUB, произведена конвертация")
    return amount


# def transaction_amount(trans: Any, currency: str = "RUB") -> Any:
#     """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
#     if trans["operationAmount"]["currency"]["code"] == currency:
#         amount = trans["operationAmount"]["amount"]
#     else:
#         amount = currency_conversion(trans)
#     return amount

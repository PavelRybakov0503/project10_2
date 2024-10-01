from typing import Dict, List

import pandas as pd
import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("reading_csv_excel")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

PATH_TO_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
PATH_TO_EXCEL = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def read_operations_from_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Читает финансовые операции из CSV файла.

    :param file_path: Путь к файлу CSV.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(file_path, sep=';')
    return df.astype(str).to_dict(orient='records')
#    return df.to_dict(orient='records')


def read_operations_from_excel(file_path: str) -> List[Dict[str, str]]:
    """
    Читает финансовые операции из Excel файла.

    :param file_path: Путь к файлу Excel.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

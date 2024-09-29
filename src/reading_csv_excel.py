from typing import Dict, List

import pandas as pd


def read_operations_from_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Читает финансовые операции из CSV файла.

    :param file_path: Путь к файлу CSV.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(file_path, sep=';')
    return df.to_dict(orient='records')


def read_operations_from_excel(file_path: str) -> List[Dict[str, str]]:
    """
    Читает финансовые операции из Excel файла.

    :param file_path: Путь к файлу Excel.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

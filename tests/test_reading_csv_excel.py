from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.reading_csv_excel import read_operations_from_csv, read_operations_from_excel


@pytest.fixture
def mock_csv_data() -> str:
    return
"""id;state;date;amount;currency_name;currency_code;from;to;description
    650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;
    Счет 39745660563456619397;Перевод организации 3598919;EXECUTED;
    2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;
    Discover 0720428384694643;Перевод с карты на карту
    """


@pytest.fixture
def mock_excel_data():
    data = {
        'id': ['650703'],
        'state': ['EXECUTED'],
        'date': ['2023-09-05T11:30:32Z'],
        'amount': ['16210'],
        'currency_name': ['Sol'],
        'currency_code': ['PEN'],
        'from': ['Счет 58803664561298323391'],
        'to': ['Счет 39745660563456619397'],
        'description': ['Перевод организации']
    }
    return pd.DataFrame(data)


def test_read_operations_from_csv(mock_csv_data) -> None:
    with patch('builtins.open', mock_open(read_data=mock_csv_data)):
        result = read_operations_from_csv('dummy_path.csv')
        expected = [
            {
                'id': '650703',
                'state': 'EXECUTED',
                'date': '2023-09-05T11:30:32Z',
                'amount': '16210',
                'currency_name': 'Sol',
                'currency_code': 'PEN',
                'from': 'Счет 58803664561298323391',
                'to': 'Счет 39745660563456619397',
                'description': 'Перевод организации'
            },
            {
                'id': '3598919',
                'state': 'EXECUTED',
                'date': '2020-12-06T23:00:58Z',
                'amount': '29740',
                'currency_name': 'Peso',
                'currency_code': 'COP',
                'from': 'Discover 3172601889670065',
                'to': 'Discover 0720428384694643',
                'description': 'Перевод с карты на карту'
            }
        ]
        assert result == expected


def test_read_operations_from_excel(mock_excel_data):
    with patch('pandas.read_excel', return_value=mock_excel_data):
        result = read_operations_from_excel('dummy_path.xlsx')
        expected = [{
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }]
        assert result == expected
from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_data


def test_get_mask_card_number():
    assert get_mask_card_number('1234567812345678') == '1234 56** **** 5678'
    # assert get_mask_card_number('1234') == '1234'
    # assert get_mask_card_number('') == 'Invalid input'
    # assert get_mask_card_number('************3456') != '7000 79** **** 6361'
    # assert get_mask_card_number(1234567890123456) == 'Invalid input'
    # assert get_mask_card_number(None) == 'Invalid input'
    # assert get_mask_card_number('12345678901234567890') == '******************7890'
    assert get_mask_card_number('1234') == 'Invalid card number length'
    assert get_mask_card_number('123456781234567890') == 'Invalid card number length'
    # Тестирование с пустой строкой
    assert get_mask_card_number('') == 'Invalid input'
    # Тестирование с нестроковым входом
    assert get_mask_card_number(1234567812345678) == 'Invalid input'
    # Тестирование с None
    assert get_mask_card_number(None) == 'Invalid input'
    # Тестирование с номером карты, состоящим только из символов
    assert get_mask_card_number('************') == 'Invalid card number length'
    # Тестирование с номером карты, содержащим пробелы и спецсимволы
    assert get_mask_card_number('1234 5678-1234!5678') == '1234 56** **** 5678'
    # Тестирование с номером карты, состоящим из цифр и пробелов
    assert get_mask_card_number('123456 781234 5678') == '1234 56** **** 5678'

def test_get_mask_account():
    assert get_mask_account('12345678') == '**5678'
    assert get_mask_account('1234') != 'None'


def test_mask_account_card():
    assert mask_account_card('1234567890123456') == '1234 56** **** 3456'
    assert mask_account_card('12345678') == '**5678'
    assert mask_account_card('123') == 'Invalid input'


def test_get_data():
    assert get_data('2023-10-01') == '01-10-2023'
    assert get_data('invalid_date') == 'Invalid date format'
    assert get_data('') == 'Invalid date'


def test_filter_by_state(sample_data):
    assert filter_by_state(sample_data, 'active') == [
        {'state': 'active', 'date': '2023-01-01'},
        {'state': 'active', 'date': '2023-01-03'}
    ]


def test_sort_by_date(sample_data):
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]['date'] == '2023-01-01'  # Ascending order
    assert sorted_data[-1]['date'] == '2023-01-03'
    sorted_data_desc = sort_by_date(sample_data, reverse=True)
    assert sorted_data_desc[0]['date'] == '2023-01-03'  # Descending order
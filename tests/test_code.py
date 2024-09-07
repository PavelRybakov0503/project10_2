from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_data


def test_get_mask_card_number():
    assert get_mask_card_number('1234567890123456') == '************3456'
    assert get_mask_card_number('1234') == '1234'
    assert get_mask_card_number('') == 'Invalid input'


def test_get_mask_account():
    assert get_mask_account('12345678') == '**5678'
    assert get_mask_account('1234') != 'None'


def test_mask_account_card():
    assert mask_account_card('1234567890123456') == '************3456'
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
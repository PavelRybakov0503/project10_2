import json
import unittest
from unittest.mock import patch
from src.external_api import currency_conversion  # Замените 'your_module' на имя вашего модуля
from json import JSONDecodeError


class TestCurrencyConversion(unittest.TestCase):
    @patch('requests.get')
    def test_conversion_rub(self, mock_get):
        # Тестируем, когда валюта уже RUB
        transaction_data = [{
            "operationAmount": {
                "amount": 1000,
                "currency": {"code": "RUB"}
            }
        }]

        result = currency_conversion(transaction_data)
        self.assertEqual(result, 1000.0)

    @patch('requests.get')
    def test_conversion_usd_to_rub(self, mock_get):
        # Тестируем конвертацию из USD в RUB
        mock_response = {
            "result": 75000.0
        }
        mock_get.return_value.ok = True
        mock_get.return_value.text = json.dumps(mock_response)

        transaction_data = [{
            "operationAmount": {
                "amount": 100,
                "currency": {"code": "USD"}
            }
        }]

        result = currency_conversion(transaction_data)
        self.assertEqual(result, 75000.0)

    @patch('requests.get')
    def test_conversion_eur_to_rub(self, mock_get):
        # Тестируем конвертацию из EUR в RUB
        mock_response = {
            "result": 85000.0
        }
        mock_get.return_value.ok = True
        mock_get.return_value.text = json.dumps(mock_response)

        transaction_data = [{
            "operationAmount": {
                "amount": 100,
                "currency": {"code": "EUR"}
            }
        }]

        result = currency_conversion(transaction_data)
        self.assertEqual(result, 85000.0)

    @patch('requests.get')
    def test_conversion_invalid_currency(self, mock_get):
        # Тестируем ситуацию с неверной валютой
        transaction_data = [{
            "operationAmount": {
                "amount": 1000,
                "currency": {"code": "ABC"}
            }
        }]

        result = currency_conversion(transaction_data)
        self.assertEqual(result, 0.0)

    @patch('requests.get')
    def test_conversion_error_response(self, mock_get):
        # Тестируем ситуацию, когда API возвращает ошибку
        mock_get.return_value.ok = False

        transaction_data = [{
            "operationAmount": {
                "amount": 100,
                "currency": {"code": "USD"}
            }
        }]

        result = currency_conversion(transaction_data)
        self.assertEqual(result, 0.0)


if __name__ == "__main__":
    unittest.main()
import os
import json
from locale import currency

import requests

values = os.getenv("PASSWORD")


def currency_conversion(transaction_data: list, API_KEY=None) -> float:
    """Функция конвертации       """
    code = transaction_data[0].get("operationAmount").get("currency").get("code")
    amount = transaction_data[0].get("operationAmount").get("amount")

    try:
        if code == "RUB":
            return float(amount)  # Убедитесь, что возвращаете float
        elif code in ['USD', 'EUR']:  # Можно использовать in для упрощения
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            headers = {"apikey": API_KEY}  # Заголовки использует apikey
            payload = {
                "amount": amount,
                "from": code,
                "to": "RUB"
            }
            response = requests.get(url, headers=headers, params=payload)

            if response.ok:
                obj = json.loads(response.text)
                if 'result' in obj:
                    amount = obj.get("result")
                    return round(float(amount), 2)  # Убедитесь, что возвращаем float и округляем до 2 знаков

    except Exception as e:  # Лучше выводить информацию об ошибке
        print(f"Что-то пошло не так: {e}")

    return 0.0  # Возврат float, если что-то не так

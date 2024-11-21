from src1.masks import get_mask_account, get_mask_card_number

def mask_account_card(number: str) -> str:
    '''Принимает на вход строку формата'''
    if len(number) == 16 and number.isdigit():  # Проверка на 16 цифр
        return get_mask_card_number(number)  # Применяем маску для номера карты
    else:
        cards = get_mask_account(number[-16:])  # Маскируем последние 16 символов
        new_cards = number.replace(number[-16:], cards)
        return new_cards

def get_date(date: str) -> str:
    '''Функция преобразования даты'''
    return f'{date[8:10]},{date[5:7]},{date[0:4]}'
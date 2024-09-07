from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    '''Принимает на вход строку формата'''
    if len(input_data) == 16:  # Предполагаем, что номер карты составляет 16 цифр
        return get_mask_card_number(input_data)
    elif len(input_data) >= 8:  # Предполагаем, что номер счета состоит из 8 и более цифр
        return get_mask_account(input_data)
    else:
        return "Invalid input"


def get_data(date_string: str) -> str:
    '''Функция преобразования даты'''
    if not date_string:
        return "Invalid date"
        # Пробуем преобразовать строку в дату
    try:
        from datetime import datetime
        return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d-%m-%Y')
    except ValueError:
        return "Invalid date format"

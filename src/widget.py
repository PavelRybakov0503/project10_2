from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает замаскированный номер"""
    divide_string = type_and_number.split(" ")
    type_card = []

    for i in divide_string:
        if i == "Счет":
            return f"{divide_string[0]} {get_mask_account(divide_string[-1])}"
        else:
            type_card.append(i)

    type_card_name = " ".join(type_card[:-1])
    return f"{type_card_name} {get_mask_card_number(divide_string[-1])}"


def get_date(format_data: str) -> str:
    """Функция преобразует формат даты"""
    return f"{format_data[8:10]}.{format_data[5:7]}.{format_data[:4]}"

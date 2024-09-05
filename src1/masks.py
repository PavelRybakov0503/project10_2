def get_mask_card_number(cart_number: str) -> str | None:
    """Принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if cart_number.isdigit() and len(cart_number) == 16:
        return f"{cart_number[:5]} {cart_number[5:7]}{"*" * 2} {"*" * 4} {cart_number[12:]}"
    else:
        return None


def get_mask_account(acc_number: str) -> str | None:
    """Принимает на вход номер счета в виде числа и возвращает маску
    номера по правилу **XXXX"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        return None

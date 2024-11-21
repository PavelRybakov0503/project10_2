import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
#     filename="../logs/masks_log.log",
#     filemode="w",)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    filename='logs/masks.log',
                    filemode='w')
mask_logger = logging.getLogger('masks')
card_number_logger = logging.getLogger()
mask_account_logger = logging.getLogger()


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    7000 79** **** 6361"""
    card_number_logger.info("Создаю маску номера карты")
    if len(str(card_number)) != 16:
        card_number_logger.error("Неправильный номер карты")
        raise ValueError("Неправильный номер карты")
    card_number_logger.info("Маска номера карты создана")
    return f"{int(str(card_number)[:4])} {int(str(card_number)[4:6])}** **** {int(str(card_number)[12:])}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    **4305"""
    mask_account_logger.info("Создаю маску номера счета")
    if len(str(account_number)) != 20:
        mask_account_logger.error("Неправильный номер счета")
        raise ValueError("Неправильный номер счета")
    mask_account_logger.info("Маска номера счета создана")
    return f"**{int(str(account_number)[-4:])}"

# # def get_mask_card_number(card_number: str) -> str:
# #     """Принимает на вход номер карты в виде числа и
# #     возвращает маску номера по правилу XXXX XX** **** XXXX"""
# #     if not card_number or not isinstance(card_number, str):
# #         return "Invalid input"
# #     return '*' * (len(card_number) - 4) + card_number[-4:]
#
#
# def get_mask_card_number(card_number: str) -> str:
#     """Принимает на вход номер карты в виде числа и
#     возвращает маску номера по правилу XXXX XX** **** XXXX"""
#     if not card_number or not isinstance(card_number, str):
#         return "Invalid input"
#
#     # Удаляем все нецифровые символы
#     card_number = ''.join(filter(str.isdigit, card_number))
#
#     if len(card_number) != 16:
#         return "Invalid card number length"
#
#     return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
#
#
# # def get_mask_account(account_number: str) -> str:
# #     """Принимает на вход номер счета в виде числа и возвращает маску
# #     номера по правилу **XXXX"""
# #     if not account_number or not isinstance(account_number, str):
# #         return "Invalid input"
# #     return '*' * (len(account_number) - 4) + account_number[-4:]
#
# def get_mask_account(acc_number: str) -> str | None:
#     """Принимает на вход номер счета в виде числа и возвращает маску
#     номера по правилу **XXXX"""
#     if acc_number.isdigit() and len(acc_number) == 8:
#         return f"{'*' * 2}{acc_number[-4::]}"
#     else:
#         return None
#
# # def get_mask_account(account_number, get_mask_account=None):
# #     # Преобразуем номер счета в строку и извлекаем последние 4 символа
# #     get_mask_account = '**' + account_number[-4:]
# #     return get_mask_account

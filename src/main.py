from time import sleep

from src.processing import filter_by_state, sort_by_date
from src.reading_csv_excel import PATH_TO_CSV, PATH_TO_EXCEL, read_operations_from_csv, read_operations_from_excel
from src.utils import PATH_TO_FILE, financial_transactions
from src.widget import get_date, mask_account_card
from src.search_transactions import search_transaction


def greeting() -> list:
    """Функция приветствует и предлагает выбрать из какого файла считать данные
    и возвращает список словарей с транзакциями"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    user_input = input("Введите номер пункта меню: ")
    while True:
        if user_input == "1":
            print("Для обработки выбран JSON-файл.")
            return financial_transactions(PATH_TO_FILE)
        elif user_input == "2":
            print("Для обработки выбран CSV-файл.")
            return read_operations_from_csv(PATH_TO_CSV)
        elif user_input == "3":
            print("Для обработки выбран EXCEL-файл.")
            return read_operations_from_excel(PATH_TO_EXCEL)
        else:
            print("Пожалуйста, введите число от 1 до 3.")
            user_input = input()


def choice_status(transactions: list) -> list:
    """Функция предлагает по какому статусу отфильтровать транзакции."""

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    user_status = input().upper()

    while True:
        if user_status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {user_status} недоступен.")
            print("Введите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            user_status = input().upper()
        else:
            break
    print(f"Операции отфильтрованы по статусу {user_status}")
    return filter_by_state(transactions, user_status)


def sorting_by_date(transactions: list) -> list:
    """Функция предлагает отсортировать транзакции по дате."""

    sorted_by_date = input("Отсортировать операции по дате? Да/Нет").lower()
    if sorted_by_date in ["да", "yes", "lf"]:
        rev = input("Отсортировать по возрастанию или по убыванию?").lower()
        if rev == "по возрастанию":
            return sort_by_date(transactions, is_reverse=False)
        else:
            return sort_by_date(transactions)
    else:
        return transactions


def only_rub(transactions: list) -> list:
    """Функция предлагает выводить только рублевые транзакции или нет"""
    print("Выводить только рублевые транзакции? Да/Нет")
    choice_currency = input().lower()
    if choice_currency in ["да", "yes", "lf"]:
        result = []
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                result.append(transaction)
        return result
    else:
        return transactions


def sorting_by_word(transactions: list) -> list:
    """Функция предлагает отфильтровать транзакции по ключевому слову"""
    print("Отфильтровать список транзакций по определенному слову описании? Да/Нет")
    user_input = input().lower()
    if user_input in ["да", "yes", "lf"]:
        user_word = input("Введите слово для сортировки").lower()
        return search_transaction(transactions, user_word)
    else:
        return transactions


def output_result(transactions: list) -> None:
    """Вывод информации по транзакциям с учетом фильтров"""

    if transactions:
        print("Программа: Распечатываю итоговый список транзакций...")
        sleep(1)
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        sleep(1)
        for transaction in transactions:
            date = get_date(transaction.get("date"))
            description = transaction.get("description")
            mask_to = mask_account_card(transaction.get("to"))
            amount = transaction.get("operationAmount")["amount"]

            if description == "Открытие вклада":
                print(f"{date} {description}")
                print(mask_to)
                print(f"Сумма: {amount}")
            else:
                mask_from = mask_account_card(transaction.get("from", "Нет данных"))
                print(f"{date} {description}")
                print(f"{mask_to} -> {mask_from}")
                print(f"Сумма: {amount}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main() -> None:
    start = greeting()
    status = choice_status(start)
    sorting = sorting_by_date(status)
    currency = only_rub(sorting)
    filtered_transactions = sorting_by_word(currency)
    output_result(filtered_transactions)


if __name__ == "__main__":
    main()

#
# import os
#
# from config import DATA_DIR
# from src.processing import filter_by_state, sort_by_date
# from src.reading_csv_excel import read_operations_from_csv, read_operations_from_excel
# from src.search_transactions import search_transactions
# from src.utils import financial_transactions, transaction_amount
# from src.widget import get_date, mask_account_card
#
#
# def main() -> None:
#     """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""
#     global list_transactions
#     while True:
#         print(
#             """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
#         Выберите необходимый пункт меню:
#         1. Получить информацию о транзакциях из JSON-файла
#         2. Получить информацию о транзакциях из CSV-файла
#         3. Получить информацию о транзакциях из XLSX-файла"""
#         )
#         user_file_choice = input().strip()
#         if user_file_choice == "1":
#             print("Для обработки выбран JSON-файл.")
#             list_transactions = financial_transactions(os.path.join(DATA_DIR,
#             "D:\py\project10_2\data\operations.json.py"))
#             break
#         elif user_file_choice == "2":
#             print("Для обработки выбран CSV-файл.")
#             list_transactions = read_operations_from_csv(os.path.join(DATA_DIR, "transactions.csv"))
#             break
#         elif user_file_choice == "3":
#             print("Для обработки выбран XLSX-файл.")
#             list_transactions = read_operations_from_excel(os.path.join(DATA_DIR, "transactions_excel.xlsx"))
#             break
#         else:
#             print("Некорректный выбор. Попробуйте еще раз.")
#             continue
#
#     filters: dict[str, str | bool] = {}
#     while True:
#         status = input(
#             "Введите статус, по которому необходимо выполнить фильтрацию. "
#             "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
#         ).upper()
#         if status in ["CANCELED", "PENDING", "EXECUTED"]:
#             filters["status"] = status
#             print(f"Операции отфильтрованы по статусу {status}")
#             break
#         else:
#             print("Некорректный выбор. Попробуйте еще раз.")
#             continue
#     while True:
#         sort_date = input("Отсортировать операции по дате?  Да/Нет\n").lower()
#         if sort_date == "да":
#             while True:
#                 sorting_order = input(
#                     """Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n"""
#                 ).lower()
#                 if sorting_order == "по возрастанию":
#                     filters["date"] = False
#                     break
#                 elif sorting_order == "по убыванию":
#                     filters["date"] = True
#                     break
#                 else:
#                     print("Некорректный выбор. Попробуйте еще раз.")
#                     continue
#             break
#         elif sort_date == "нет":
#             break
#         else:
#             print("Некорректный выбор. Попробуйте еще раз.")
#             continue
#     while True:
#         sort_code = str(input("Выводить только рублевые транзакции? Да/Нет\n")).lower()
#         if sort_code == "да":
#             filters["currency"] = "RUB"
#             break
#         elif sort_code == "нет":
#             break
#         else:
#             print("Некорректный выбор. Попробуйте еще раз.")
#             continue
#     while True:
#         user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
#         if user_input == "да":
#             search = input("Видите слово для поиска: ")
#             filters["description"] = search
#             break
#         elif user_input == "нет":
#             break
#         else:
#             print("Некорректный выбор. Попробуйте еще раз.")
#             continue
#
#     transactions = list_transactions
#     for filter_type, filter_value in filters.items():
#         if filter_type == "status":
#             transactions = filter_by_state(transactions, filter_value)
#         elif filter_type == "date":
#             transactions = sort_by_date(transactions, filter_value)
#         elif filter_type == "currency":
#             transactions = [
#                 txn
#                 for txn in transactions
#                 if txn.get("operationAmount", {}).get("currency", {}).get("code") == filter_value
#             ]
#         elif filter_type == "description":
#             transactions = search_transactions(transactions, filter_value)
#
#     if not transactions:
#         print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
#         return
#
#     print("Распечатываю итоговый список транзакций...")
#     print(f"Всего банковских операций в выборке: {len(transactions)}")
#     for transaction in transactions:
#         description = transaction.get("description")
#         if description == "Открытие вклада":
#             from_ = description
#         else:
#             from_ = mask_account_card(transaction.get("from"))
#
#         to_ = mask_account_card(transaction.get("to"))
#         date = get_date(transaction.get("date"))
#
#         amount = transaction["operationAmount"]["amount"]
#         currency = transaction["operationAmount"]["currency"]["name"]
#
#         if description == "Открытие вклада":
#             print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
#         else:
#             print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")
#
#
# if __name__ == "__main__":
#     main()

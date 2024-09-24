from typing import Any, Dict, Generator, Iterator, List


def filter_by_currency(transaction_list: List[Dict[str, Any]], name: str) -> Iterator[Dict[str, Any]]:
    """Функция выдает список трансакций с определенной валютой"""
    for transaction in transaction_list:
        operation_amount = transaction.get("operationAmount")
        if operation_amount is not None:
            currency = operation_amount.get("currency")
            if currency is not None and currency.get("name") == name:
                yield transaction


def transaction_descriptions(transactions_list: Any) -> Any:
    """Функция выдает описание операций"""
    description_of_transactions = ""
    for transact in transactions_list:
        description_of = transact["description"]
        description_of_transactions = (
            description_of_transactions + description_of + "/n"
        )
    description_of_transactions_list = description_of_transactions.split("/n")
    for transaction in description_of_transactions_list:
        yield transaction


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Функция генерирует номера карт"""
    for number in range(start, end + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number

        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

        yield (formatted_card_number)


# gen_number = card_number_generator(1,3)
# print(next(gen_number))
# print(next(gen_number))
# print(next(gen_number))

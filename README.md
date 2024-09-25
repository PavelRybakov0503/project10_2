# БАНК

## Описание:

Проект БАНК - это функции на Python для управления счетами, картами и датами.
Данный проект включает в себя функции для маскировки номеров карт и аккаунтов,
а также для обработки данных.
Функции позволяют фильтровать данные по состоянию и сортировать записи по дате.

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/PavelRybakov0503/project11_1/pulls
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Тестирование:

Для проверки работы функций разработаны тесты, которые выполняют основные проверки на корректность.
Используются утверждения для проверки ожидаемых результатов.
Примечания:
- Входные параметры должны быть корректными, в противном случае функции могут вернуть
- сообщения об ошибках, например, "Invalid input" или "Invalid date format".

Как использовать:
1. Импортируйте необходимые функции из модуля.
2. Вызывайте функции с необходимыми параметрами и обрабатывайте их результаты.

## Использование

1. Модуль widget.py принимает Наименование карты или счет и номер и возвращает замаскированный номер
2. Модуль processing.py принимает список операций и возвращает отсортированные по успешности и по дате списки
3. Модуль generators.py сортирует списки операций и генерирует номера карт
4. Модуль decorators.py автоматически логирует начало и конец выполнения функции, а также ее результаты или
возникшие ошибки
5. Модуль masks. 
5.1 Принимает номер карты отдает на выход маску номера карты
- функция get_mask_card_number
- пример маски номера 7000 79** **** 6361
5.2 Принимает номер счета отдает на выход маску номера счета
- функция get_mask_account
- пример маски номера **4305
6. Модуль utils. 
- Функция financial_transactions принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
- JSON-файл находится в директории data.
- Функция transaction_amount принимает на вход транзакцию и возвращает сумму транзакции в рублях.
7. Модуль external_api.
Функция конвертации currency_conversion, используется функцией transaction_amount, если валюта транзакции не рубль.

## Логирование

Файлы логов записываются в папку logs
Для модуля masks.py - masks_log.log
Для модуля utils.py - utils_log.log
Файлы логов перезаписываемые

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по Creative Commons Legal Code (LICENSE).
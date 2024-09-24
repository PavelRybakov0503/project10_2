from typing import Any
from src.decorators import log


@log()
def my_function(x: int, y: int) -> float:
    """Делит x на y и возвращает результат.
        Args: x (int): Делимое.
        y (int): Делитель.
        Returns:
        float: Результат деления.
        Raises:
        ZeroDivisionError: Если y равен 0.
    """
    return x / y


def test_log_print(capsys: Any) -> Any:
    """Тестирует вывод журнала для успешного выполнения функции.
        Args:
            capsys (Any): Фиксатор для захвата стандартного вывода.
    """
    my_function(10, 5)
    captured = capsys.readouterr()
    expected_output = ("my_function started\n""my_function ok\n""my_function finished\n")
    assert captured.out == expected_output


def test_log_print_try(capsys: Any) -> Any:
    """Тестирует вывод журнала при возникновении ошибки деления на ноль.
        Args: capsys (Any): Фиксатор для захвата стандартного вывода."""
    my_function(10, 0)
    captured = capsys.readouterr()
    expected_output = ("my_function started\n""my_function error: division by zero. Inputs: (10, 0), {}\n")
    assert captured.out == expected_output


def test_log_print_fail(tmp_path: Any) -> None:
    """Тестирует функцию логирования для успешного выполнения.

        Args:
            tmp_path (Any): Временный путь для создания файла вывода.
        """
    log_file = tmp_path / "test_output.txt"

    @log(log_file)
    def my_function(x: int, y: int) -> Any:
        """Локальная функция для тестирования. Делит x на y."""
        return x / y
    my_function(10, 5)
    with open(log_file, "r") as f:
        content = f.read()
    assert content == "my_function ok\n"


# def test_log_print_fail_try(tmp_path):
#     log_file = tmp_path / "test_output.txt"
#
#     @log(log_file)
#     def my_function(x, y):
#         return x / y
#
#     my_function(10, 0)
#     with open(log_file, "r") as f:
#         content = f.read()
#     assert content == "my_function error: division by zero. Inputs: (10, 0), {}"


def test_log_print_fail_try(tmp_path: Any) -> None:
    """Тестирует функцию логирования при возникновении ошибки деления на ноль."""
    log_file = tmp_path / "test_output.txt"

    @log(log_file)
    def my_function(x: int, y: int) -> Any:
        """Локальная функция для тестирования. Делит x на y."""
        return x / y

    try:
        my_function(10, 0)
    except ZeroDivisionError:
        pass  # Ожидаем, что будет выброшено исключение, которое логируем

    with open(log_file, "r") as f:
        content = f.read()

        # Проверяем, что контент совпадает с тем, что мы ожидаем
    expected_content = "my_function error: division by zero. Inputs: (10, 0), {}\n"
    assert content == expected_content

    # Замените «{}» на 'None' или любой другой формат, подходящий для ваших нужд
#    assert content == f"my_function error: division by zero. Inputs: (10, 0), None"

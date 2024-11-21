from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Функция-декоратор логирует начало и конец работы функции, результаты и ошибки"""
    def decorator(my_func: Callable) -> Callable:
        @wraps(my_func)
        def wrapper(*args: int, **kwargs: str) -> Any:
            if not filename:
                print(f"{my_func.__name__} started")
                try:
                    result = my_func(*args, **kwargs)
                    print(f"{my_func.__name__} ok")
                    print(f"{my_func.__name__} finished")
                    return result
                except Exception as e:
                    print(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            else:
                try:
                    result = my_func(*args, **kwargs)
                    with open(filename, "a") as file:  # Используем режим "a"
                        file.write(f"{my_func.__name__} ok\n")
                    return result
                except Exception as e:
                    with open(filename, "a") as file:  # Используем режим "a"
                        file.write(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                    raise  # Возможно, выйдем с ошибкой

        return wrapper

    return decorator

from functools import wraps
from time import ctime
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор логирования с необязательным параметром,
    соответствующим имени файла, содержащего информацию о вызове переданной функции"""

    def decorator(func: Callable) -> Callable:
        """Вложенный декоратор, принимающий декорируемую функцию в качестве аргумента"""

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """Вложенный декоратор-обертка, возвращающий результат логируемой функции и информацию о ее вызове"""
            start_time = ctime()
            try:
                result = func(*args, **kwargs)
                end_time = ctime()
                log_info_part_1 = f"Вызываемая функция: {func.__name__}\nВремя вызова: {start_time}\n"
                log_info_part_2 = f"Результат: {result}\nВремя завершения вызова: {end_time}\n\n"
                log_info = log_info_part_1 + log_info_part_2
                return result
            except Exception as some_ex:
                log_info_part_1 = f"Вызываемая функция: {func.__name__}\nВремя вызова: {start_time}\n"
                log_info_part_2 = "Результат: Работа преждевременно завершена с ошибкой: "
                log_info_part_3 = f'{type(some_ex).__name__} "{str(some_ex)}"\n'
                log_info_part_4 = f"При входных параметрах:\nПозиционных: {args}\nИменованных: {kwargs}\n\n"
                log_info = log_info_part_1 + log_info_part_2 + log_info_part_3 + log_info_part_4
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_info)
                else:
                    print(log_info)

        return wrapper

    return decorator

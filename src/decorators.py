from functools import wraps
from time import ctime
from typing import Callable, Any


def log(filename: str =None) -> Callable:
    '''Декоратор логирования с необязательным параметром, соответствующим имени файла, содержащего информацию о вызове переданной функции'''
    def decorator(func: Callable) -> Callable:
        '''Вложенный декоратор, принимающий декорируемую функцию в качестве аргумента'''
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            '''Вложенный декоратор-обертка, возвращающий результат логируемой функции и информацию о ее вызове'''
            start_time = ctime()
            try:
                result = func(*args, **kwargs)
                end_time = ctime()
                log_info = f'Вызываемая функция: {func.__name__}\nВремя вызова: {start_time}\nРезультат: {result}\nВремя завершения вызова: {end_time}\n\n'
                return result
            except Exception as some_ex:
                log_info = f'Вызываемая функция: {func.__name__}\nВремя вызова: {start_time}\nРезультат: Работа преждевременно завершена с ошибкой: {type(some_ex).__name__} "{str(some_ex)}"\nПри входных параметрах:\nПозиционных: {args}\nИменованных: {kwargs}\n\n'
            finally:
                if filename:
                    with open(filename, 'a', encoding="utf-8") as file:
                        file.write(log_info)
                else:
                    print(log_info)
        return wrapper
    return decorator

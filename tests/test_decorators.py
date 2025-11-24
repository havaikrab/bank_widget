from src import decorators
from time import ctime



def test_log_correct_call():
    @decorators.log()
    def add_string(a, b):
        return str(a) + ' - ' + str(b) + '!'
    result = add_string('Декоратор', 'Функция')
    assert result == 'Декоратор - Функция!'


def test_log_incorrect_call():
    @decorators.log()
    def zero_division(x):
        return x / 0
    result = zero_division(5)
    assert result is None


def test_log_console_message(capsys):
    @decorators.log()
    def hello_world():
        return "Hello World!"
    result = hello_world()
    captured = capsys.readouterr()
    assert captured.out == f'Вызываемая функция: hello_world\nВремя вызова: {ctime()}\nРезультат: Hello World!\nВремя завершения вызова: {ctime()}\n\n\n'


def test_log_file_message():
    @decorators.log('log_file.txt')
    def add_numbers(i, j):
        return i + j
    add_result = add_numbers(5, 10)
    with open('log_file.txt', 'r', encoding="utf-8") as file:
        file_message = ' '.join([i for i in file.read().strip().split('\n')][-4:])
    assert file_message == f'Вызываемая функция: add_numbers Время вызова: {ctime()} Результат: 15 Время завершения вызова: {ctime()}'
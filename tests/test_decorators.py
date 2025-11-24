from time import ctime

from src import decorators


def test_log_correct_call():
    @decorators.log()
    def add_string(a, b):
        return str(a) + " - " + str(b) + "!"

    result = add_string("Декоратор", "Функция")
    assert result == "Декоратор - Функция!"


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

    hello_world()
    captured = capsys.readouterr()
    log_info_part_1 = f"Вызываемая функция: hello_world\nВремя вызова: {ctime()}\nРезультат: Hello World!\n"
    log_info_part_2 = f"Время завершения вызова: {ctime()}\n\n\n"
    log_info = log_info_part_1 + log_info_part_2
    assert captured.out == log_info


def test_log_file_message():
    @decorators.log("log_file.txt")
    def add_numbers(i, j):
        return i + j

    add_numbers(5, 10)
    with open("log_file.txt", "r", encoding="utf-8") as file:
        file_message = " ".join([i for i in file.read().strip().split("\n")][-4:])
    assert (
        file_message
        == f"Вызываемая функция: add_numbers Время вызова: {ctime()} Результат: 15 Время завершения вызова: {ctime()}"
    )

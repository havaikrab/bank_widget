import logging
import os


masks_logger = logging.getLogger("masks_logger")
os.makedirs("logs/", exist_ok=True)
file_handler = logging.FileHandler("logs/masks_logs.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску намера карты"""

    masks_logger.info("Вызвана функция get_mask_card_number")
    if not isinstance(card_number, str):
        masks_logger.error("Функции передан некорректный тип данных, работа завершена с ошибкой")
        raise TypeError("Некорректный номер карты")
    for i in card_number:
        if not i.isdigit():
            masks_logger.error("Функции передан некорректный тип данных, работа завершена с ошибкой")
            raise TypeError("Некорректный номер карты")

    if 12 < len(card_number) < 20:
        first_slice = list(card_number)[:6]
        first_slice.insert(4, " ")
        first_str = "".join(first_slice)
        end_str = card_number[-4:]
        masked_card_number = first_str + "** **** " + end_str
        masks_logger.info("Маска номера карты успешно получена")
        return masked_card_number
    else:
        masks_logger.error("Функции передан аргумент с недопустимым значением, работа завершена с ошибкой")
        raise ValueError("Некорректный номер карты")


def get_mask_account(account: str) -> str:
    """Возвращает маску намера счета"""

    masks_logger.info("Вызвана функция get_mask_account")
    if not isinstance(account, str):
        masks_logger.error("Функции передан некорректный тип данных, работа завершена с ошибкой")
        raise TypeError("Некорректный номер счета")
    for i in account:
        if not i.isdigit():
            masks_logger.error("Функции передан некорректный тип данных, работа завершена с ошибкой")
            raise TypeError("Некорректный номер счета")

    if 14 < len(account) < 35:
        end_str = account[-4:]
        masked_account = "**" + end_str
        masks_logger.info("Маска номера счета успешно получена")
        return masked_account
    else:
        masks_logger.error("Функции передан аргумент с недопустимым значением, работа завершена с ошибкой")
        raise ValueError("Некорректный номер счета")

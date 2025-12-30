import pytest

from src import searchers


@pytest.mark.parametrize(
    "transactions_descriptions_list, text, expected_list",
    [
        (
            [
                {"id": 176798279, "description": "Открытие вклада"},
                {
                    "id": 414894334,
                    "description": "Перевод со счета на счет",
                },
                {},
                {
                    "id": "INVALID KEY DESCRIPTION",
                    "beSCRiption": "Перевод с карты на карту",
                },
                {"id": 200634844, "description": "Перевод организации"},
                {"id": 710136990, "description": "Перевод организации"},
            ],
            "Account CARD СЧЕТ счёт ПеРеВоД",
            [
                {
                    "id": 414894334,
                    "description": "Перевод со счета на счет",
                },
                {"id": 200634844, "description": "Перевод организации"},
                {"id": 710136990, "description": "Перевод организации"},
            ],
        ),
        (
            [
                {"id": 86608620, "description": "Перевод с карты на карту"},
                {
                    "id": 185048835,
                    "description": "ПерИвоТ организации",
                },
                {"id": 4574785445, "description": "FROM CARD TO CARD"},
                {
                    "id": 1234567,
                    "description": "Списание с карты на счет",
                },
                {"id": 200634844, "description": "Открытие карты"},
                {"id": 710136990, "description": "Снятие наличных"},
            ],
            "Account card карт счёт ПеРеВоД",
            [
                {"id": 86608620, "description": "Перевод с карты на карту"},
                {"id": 4574785445, "description": "FROM CARD TO CARD"},
                {
                    "id": 1234567,
                    "description": "Списание с карты на счет",
                },
                {"id": 200634844, "description": "Открытие карты"},
            ],
        ),
    ],
)
def test_find_description(transactions_descriptions_list, text, expected_list):
    assert searchers.find_description(transactions_descriptions_list, text) == expected_list


@pytest.mark.parametrize(
    "transactions_list, required_descriptions, expected_dict",
    [
        (
            [
                {"id": 176798279, "description": "Открытие вклада"},
                {"id": 414894334, "description": "Перевод со счета на счет"},
                {},
                {
                    "id": "INVALID KEY DESCRIPTION",
                    "beSCRiption": "Перевод с карты на карту",
                },
                {"id": 200634844, "description": "Перевод организации"},
                {"id": 710136990, "description": "Перевод организации"},
            ],
            ["Перевод организации", "Открытие вклада"],
            {"Открытие вклада": 1, "Перевод организации": 2},
        ),
        (
            [
                {"id": 86608620, "description": "Перевод с карты на карту"},
                {
                    "id": 185048835,
                    "description": "ПерИвоТ организации",
                },
                {"id": 4574785445, "description": "FROM CARD TO CARD"},
                {
                    "id": 1234567,
                    "description": "Списание с карты на счет",
                },
                {"id": 200634844, "description": "Открытие карты"},
                {"id": 710136990, "description": "Снятие наличных"},
            ],
            ["ПерИвоТ организации", "Снятие наличных"],
            {"ПерИвоТ организации": 1, "Снятие наличных": 1},
        ),
        ({}, ["Перевод"], {}),
    ],
)
def test_aggregate_by_description(transactions_list, required_descriptions, expected_dict):
    assert searchers.aggregate_by_description(transactions_list, required_descriptions) == expected_dict

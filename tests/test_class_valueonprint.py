from utils import class_valueonprint


def test__formatted_card_number():
    list_ = [{
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }]
    f = class_valueonprint.ValueOnPrint(list_).formatted_card_number("Maestro 1308795367077170")
    assert f == 'Maestro  1308 79*******************7170'


def test__formatted_time():
    list_ = [{
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }]
    f = class_valueonprint.ValueOnPrint(list_).formatted_time("2019-07-13T18:51:29.313309")
    assert f == '13.07.2019'


def test__formatted_score_number():
    list_ = [{
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }]
    f = class_valueonprint.ValueOnPrint(list_).formatted_score_number("Счет 96527012349577388612")
    assert f == 'Счет  **8612'

def test__view_on_print():
    list_ = [{
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }]
    f = class_valueonprint.ValueOnPrint(list_)
    assert f.view_on_print(0) == '\n        13.07.2019 Перевод с карты на счет\n        Maestro  1308 79*******************7170->Счет  **8612\n        97853.86 руб.\n        '
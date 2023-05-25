from src.utils import load_jsonfile, removing_empty, get_five_operations


def test_load_jsonfile():
    assert load_jsonfile('test_operation.json') == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}, {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {}]


def test_removing():
    json_file = load_jsonfile('test_operation.json')
    assert removing_empty(json_file) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                                          'operationAmount': {'amount': '41096.24',
                                                              'currency': {'name': 'USD', 'code': 'USD'}},
                                          'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
                                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
                                          'operationAmount': {'amount': '67314.70',
                                                              'currency': {'name': 'руб.', 'code': 'RUB'}},
                                          'description': 'Перевод организации',
                                          'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'},
                                         {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                                          'operationAmount': {'amount': '31957.58',
                                                              'currency': {'name': 'руб.', 'code': 'RUB'}},
                                          'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                                          'to': 'Счет 64686473678894779589'}]


def test_get_operations():
    assert get_five_operations('test_operation.json') == ("08.12.2019 Открытие вклада\n"
                                              "Счет **5907\n"
                                              "41096.24 USD\n"
                                              "\n"
                                              "26.08.2019 Перевод организации\n"
                                              "Maestro 159683** **** 837868705199 -> Счет **9589\n"
                                              "31957.58 руб.")

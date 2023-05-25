import json

from datetime import datetime


def load_jsonfile(filename):
    """Считываем из файла данные и
    переводим на язык python"""
    with open(filename, encoding='utf8') as file:
        return json.loads(file.read())


def removing_empty(filename):
    """Удаляем пустые словари
    """
    new_list = []
    for item in filename:
        if bool(item) is False:
            continue
        else:
            new_list.append(item)
    return new_list


def get_five_operations(operations):
    """Вывод последних 5-ти операций
    клиентом"""
    operations = load_jsonfile(operations)
    operations = removing_empty(operations)
    date_list = []
    for date in operations:
        if 'date' in date:
            date_list.append(date["date"])
    date_list = sorted(date_list[0:5])
    five_operations = []
    for index in operations:
        if "EXECUTED" in index['state']:
            for date in date_list:
                if date in index["date"]:
                    date_str = index['date'].split("T")[0]
                    date_time = datetime.strptime(date_str, '%Y-%m-%d').date().strftime('%d.%m.%Y')
                    description_ = index["description"]
                    amount_ = index['operationAmount']["amount"]
                    money = index["operationAmount"]["currency"]["name"]
                    if "Открытие вклада" in description_:
                        check = index['to'][0:5] + '**' + index['to'][-4:]
                        five_operations.append(f"{date_time} {description_}\n{check}\n{amount_} {money}")
                    else:
                        card = index['from'][:-10] + '** **** ' + index['from'][12:]
                        check = index['to'][0:5] + '**' + index['to'][-4:]
                        five_operations.append(f"{date_time} {description_}\n{card} -> {check}\n{amount_} {money}")
    return '\n\n'.join(five_operations)

import json


# import datetime

def load_jsonfile(filename):
    """Считываем из файла данные и
    переводим на язык python"""
    with open(filename, encoding='utf8') as file:
        return json.loads(file.read())


def removing_empty(filename):
    new_list = []
    for item in filename:
        if bool(item) is False:
            del item
        else:
            new_list.append(item)
    return new_list



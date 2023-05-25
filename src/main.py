from src.utils import get_five_operations, removing_empty, load_jsonfile

operation = load_jsonfile('operations.json')
# print(operation)
operation = removing_empty(operation)
# print(operation)
print(get_five_operations('operations.json'))



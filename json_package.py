import json

input_list = [{'key1': 1},{'key2':2}]
print(json.dumps(input_list))

input_list1 = '{"key1":1, "key2":2, "key3":3}'

input_load = json.loads(input_list1)
print(input_load)
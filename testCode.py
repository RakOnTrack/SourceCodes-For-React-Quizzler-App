import json

data = {
    "results": [

        {'key1': 'value1'},
        {'key2': 'value2'},
        {'key3': 'value3'}
    ]
}

with open('output.json', 'w') as file:
    json.dump(data, file, indent=2, separators=(',', ': '))

import json

def get_list():
    file_p = 'operations.json'
    with open (file_p) as file:
        data = json.load(file)
    return data






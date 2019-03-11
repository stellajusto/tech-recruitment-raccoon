import json
import os

def quantity_correction():
    with open('broken-database.json', 'r+') as json_data:
        data = json.load(json_data)

        for item in data:
            # If the key 'quantity' does not exist, create it and assign zero to it
            if 'quantity' not in item:
                item['quantity'] = 0

    os.remove('broken-database.json')
    with open('repaired-database.json', 'w') as json_data:
        json.dump(data, json_data, indent=4, sort_keys=False, ensure_ascii=False)

    json_data.close()

if __name__ == '__main__':
    quantity_correction()

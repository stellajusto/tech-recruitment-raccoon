import json
import os

from locale import atof

def price_correction():
    with open('broken-database.json','r+') as json_data:
        data = json.load(json_data)

        for item in data:
            # Convert string to float
            if isinstance(item['price'], str):
                item['price'] = atof((item['price']))

            # Convert int to float to make prices standardized
            elif isinstance(item['price'], int):
                item['price'] = float(item['price'])

    os.remove('broken-database.json')
    with open('broken-database.json','w') as json_data:
        json.dump(data, json_data, indent=4, sort_keys=False, ensure_ascii=False)

    json_data.close()

if __name__ == '__main__':
    price_correction()

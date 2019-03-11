import json
import os

# Function to replace non-ASCII characters that corrupted the database
def replace_non_ascii(x):
    x = x.replace('æ', 'a').replace('¢', 'c').replace('ø', 'o').replace('ß', 'b')
    return x

def name_correction():
    with open('broken-database.json', 'r+') as json_data:
        data = json.load(json_data)

        for item in data:
            # Call the function replace_non_ascii() in each iteration to fix the 'name' of the product
            item['name'] = replace_non_ascii(item['name'])

    os.remove('broken-database.json')
    with open('broken-database.json', 'w') as json_data:
        json.dump(data, json_data, indent=4, sort_keys=False, ensure_ascii=False)

    json_data.close()

if __name__ == '__main__':
    name_correction()

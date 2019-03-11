import json
import operator

def sort_database():
    with open('repaired-database-from-Q1.json', 'r+') as json_data:
        data = json.load(json_data)

    # Sort objects by 'category' using alphabetical order
    # and then sort by 'id' in increasing order among objects of the same category
    data.sort(key = operator.itemgetter('category', 'id'))

    with open('sorted-database.json', 'w') as json_data:
        json.dump(data, json_data, indent=4, sort_keys=False, ensure_ascii=False)

    json_data.close()

if __name__ == '__main__':
    sort_database()

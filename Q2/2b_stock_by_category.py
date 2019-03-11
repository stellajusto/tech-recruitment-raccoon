import json

def stock_price():
    with open('repaired-database-from-Q1.json', 'r+') as json_data:
        data = json.load(json_data)

    # Create a dictionary for categories
    categories = {}

    for item in data:
        # If a category does not exist exist in the dictionary, create it and assign zero as price to it
        if not item['category'] in categories:
            categories[item['category']] = 0

        # Price of all items of a given product
        x = float((item['price'] * item['quantity']))

        # Increase the value of x to the total value of the category
        categories[item['category']] += x

        # Round price to 2 floating points
        categories[item['category']] = round(categories[item['category']], 2)

    # Create an array for stock and adding categories as an object
    stock = [categories]

    with open('stock-by-category.json', 'w') as fp:
        json.dump(stock, fp, indent=4, sort_keys=False, ensure_ascii=False)

    json_data.close()

if __name__ == '__main__':
    stock_price()
# EX10.Show product name that has maximum price
def max_price(products):
    maximum_price=0
    max_name=""
    for i in range(len(products)):
        if maximum_price==0:
            maximum_price=products[0]["price"]
            max_name=products[i]["name"]
        elif maximum_price<products[i]["price"]:
            maximum_price=products[i]["price"]
            max_name=products[i]["name"]
    return max_name
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(max_price(products))
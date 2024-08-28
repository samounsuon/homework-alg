# EX8.Create function to sum total of price 
def sum(array):
    sum=0
    for i in range(len(products)):
        if products[i]["price"]:
            sum+=products[i]["price"]
    return sum
products = [
        {"name": "Apple", "price": 20},
        {"name": "Orange", "price": 24},
    ]
print(sum(products))
# EX9.Create function to find average of price
def average(products):
    average=0
    for i in range(len(products)):
        average+= products[i]["price"]/2
    return average
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(average(products))
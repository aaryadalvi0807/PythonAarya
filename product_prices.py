products = [
    ("Pen", 10),
    ("Bag", 50),
    ("Shoes", 60)
]

USD_TO_INR = 83

result = [
    (name, price * USD_TO_INR)
    for name, price in products
    if price * USD_TO_INR > 3000
]

print(result)

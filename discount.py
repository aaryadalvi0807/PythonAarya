products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]

total_discounted_price = 0

for name, category, price in products:
    if category == "Electronics":
        discounted_price = price * 0.8  # Apply 20% discount
        total_discounted_price += discounted_price

print("Total Discounted Electronics Price:", total_discounted_price)
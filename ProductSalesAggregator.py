sales = [("Pen", 10), ("Pencil", 5), ("Pen", 15)]
total_sales = {}

for product, qty in sales:
    total_sales[product] = total_sales.get(product, 0) + qty

print(total_sales)



# revenue.py
# Total Revenue from Active Customers

customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]

total_revenue = 0

for customer in customers:
    if customer["active"]:
        for purchase in customer["purchases"]:
            if purchase >= 100:
                total_revenue += purchase * 1.10  # Add 10% tax

print("Total Revenue from Active Customers:", total_revenue)
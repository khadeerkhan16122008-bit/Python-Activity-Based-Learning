products = [
    ("P101", 499, 12),
    ("P102", 0, 5),
    ("P103", 1299, 0),
    ("P104", 249.50, 3),
    ("P105", 799, -2)
]

reorder_level = 4
total_value = 0

print("Product Catalogue Report")

for product_id, price, quantity in products:
    if price < 0 or quantity < 0:
        print(product_id, ": Invalid product record")
        continue

    value = price * quantity
    total_value += value

    print("\nProduct ID:", product_id)
    print("Price:", price)
    print("Stock:", quantity)
    print("Inventory Value:", value)

    if quantity <= reorder_level:
        print("Reorder required")

print("\nTotal Valid Inventory Value:", total_value)

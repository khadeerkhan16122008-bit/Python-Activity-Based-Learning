transactions = [
    ("TX101", 450),
    ("TX102", 1200),
    ("TX103", 850),
    ("TX102", 1200),
    ("TX104", 6200),
    ("TX105", 300)
]

seen = []
duplicates = []
threshold = 5000

print("Transaction Details")

for transaction_id, amount in transactions:
    print(transaction_id, "Amount:", amount)

    if transaction_id in seen:
        if transaction_id not in duplicates:
            duplicates.append(transaction_id)
    else:
        seen.append(transaction_id)

    if amount > threshold:
        print("High-value transaction:", transaction_id)

print("\nDuplicate transaction IDs:")
if duplicates:
    for transaction_id in duplicates:
        print(transaction_id)
else:
    print("No duplicates found")

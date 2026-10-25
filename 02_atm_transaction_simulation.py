balance = float(input("Enter opening balance: "))

transactions = [
    ("deposit", 1500),
    ("withdraw", 400),
    ("withdraw", 5000),
    ("deposit", 750),
    ("withdraw", 250)
]

accepted = 0
rejected = 0

for action, amount in transactions:
    if amount <= 0:
        print("Invalid transaction amount")
        rejected += 1
    elif action == "deposit":
        balance += amount
        accepted += 1
        print("Deposited:", amount, "Balance:", balance)
    elif action == "withdraw":
        if amount <= balance:
            balance -= amount
            accepted += 1
            print("Withdrawn:", amount, "Balance:", balance)
        else:
            print("Insufficient balance for:", amount)
            rejected += 1

print("Accepted transactions:", accepted)
print("Rejected transactions:", rejected)
print("Final balance:", balance)

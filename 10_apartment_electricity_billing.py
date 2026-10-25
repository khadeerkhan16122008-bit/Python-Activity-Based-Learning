apartments = [
    ("A-101", 85),
    ("A-102", 145),
    ("A-103", 230),
    ("A-104", 62),
    ("A-105", 190)
]

fixed_charge = 50

def calculate_bill(units):
    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100 * 2 + (units - 100) * 3
    else:
        charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    return charge + fixed_charge

bills = []

print("Apartment Electricity Bills")

for apartment, units in apartments:
    if units < 0:
        print(apartment, ": Invalid units")
        continue

    bill = calculate_bill(units)
    bills.append((apartment, units, bill))

    print("\nApartment:", apartment)
    print("Units Consumed:", units)
    print("Total Bill: Rs.", bill)

bills.sort(key=lambda item: item[1], reverse=True)

print("\nConsumption Ranking")

for rank, (apartment, units, bill) in enumerate(bills, start=1):
    print(rank, apartment, "-", units, "units, Bill: Rs.", bill)

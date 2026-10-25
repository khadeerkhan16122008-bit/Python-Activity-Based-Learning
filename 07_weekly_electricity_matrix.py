appliances = ["Fan", "Light", "Computer"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

usage = [
    [1.2, 1.1, 1.3, 1.2, 1.4, 1.6, 1.5],
    [0.5, 0.5, 0.4, 0.5, 0.6, 0.7, 0.6],
    [2.0, 2.5, 2.2, 2.8, 3.0, 3.5, 3.1]
]

limit = 5.0

print("Weekly Appliance Consumption")

for i in range(len(appliances)):
    total = sum(usage[i])
    print(appliances[i], ":", round(total, 2), "kWh")

print("\nDaily Consumption")

daily_totals = []

for j in range(len(days)):
    total = 0

    for i in range(len(appliances)):
        total += usage[i][j]

    daily_totals.append(total)
    print(days[j], ":", round(total, 2), "kWh")

    if total > limit:
        print("Warning: Consumption exceeds the limit")

highest_day = daily_totals.index(max(daily_totals))

print("\nHighest Consumption Day:", days[highest_day])
print("Consumption:", round(daily_totals[highest_day], 2), "kWh")

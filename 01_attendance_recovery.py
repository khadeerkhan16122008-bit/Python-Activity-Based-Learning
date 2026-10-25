attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
target = float(input("Enter required attendance percentage: "))

if attended < 0 or conducted < 0 or attended > conducted or target < 0 or target > 100:
    print("Invalid input")
elif conducted == 0:
    print("No classes conducted")
else:
    current = attended / conducted * 100
    print("Current attendance:", round(current, 2), "%")

    extra = 0
    while (attended + extra) / (conducted + extra) * 100 < target:
        extra += 1

    print("Additional classes required:", extra)
    print("Final attendance:",
          round((attended + extra) / (conducted + extra) * 100, 2), "%")

subjects = ["Python", "Mathematics", "English"]
scores = []

for subject in subjects:
    marks = []
    for test in range(1, 4):
        mark = float(input(
            "Enter " + subject + " marks for test " + str(test) + ": "
        ))

        while mark < 0 or mark > 100:
            print("Marks must be between 0 and 100")
            mark = float(input("Enter marks again: "))

        marks.append(mark)

    scores.append(marks)

for i in range(len(subjects)):
    average = sum(scores[i]) / 3
    change = scores[i][2] - scores[i][0]

    print("\nSubject:", subjects[i])
    print("Average:", round(average, 2))
    print("Change:", change)

    if change > 0:
        print("Trend: Improved")
    elif change < 0:
        print("Trend: Declined")
    else:
        print("Trend: No change")

    if average < 50:
        print("Status: Weak subject")

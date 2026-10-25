students = ["Asha", "Ravi", "Noor", "Kiran"]
subjects = ["Python", "Maths", "English"]

marks = [
    [88, 76, 91],
    [67, 82, 73],
    [94, 89, 96],
    [55, 61, 58]
]

print("Student Averages")

averages = []

for i in range(len(students)):
    average = sum(marks[i]) / len(marks[i])
    averages.append(average)
    print(students[i], ":", round(average, 2))

print("\nSubject Averages")

for j in range(len(subjects)):
    total = 0

    for i in range(len(students)):
        total += marks[i][j]

    average = total / len(students)
    print(subjects[j], ":", round(average, 2))

top_index = averages.index(max(averages))

print("\nTop Performer:", students[top_index])
print("Highest Average:", round(averages[top_index], 2))

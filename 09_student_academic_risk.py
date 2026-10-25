students = [
    ("Asha", 78, 92, 85),
    ("Ravi", 43, 68, 55),
    ("Noor", 61, 74, 42),
    ("Kiran", 35, 52, 30)
]

print("Student Academic Risk Report")

for name, marks, attendance, lab in students:
    reasons = []

    if marks < 50:
        reasons.append("Low marks")

    if attendance < 75:
        reasons.append("Low attendance")

    if lab < 50:
        reasons.append("Low lab score")

    if len(reasons) >= 2:
        category = "High Risk"
    elif len(reasons) == 1:
        category = "Moderate Risk"
    else:
        category = "Low Risk"

    print("\nStudent:", name)
    print("Risk Category:", category)

    if reasons:
        print("Reasons:", ", ".join(reasons))
    else:
        print("Reasons: None")

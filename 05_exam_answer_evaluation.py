answer_key = ["A", "C", "B", "D", "A"]
answers = []

for i in range(len(answer_key)):
    answer = input(
        "Enter answer for question " + str(i + 1) + ": "
    ).strip().upper()

    while answer not in ["A", "B", "C", "D", ""]:
        print("Enter A, B, C, D, or leave blank")
        answer = input("Enter answer again: ").strip().upper()

    answers.append(answer)

correct = 0
wrong = 0
unanswered = 0

for i in range(len(answer_key)):
    if answers[i] == "":
        unanswered += 1
    elif answers[i] == answer_key[i]:
        correct += 1
    else:
        wrong += 1

score = correct * 2 - wrong * 0.5

print("\nExamination Result")
print("Correct answers:", correct)
print("Wrong answers:", wrong)
print("Unanswered:", unanswered)
print("Final score:", score, "out of", len(answer_key) * 2)

# Python ABL Documentation

This folder contains documentation for the 10 Python Activity-Based Learning case studies.

Each case study will include:

- Problem Statement
- Objectives
- Assumptions
- Algorithm
- Flowchart
- Pseudocode
- Python Source Code
- Test Cases
- Output Screenshots
- Conclusion

## List of Case Studies

1. Attendance Recovery Computation
2. ATM Transaction Sequence Simulation
3. Student Performance Trend Analysis
4. Repeated Transaction Detection
5. String-Based Examination Answer Evaluation
6. Student Marks Matrix Analysis
7. Weekly Electricity Consumption Matrix
8. Tuple-Based Product Catalogue Audit
9. Student Academic Risk Classification
10. Smart Electricity Billing for Multiple Apartments


# Case Study 1: Attendance Recovery Computation

## 1. Problem Statement

To calculate a student's attendance percentage based on the total number of classes and the number of classes attended, and determine whether the attendance requirement is satisfied.

## 2. Objectives

- To calculate the attendance percentage.
- To check whether the student meets the minimum attendance requirement.
- To practise variables, arithmetic operators, and conditional statements in Python.

## 3. Assumptions

1. The total number of classes must be greater than zero.
2. The number of classes attended must not exceed the total number of classes.
3. The minimum required attendance is assumed to be 75%.
4. The inputs are valid numerical values.

## 4. Algorithm

1. Start.
2. Read the total number of classes.
3. Read the number of classes attended.
4. Calculate the attendance percentage by dividing the attended classes by total classes and multiplying by 100.
5. Display the attendance percentage.
6. If the attendance percentage is greater than or equal to 75%, display “Attendance requirement met”.
7. Otherwise, display “Attendance requirement not met”.
8. Stop.

## 5. Flowchart

Draw the flowchart using the following sequence and standard symbols:

```text
             ( START )
                 |
                 v
       / Input total classes,  /
      /    attended classes   /
                 |
                 v
      +------------------------+
      | Calculate attendance % |
      +------------------------+
                 |
                 v
          < Attendance >= 75%? >
              /          \
           Yes            No
            |              |
            v              v
   / Display "Requirement /  / Display "Requirement /
  /         met"            / /       not met"       /
            |              |
            +-------+------+
                    |
                    v
                 ( STOP )
```

**Flowchart symbols:**
- Oval: Start and Stop
- Parallelogram: Input and Output
- Rectangle: Calculation
- Diamond: Decision
- Arrows: Direction of flow

## 6. Pseudocode

```text
START
    INPUT total_classes
    INPUT attended_classes

    attendance = (attended_classes / total_classes) * 100

    DISPLAY attendance

    IF attendance >= 75 THEN
        DISPLAY "Attendance requirement met"
    ELSE
        DISPLAY "Attendance requirement not met"
    END IF
STOP
```

## 7. Python Source Code

Refer to `01_attendance_recovery.py` in the main repository.

## 8. Test Cases

| Total Classes | Attended Classes | Expected Attendance | Result |
|---:|---:|---:|---|
| 100 | 80 | 80% | Requirement met |
| 100 | 70 | 70% | Requirement not met |
| 40 | 30 | 75% | Requirement met |

## 9. Output Screenshot

Insert the screenshot of the program's actual output here. Upload the screenshot to the `Screenshots` folder in the GitHub repository.

## 10. Conclusion

This program demonstrates how Python arithmetic operators and conditional statements can be used to calculate attendance percentage and check whether a student satisfies the attendance requirement.
# Case Study 2: ATM Transaction Sequence Simulation

## 1. Problem Statement

To simulate ATM transactions by processing deposits and withdrawals, updating the account balance, and rejecting invalid transactions or withdrawals that exceed the available balance.

## 2. Objectives

- To understand transaction processing using Python.
- To update an account balance after each transaction.
- To use conditional statements and loops.
- To identify invalid transactions.

## 3. Assumptions

1. The account has an initial balance.
2. Transactions include deposits and withdrawals.
3. Transaction amounts must be positive.
4. A withdrawal cannot exceed the available balance.
5. Transactions are processed in the given sequence.

## 4. Algorithm

1. Start.
2. Initialize the account balance.
3. Read or obtain the transaction sequence.
4. Process each transaction one by one.
5. Check whether the transaction amount is positive.
6. If it is a deposit, add the amount to the balance.
7. If it is a withdrawal, check whether sufficient balance is available.
8. Accept valid transactions and update the balance.
9. Reject invalid transactions or withdrawals with insufficient balance.
10. Display the transaction result and final balance.
11. Stop.

## 5. Flowchart

Draw the flowchart using this sequence:

Start → Initialize balance → Process next transaction → Check transaction amount → Check transaction type → Deposit or check withdrawal balance → Update balance or reject transaction → More transactions? → Yes: repeat processing; No: display final balance → Stop.

Use a diamond for each decision and a rectangle for balance calculations.

## 6. Pseudocode

```text
START
    INITIALIZE balance
    FOR each transaction
        CHECK transaction amount

        IF amount <= 0 THEN
            DISPLAY "Invalid transaction"
        ELSE IF transaction is deposit THEN
            ADD amount to balance
            DISPLAY updated balance
        ELSE IF transaction is withdrawal THEN
            IF amount <= balance THEN
                SUBTRACT amount from balance
                DISPLAY updated balance
            ELSE
                DISPLAY "Insufficient balance"
            END IF
        END IF
    END FOR
    DISPLAY final balance
STOP
```

## 7. Python Source Code

Refer to `02_atm_transaction_simulation.py` in the main repository.

## 8. Test Cases

| Test Case | Input/Condition | Expected Result |
|---|---|---|
| 1 | Valid deposit | Balance increases |
| 2 | Valid withdrawal | Balance decreases |
| 3 | Withdrawal greater than balance | Transaction rejected |
| 4 | Zero or negative amount | Transaction rejected |

## 9. Output Screenshot

Insert the actual output screenshot of the ATM transaction program.

## 10. Conclusion

This program demonstrates how Python loops and conditional statements can simulate ATM transactions, update account balances, and handle invalid operations.

---

# Case Study 3: Student Performance Trend Analysis

## 1. Problem Statement

To analyse students' academic performance by recording marks from multiple tests, calculating averages, and identifying whether performance improves or declines over time.

## 2. Objectives

- To store and analyse students' marks.
- To calculate average marks.
- To compare marks from the first and third tests.
- To identify students who need academic improvement.

## 3. Assumptions

1. Marks are recorded for three tests.
2. Marks are recorded for three subjects.
3. Each mark is between 0 and 100.
4. The average is calculated using the available test marks.
5. An average below 50 is considered weak performance.

## 4. Algorithm

1. Start.
2. Read marks for three subjects across three tests.
3. Validate that each mark is between 0 and 100.
4. Calculate the average marks for each subject.
5. Calculate the student's overall average.
6. Compare the first-test marks with the third-test marks.
7. Identify whether performance improved, declined, or remained unchanged.
8. If the overall average is below 50, identify weak performance.
9. Display the averages and performance trend.
10. Stop.

## 5. Flowchart

Start → Input marks for three subjects and tests → Validate marks → Calculate averages → Compare first and third tests → Classify performance trend → Check whether average is below 50 → Display results → Stop.

If validation fails, follow the error-handling path used in the Python program.

## 6. Pseudocode

```text
START
    INPUT marks for three subjects across three tests
    VALIDATE all marks

    CALCULATE subject averages
    CALCULATE overall average

    COMPARE first-test and third-test marks

    IF third-test performance > first-test performance THEN
        DISPLAY "Performance improved"
    ELSE IF third-test performance < first-test performance THEN
        DISPLAY "Performance declined"
    ELSE
        DISPLAY "Performance unchanged"
    END IF

    IF overall average < 50 THEN
        DISPLAY "Weak performance"
    END IF

    DISPLAY averages and trend
STOP
```

## 7. Python Source Code

Refer to `03_student_performance_trend.py` in the main repository.

## 8. Test Cases

| Test Case | Marks Pattern | Expected Result |
|---|---|---|
| 1 | Third-test marks are higher | Improvement identified |
| 2 | Third-test marks are lower | Decline identified |
| 3 | First and third tests have equal marks | No change identified |
| 4 | Overall average below 50 | Weak performance identified |

## 9. Output Screenshot

Insert the actual output screenshot showing the calculated averages and performance trend.

## 10. Conclusion

This program demonstrates how Python can be used to calculate averages, compare test results, and analyse students' academic performance.

---

# Case Study 4: Repeated Transaction Detection

## 1. Problem Statement

To examine a sequence of financial transactions and identify repeated transaction IDs and transactions involving amounts greater than ₹5,000.

## 2. Objectives

- To identify duplicate transaction IDs.
- To detect transactions above a specified amount.
- To use lists, loops, and conditional statements.
- To improve basic transaction-monitoring logic.

## 3. Assumptions

1. Each transaction has an ID and an amount.
2. Transaction IDs are used to identify repeated transactions.
3. An amount greater than ₹5,000 is flagged for review.
4. A repeated ID is reported as a duplicate.
5. Flagging a transaction does not automatically prove fraud.

## 4. Algorithm

1. Start.
2. Read the transaction IDs and amounts.
3. Create a collection to store previously encountered transaction IDs.
4. Process each transaction.
5. Check whether the transaction ID has already appeared.
6. If it has appeared, flag the transaction as repeated.
7. Otherwise, record the transaction ID.
8. Check whether the amount is greater than ₹5,000.
9. Flag high-value transactions when applicable.
10. Display the flagged transactions.
11. Stop.

## 5. Flowchart

Start → Input transactions → Select next transaction → Check whether ID already exists → Flag duplicate or record new ID → Check whether amount exceeds ₹5,000 → Flag high-value transaction if applicable → More transactions? → Yes: repeat; No: display results → Stop.

## 6. Pseudocode

```text
START
    INPUT transactions
    INITIALIZE seen_IDs

    FOR each transaction
        IF transaction_ID is in seen_IDs THEN
            DISPLAY "Repeated transaction"
        ELSE
            ADD transaction_ID to seen_IDs
        END IF

        IF amount > 5000 THEN
            DISPLAY "High-value transaction"
        END IF
    END FOR

STOP
```

## 7. Python Source Code

Refer to `04_repeated_transaction_detection.py` in the main repository.

## 8. Test Cases

| Test Case | Transaction Condition | Expected Result |
|---|---|---|
| 1 | A new ID with amount below the threshold | No duplicate or high-value flag |
| 2 | An ID that appeared earlier | Duplicate flag |
| 3 | Amount of ₹6,000 | High-value flag |
| 4 | Amount exactly ₹5,000 | No high-value flag under the stated rule |

## 9. Output Screenshot

Insert the actual output screenshot showing detected repeated IDs and high-value transactions.

## 10. Conclusion

This program demonstrates how Python lists and conditional statements can be used to detect repeated transaction IDs and flag high-value transactions for review.

---

# Case Study 5: String-Based Examination Answer Evaluation

## 1. Problem Statement

To evaluate a student's objective examination answers by comparing them with an answer key and calculating the score using the specified marking scheme.

## 2. Objectives

- To compare student answers with correct answers.
- To calculate marks for correct and incorrect answers.
- To handle unanswered questions.
- To practise strings, loops, and conditional statements.

## 3. Assumptions

1. The answer key contains five answers.
2. Each correct answer earns 2 marks.
3. Each incorrect answer loses 0.5 marks.
4. An unanswered question earns zero marks.
5. The answer key is A, C, B, D, A.

## 4. Algorithm

1. Start.
2. Store the correct answer key.
3. Read the student's answers.
4. Initialize the score to zero.
5. Compare each student answer with the corresponding correct answer.
6. Add 2 marks for a correct answer.
7. Subtract 0.5 marks for an incorrect answer.
8. Award zero marks for an unanswered question.
9. Display the total score and evaluation result.
10. Stop.

## 5. Flowchart

Start → Store answer key → Input student answers → Initialize score → Compare each answer → Correct? Add 2; incorrect? Subtract 0.5; unanswered? Add 0 → Process remaining questions → Display score → Stop.

## 6. Pseudocode

```text
START
    SET answer_key = [A, C, B, D, A]
    INPUT student_answers
    SET score = 0

    FOR each question
        IF answer is correct THEN
            score = score + 2
        ELSE IF answer is incorrect THEN
            score = score - 0.5
        ELSE
            score = score + 0
        END IF
    END FOR

    DISPLAY score
STOP
```

## 7. Python Source Code

Refer to `05_exam_answer_evaluation.py` in the main repository.

## 8. Test Cases

| Test Case | Student Answers | Expected Score |
|---|---|---:|
| 1 | A, C, B, D, A | 10 |
| 2 | All five answers incorrect | -2.5 |
| 3 | All five questions unanswered | 0 |
| 4 | Four correct and one incorrect | 7.5 |

## 9. Output Screenshot

Insert the actual output screenshot showing the submitted answers and calculated score.

## 10. Conclusion

This program demonstrates how Python strings, loops, and conditional statements can be used to evaluate objective examination answers and calculate scores.

---

# Case Study 6: Student Marks Matrix Analysis

## 1. Problem Statement

To analyse students' marks in different subjects using a matrix and calculate student averages, subject averages, and the highest-performing student.

## 2. Objectives

- To represent marks using a nested list.
- To calculate each student's average.
- To calculate the average for each subject.
- To identify the student with the highest average.

## 3. Assumptions

1. Marks are arranged in rows and columns.
2. Each row represents one student.
3. Each column represents one subject.
4. Marks are valid numerical values.
5. The highest average is used to identify the top-performing student.

## 4. Algorithm

1. Start.
2. Store student marks in a nested list.
3. Calculate the total marks of each student.
4. Divide each total by the number of subjects to obtain the student average.
5. Calculate the total marks for each subject.
6. Divide each subject total by the number of students to obtain the subject average.
7. Compare student averages.
8. Identify the student with the highest average.
9. Display student averages, subject averages, and the top performer.
10. Stop.

## 5. Flowchart

Start → Store marks matrix → Calculate each student's average → Calculate each subject's average → Compare student averages → Identify top performer → Display results → Stop.

## 6. Pseudocode

```text
START
    INPUT or INITIALIZE marks_matrix

    FOR each student
        CALCULATE total marks
        CALCULATE student average
    END FOR

    FOR each subject
        CALCULATE total marks for subject
        CALCULATE subject average
    END FOR

    FIND student with highest average

    DISPLAY student averages
    DISPLAY subject averages
    DISPLAY top performer
STOP
```

## 7. Python Source Code

Refer to `06_student_marks_matrix.py` in the main repository.

## 8. Test Cases

| Test Case | Condition | Expected Result |
|---|---|---|
| 1 | Different students have different marks | Individual averages are calculated |
| 2 | Subject marks vary among students | Subject averages are calculated |
| 3 | One student has the highest average | That student is identified |
| 4 | Two students have equal highest averages | The program's tie-handling behaviour is displayed |

## 9. Output Screenshot

Insert the actual output screenshot showing student averages, subject averages, and the top performer.

## 10. Conclusion

This program demonstrates how nested lists and loops can be used to organize and analyse student marks efficiently.

---

# Case Study 7: Weekly Electricity Consumption Matrix

## 1. Problem Statement

To analyse electricity consumption for multiple appliances over several days and identify appliances whose daily consumption exceeds 5.0 kWh.

## 2. Objectives

- To store electricity consumption data in a matrix.
- To calculate total consumption for each appliance.
- To compare daily consumption with a specified threshold.
- To identify high-consumption appliances or days.

## 3. Assumptions

1. Electricity consumption is measured in kilowatt-hours (kWh).
2. Data is arranged by appliance and day.
3. Consumption values are non-negative.
4. A daily consumption greater than 5.0 kWh triggers a warning.
5. The threshold is a monitoring rule for this program.

## 4. Algorithm

1. Start.
2. Store electricity consumption data in a nested list.
3. Initialize the total consumption for each appliance.
4. Process each appliance's daily readings.
5. Add daily readings to calculate the appliance's total consumption.
6. Check whether any daily reading exceeds 5.0 kWh.
7. Display a warning when the threshold is exceeded.
8. Display total consumption for each appliance.
9. Stop.

## 5. Flowchart

Start → Input or initialize consumption matrix → Select appliance → Add daily readings → Check each reading against 5.0 kWh → Display warning when exceeded → More appliances? → Yes: repeat; No: display totals → Stop.

## 6. Pseudocode

```text
START
    INPUT or INITIALIZE consumption_matrix

    FOR each appliance
        SET total = 0

        FOR each daily reading
            total = total + reading

            IF reading > 5.0 THEN
                DISPLAY "High consumption warning"
            END IF
        END FOR

        DISPLAY appliance total
    END FOR
STOP
```

## 7. Python Source Code

Refer to `07_weekly_electricity_matrix.py` in the main repository.

## 8. Test Cases

| Test Case | Daily Reading | Expected Result |
|---|---:|---|
| 1 | 3.0 kWh | No warning |
| 2 | 5.0 kWh | No warning under the stated rule |
| 3 | 6.0 kWh | High-consumption warning |
| 4 | Several daily readings | Total consumption is calculated |

## 9. Output Screenshot

Insert the actual output screenshot showing appliance totals and any high-consumption warnings.

## 10. Conclusion

This program demonstrates how nested lists, loops, and conditional statements can be used to analyse electricity consumption and identify readings that exceed a threshold.

---

# Case Study 8: Tuple-Based Product Catalogue Audit

## 1. Problem Statement

To audit a product catalogue stored using tuples by checking product prices and quantities, identifying products that need restocking, and calculating inventory value.

## 2. Objectives

- To store product information using tuples.
- To validate prices and quantities.
- To identify products requiring restocking.
- To calculate the total inventory value.

## 3. Assumptions

1. Each product has a name, price, and quantity.
2. Product prices and quantities cannot be negative.
3. A quantity of 4 or fewer items triggers a restocking alert.
4. Inventory value is calculated as price multiplied by quantity.
5. Product records follow the structure used by the Python program.

## 4. Algorithm

1. Start.
2. Store product records in a tuple-based catalogue.
3. Select each product record.
4. Check whether its price and quantity are valid.
5. Calculate the product's inventory value by multiplying price by quantity.
6. Add the product value to the total inventory value.
7. Check whether the quantity is 4 or fewer.
8. Display a restocking alert when necessary.
9. Display the inventory values and total.
10. Stop.

## 5. Flowchart

Start → Store product catalogue → Select product → Validate price and quantity → Calculate product inventory value → Add to total → Check quantity ≤ 4 → Display restocking alert if required → More products? → Yes: repeat; No: display total inventory value → Stop.

## 6. Pseudocode

```text
START
    INPUT or INITIALIZE product_catalogue
    SET total_inventory_value = 0

    FOR each product
        READ product name, price, quantity

        IF price < 0 OR quantity < 0 THEN
            DISPLAY "Invalid product data"
        ELSE
            product_value = price * quantity
            total_inventory_value =
                total_inventory_value + product_value

            IF quantity <= 4 THEN
                DISPLAY "Restocking required"
            END IF
        END IF
    END FOR

    DISPLAY total_inventory_value
STOP
```

## 7. Python Source Code

Refer to `08_tuple_product_catalogue.py` in the main repository.

## 8. Test Cases

| Test Case | Product Condition | Expected Result |
|---|---|---|
| 1 | Quantity is 10 | No restocking alert |
| 2 | Quantity is 4 | Restocking alert |
| 3 | Quantity is 0 | Restocking alert |
| 4 | Valid price and quantity | Inventory value is calculated |

## 9. Output Screenshot

Insert the actual output screenshot showing product details, restocking alerts, and inventory value.

## 10. Conclusion

This program demonstrates how tuples and loops can be used to organize product information, calculate inventory value, and identify products that require restocking.

---

# Case Study 9: Student Academic Risk Classification

## 1. Problem Statement

To classify students according to academic risk by checking their marks, attendance percentage, and laboratory marks against specified thresholds.

## 2. Objectives

- To evaluate students using multiple criteria.
- To identify students who may need academic support.
- To use conditional statements and logical operators.
- To classify students into different risk levels.

## 3. Assumptions

1. The program checks academic marks, attendance, and laboratory marks.
2. Marks and attendance are expressed on a scale from 0 to 100.
3. Marks below 50 are considered low.
4. Attendance below 75% is considered insufficient.
5. Laboratory marks below 50 are considered low.
6. Two or more risk conditions indicate high risk; one indicates moderate risk.

## 4. Algorithm

1. Start.
2. Read the student's marks, attendance percentage, and laboratory marks.
3. Check whether the marks are below 50.
4. Check whether attendance is below 75%.
5. Check whether laboratory marks are below 50.
6. Count the number of conditions that indicate risk.
7. If two or more conditions are satisfied, classify the student as high risk.
8. If exactly one condition is satisfied, classify the student as moderate risk.
9. Otherwise, classify the student as low risk.
10. Display the classification.
11. Stop.

## 5. Flowchart

Start → Input marks, attendance, and laboratory marks → Check all three risk conditions → Count risk conditions → Is count ≥ 2? → Yes: High Risk → No: Is count = 1? → Yes: Moderate Risk → No: Low Risk → Display classification → Stop.

## 6. Pseudocode

```text
START
    INPUT marks
    INPUT attendance
    INPUT laboratory_marks

    SET risk_count = 0

    IF marks < 50 THEN
        risk_count = risk_count + 1
    END IF

    IF attendance < 75 THEN
        risk_count = risk_count + 1
    END IF

    IF laboratory_marks < 50 THEN
        risk_count = risk_count + 1
    END IF

    IF risk_count >= 2 THEN
        DISPLAY "High Risk"
    ELSE IF risk_count == 1 THEN
        DISPLAY "Moderate Risk"
    ELSE
        DISPLAY "Low Risk"
    END IF
STOP
```

## 7. Python Source Code

Refer to `09_student_academic_risk.py` in the main repository.

## 8. Test Cases

| Test Case | Marks | Attendance | Lab Marks | Expected Risk |
|---|---:|---:|---:|---|
| 1 | 70 | 85% | 75 | Low |
| 2 | 45 | 85% | 70 | Moderate |
| 3 | 40 | 60% | 45 | High |
| 4 | 50 | 75% | 50 | Low |

## 9. Output Screenshot

Insert the actual output screenshot showing the student's inputs and risk classification.

## 10. Conclusion

This program demonstrates how Python conditional statements and logical comparisons can classify students according to academic indicators and identify those who may need additional support.

---

# Case Study 10: Smart Electricity Billing for Multiple Apartments

## 1. Problem Statement

To calculate electricity bills for multiple apartments based on their electricity consumption, a fixed charge, and the specified unit-rate rules, and rank apartments according to their consumption.

## 2. Objectives

- To calculate electricity bills for multiple apartments.
- To apply different unit-rate rules.
- To include a fixed charge in the bill.
- To compare and rank apartments according to electricity consumption.

## 3. Assumptions

1. Each apartment has a recorded electricity consumption in units.
2. The fixed charge is ₹50 per apartment.
3. The unit rate is ₹2 for consumption up to 100 units.
4. The unit rate is ₹3 for consumption from 101 to 200 units.
5. The unit rate is ₹5 for consumption above 200 units.
6. The billing calculation follows the formula implemented in the Python program.
7. Apartments are ranked by their electricity consumption.

## 4. Algorithm

1. Start.
2. Read the number of apartments and their electricity consumption.
3. Select each apartment.
4. Determine the applicable unit-rate category.
5. Calculate the energy charge according to the program's billing rule.
6. Add the fixed charge of ₹50.
7. Display the apartment's consumption and bill amount.
8. Repeat for all apartments.
9. Rank apartments by electricity consumption.
10. Display the ranking and stop.

## 5. Flowchart

Start → Input apartment consumption → Select apartment → Determine unit-rate category → Calculate energy charge → Add ₹50 fixed charge → Display bill → More apartments? → Yes: repeat; No: rank apartments by consumption → Display ranking → Stop.

## 6. Pseudocode

```text
START
    INPUT apartment consumption values

    FOR each apartment
        INPUT or READ units

        IF units <= 100 THEN
            rate = 2
        ELSE IF units <= 200 THEN
            rate = 3
        ELSE
            rate = 5
        END IF

        energy_charge = units * rate
        total_bill = energy_charge + 50

        DISPLAY units
        DISPLAY total_bill
    END FOR

    RANK apartments by units consumed
    DISPLAY ranking
STOP
```

## 7. Python Source Code

Refer to `10_apartment_electricity_billing.py` in the main repository.

## 8. Test Cases

The following examples assume the program multiplies all consumed units by the rate selected for the consumption category.

| Test Case | Units | Energy Charge | Fixed Charge | Total Bill |
|---|---:|---:|---:|---:|
| 1 | 80 | ₹160 | ₹50 | ₹210 |
| 2 | 150 | ₹450 | ₹50 | ₹500 |
| 3 | 250 | ₹1,250 | ₹50 | ₹1,300 |

## 9. Output Screenshot

Insert the actual output screenshot showing apartment consumption, calculated bills, and the consumption ranking.

## 10. Conclusion

This program demonstrates how Python conditional statements, loops, and arithmetic operators can calculate electricity bills for multiple apartments and rank them according to their electricity consumption.

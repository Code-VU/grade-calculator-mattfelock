def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    score = float(input("Enter score: "))
    if score >= 0.9 and score <= 1 and score >= 0:
        print("A")
    elif score >= 0.8 and score <= 1 and score >= 0:
        print("B")
    elif score >= 0.7 and score <= 1 and score >= 0:
        print("C")
    elif score >= 0.6 and score <= 1 and score >= 0:
        print("D")
    elif score < 0.6 and score <= 1 and score >= 0:
        print("F")
    elif score > 1.0 or score < 0.0:
        print("score out of range")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()
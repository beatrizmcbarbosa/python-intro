score = int(input("Score: "))

if score > 100 or score < 0:
    print ("Score is not valid")
elif score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >=70:
    print("Grade C")
elif score >=60:
    print("Grade D")
else:
    print("Grade F")
    
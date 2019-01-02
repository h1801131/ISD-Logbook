letterGrade = int(input("Enter the letter Grade:"))
if letterGrade >= 90:
    letterGrade = "A"
elif letterGrade >= 80:
    letterGrade = "B"
elif letterGrade >= 70:
    letterGrade = "C"
elif letterGrade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"
print("Your grade is: ",letterGrade)

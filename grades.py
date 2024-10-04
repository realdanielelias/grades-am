#Take both test grades
grade1 = float(input("Type the first grade: "))
grade2 = float(input("Type the second grade: "))

#Calculate the arithmetic mean
mean = (grade1+grade2)/2

#If the student mean is equal or higher than 7, the student was approved
if mean >=7:
    print("Passed")

#If not, the student was reproved
else:
    print("Failed")
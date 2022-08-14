firdtName = input("Please Enter Name:")
lastName = input("Please Enter LastName:")
courseGradeOne = float(input("Please Enter course Grade One:"))
courseGradeTwo = float(input("Please Enter course Grade Second:"))
courseGradeThird = float(input("Please Enter course Grade Third:"))

if courseGradeOne >= 0 and courseGradeOne <= 20 and courseGradeTwo >= 0 and courseGradeTwo <= 20 and courseGradeThird >= 0 and courseGradeThird <= 20:

    average = float((courseGradeOne + courseGradeTwo + courseGradeThird) / 3)

    if average >= 17:
        print("Great")

    if average <= 12 and average < 17:
        print("Normal")

    if average < 12:
        print("Fail")

else:
    print("Please Enter The Correct Value")
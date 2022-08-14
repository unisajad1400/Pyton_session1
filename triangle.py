sideOne = int(input("Please Enter The First Side:"))
sideTwo = int(input("Please Enter The Second Side:"))
sideThird = int(input("Please Enter The Third Side:"))

if int(sideTwo + sideThird) > sideOne or int(sideOne + sideThird) > sideTwo or int(sideOne + sideTwo) > sideThird:
    print("This Is A Triangle")

else:
    print("This Is Not A Triangle")    
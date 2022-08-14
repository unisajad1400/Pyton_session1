from pickletools import float8


weight = float(input)
height = float(input)

if weight <= 120 and weight >= 40 and height <= 2 and height >= 1.40:
    result = float(weight / height ** 2)

    if result < 18.5:
        print("UNDER WEIGHT")

    if result >= 18.5 and result <= 24.9:
        print("NORMAL")

    if result >= 25 and result <= 29.9:
        print("OVER WEIGHT")

    if result >= 30 and result <= 34.9:
        print("OBESE")

    if result >= 35:
        print("EXTREMELY OBESE")
else:

    print("Please Enter The Correct Value")

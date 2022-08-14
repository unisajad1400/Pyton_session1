from ast import And
import math
from xml.etree.ElementInclude import include
import math

numOne = int(input())

op = input("Please Insert Operator:")

if op == "+" or op == "-" or op == "*" or op == "/" or op == "fac" or op == "sqrt" or op == "sin" or op == "cos" or op == "tan" or op == "cot":

    if op == "+" or op == "-" or op == "*" or op == "/":
        numTwo = int(input("Please Insert NumberTwo:"))

        if op == "+":
            result = numOne + numTwo

        if op == "-" and numOne >= numTwo:
            result = numOne - numTwo

        if op == "*":
            result = numOne * numTwo
    
        if op == "/" and numOne > numTwo and numTwo != 0:
            result = numOne / numTwo

    else:
        if op == "fac" and numOne > 1:
            result = int(math.factorial(numOne))

        if op == "sqrt" and numOne > 0:
            result = float(math.sqrt(numOne))

        if op == "sin":
            result = float(math.sin(numOne * 180))

        if op == "cos":
            result = float(math.cos(numOne * 180))

        if op == "tan":
            result = float(math.tan(numOne * 180))

        if op == "cot":
            result = 1 / float((math.tan(numOne * 180)))

    print(result)

else: 
    print("Sorry! The operator entered is not valid")


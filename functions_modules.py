#Functions & Modules
# import math
# print(math.pi)

# from math import pi
# print(pi)

from math import *
# Task 1

def factorialCal(number):
    if (number < 2):
        return "1. Factorial of "+str(number) + " is : 1"

    finalNumber = 1
    for i in range(1,number+1):
        finalNumber = i * finalNumber
    
    return "1. Factorial of "+str(number) + " is : "+ str(finalNumber)
        
numberInput = input("Provide me a number :")
finalNumberData = factorialCal(int(numberInput))
print(finalNumberData)

#Task 1 Second Approch according to video
def factorialCalculation(n):
    if(n < 2):
       return "2. Factorial of "+str(n) + " is : 1"
    else:
        calculatValue = n * (factorial(n - 1))
        return "2. Factorial of "+str(n) + " is : "+ str(calculatValue)


resultData  = factorialCalculation(int(numberInput))
print(resultData)
     




# Task 2
numberData = input("Provide me a number : ")

def useMathMethod(nData):
    squareRoot = sqrt(nData)
    logarithm = log(nData)
    sine = sin(nData)
    print("Square Root : " + str(squareRoot) + " \nLogarithm : " + str(logarithm) + " \nSine : " + str(sine) )
    # print(logarithm)
    # print(sine)


useMathMethod(int(numberData))

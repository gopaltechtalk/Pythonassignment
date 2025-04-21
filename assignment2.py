#Task 1

number = input("Provide me a number :")
print(number)
string = "This is odd number"
if(int(number) % 2 == 0):
    string = "This is even number"


print(string)





#Task 2
sumValue = 0
finalResult = 0
for i in range(1,50):
    sumValue = i+sumValue
    if sumValue == 1225:
        finalResult = sumValue
        break
    

if finalResult is not None:
    print(finalResult)
    
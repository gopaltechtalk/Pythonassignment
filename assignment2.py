sumValue = 0
finalResult = 0
for i in range(1,50):
    sumValue = i+sumValue
    if sumValue == 1225:
        finalResult = sumValue
        break
    

if finalResult is not None:
    print(finalResult)
    
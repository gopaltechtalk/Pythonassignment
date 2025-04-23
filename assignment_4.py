# Task 1

try:
    importFile = open("sample.txt","r") #This line imports the file
    readFileContent = importFile.read()
    print(readFileContent)

    importFile.close()
except:
    print("The File'Sample.txt' was not found.")
finally:
    print("Continue with the following code")

#Task 1 Second Approch

try:
    with open("sample2.txt","r") as addFile:
        getFileData = addFile.read()
        print(getFileData)
except:
    print("Error: The file 'sample.txt' was not found") 
finally:
    print("Continue with the following code")


# Task 2
appendData = input("Enter text to write into the file : ")
importOutputFile = open("output.txt","a")
importOutputFile.write(appendData + "\n")
print("Data Successfully appended.")
importOutputFile.close()

try:
    with open("output.txt","r") as fileImport:
        getData = fileImport.read()
        print(getData)
except:
    print("Error: The file 'output.txt' was not found")
finally:
    print("Continue with the following code")
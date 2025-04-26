# # Task 1
# stuData = {"Gopal":'90',"Divya":'99',"Bharat":'100',"Vikarm":'98',"Namrta":'97',"Pooja":'35'}
# print(stuData)
# try:
#     Name = input("Enter the student's Name : ")
#     print(Name + "'s marks : "  + stuData[Name])
# except:
#     print("Student not found")

# # Task 1 Approch 2 Here is drowback is that I can not add more then one key:value into distionaries 
# stuData_2 = {"Gopal":'90',"Divya":'99',"Bharat":'100',"Vikarm":'98',"Namrta":'97',"Pooja":'35'}
# try:
#     sName = input("Enter the student's Name : ")
#     # print(stuData_2)
#     findData = sName in stuData_2
#     if(findData):
#         print(sName + "'s marks : "  + stuData_2[sName])
#     else:
#         print("Student not found")
# except:
#     print("Something went wrong !!!")



# Task 1 Approch 3 Here is drowback is that I can not add more then one key:value into distionaries 
# stuData = {}
# studentName = input("Provide the Student Name which you want to add into Dictionari : ")
# stuMark = input("Provide Exam marks for student : ")
# stuData[studentName] = stuMark
# print(stuData)
# findStudent = input('Enter Student Name which you find into distionari :')
# try:
#     print(studentName + "'s marks : "  + stuData[studentName])
# except:
#     print("Student not found")


# Task 2 
listData = [1,2,3,4,5,6,7,8,9,10]
print("Original list :",listData) 
sliceListData = listData[0:5]


# The reason you see None is because the .reverse() method reverses the list in place and does not return a new list, it returns None. To fix it, just call sliceListData.reverse() first and then print sliceListData, or use slicing like sliceListData[::-1] to get a reversed copy.

print("Extracted first five elements : ",sliceListData )
# reverseSliceListData = sliceListData.reverse()
# After help TuteDude Thanks !!!
reverseSliceListData = sliceListData[::-1]

print("Reversed Extracted elements : ", reverseSliceListData)  

# I am not getting why None is coming as when we print sliceListData it shows [1,2,3,4,5]. Please help

class Student:
    colName="ABCD" #static variable
s1=Student() #object creation
s2=Student()
print(s1.colName) #accessing static variable using object name
print(Student.colName)#accessing static variable using class name

Student.colName="PQRS" #modify static variable using classname

print(s1.colName) 
print(Student.colName)

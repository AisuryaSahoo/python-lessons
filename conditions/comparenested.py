#compare 3 numbers
x=float(input("Enter 1st no"))
y=float(input("Enter 2nd no"))
z=float(input("Enter 3rd no"))
if(x>y):
    if(x>z):
        print(x,"is greatest no")
    else:
        print(z,"is greatest no")
else:
    if(y>z):
        print(y,"is greatest no")
    else:
        print(z,"is greatest no")

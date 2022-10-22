class Student:
    clgName="ABCD"
    def show(self):   #instance method   receives object
        print(self.clgName)
        print(self.name)
        print(self.roll)

    @classmethod  #decorator
    def showClassVar(cls):   #receives classname
        cls.clgName="PQRS"
        print(cls.clgName)

    @staticmethod  #receives neither class nor object (utility method)
    def evenodd(num):
        if(num%2==0):
            print("even")
        else:
            print("odd")
    
    
s1=Student()
s1.name="Shashi" #instace variable
s1.roll=10
s1.show()
s1.showClassVar()
x=int(input("Enter a number"))
s1.evenodd(x)
s1.evenodd(int(input("Enter a number")))


"""
s2=Student()
s2.name="Rabi" #instace variable
s2.roll=12
s2.show()
"""

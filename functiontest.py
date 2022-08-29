#no return no argument/parameter
"""
def display():
    print("hello world")
display()


"""

#keyword -- def
#function identifier --display

#with return no arguments
"""
def display():
    print("From display function definition, returning value 5")
    return 5
a=display()
print("In main received value",a)

"""
# no return with arguments
"""
def display(a):
    print("In display func definition recevied value", a,"from main")
print("from main sending value 5 to display")
display(5) # 5 will be sent to display definition
"""
#with return with arguments

def display(a): #a will get value 5
    print("In display function ,received value",a,"from main")
    print("From display returning value 10")
    return 10
print("From main sending value 5 to display")
b=display(5) # b will receive value 10
print("In main received value",b,"from display")


    











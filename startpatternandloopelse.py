
"""
i=1
while(i<=5): #
    j=1
    while(j<=i):#
        j+=1#
        print('*',end=" ")
    print()
    i+=1
"""

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
"""
i=1
while(i<=5): #
    j=1
    while(j<=i):#
        print(j,end=" ")
        j+=1#
    print()
    i+=1
"""
"""

    *
   **
  ***
 ****
*****
"""
"""
i=1
while(i<=5):
    space=1
    star=1
    while(space<=(5-i)): #space
        print(" ",end=" ")
        space+=1
    while(star<=i): #start
        print('*',end=" ")
        star+=1
    print()
    i+=1
"""
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""


"""
loop else is executed when the loop is terminated normally without any break
normal termination for for loop->if all the iterations are completed without break
normal termination for while loop -> when condition fails

"""

"""
for i in range(10):
    print(i)
    if(i==5):
        break #for will terminate here abnormally ,hence else won't be executed
else:
    print("for - else executed")
    
print("end of program")
"""
i=1
while(i<=10):
    print(i)
    if(i==11):
        break
    i+=1
else:
    print("while - else executed")
print("end")
    














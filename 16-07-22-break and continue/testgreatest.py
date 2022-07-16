while(True):
    x=int(input("enter 1st no"))
    y=int(input("enter 2nd no"))
    z=int(input("enter 3rd no"))
    if(x==y or x==z or y==z):
        print("Sorry, equl numbers provided")
        print("Please provide different numbers")
        #continue
    else:
        if(x>y):
            if(x>z):
                print(x," is greatest")
            else:
                print(z," is greatest")
        elif(y>z):
            print(y," is greatest")
        else:
            print(z," is greatest")
        print("Successful execution ...exiting from program")
        break;
    
            

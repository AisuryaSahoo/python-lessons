while(True):
    num=int(input("enter a number"))
    if(num==0):
        print("Enter a non zero positive no")
    else:
        temp=num
        sum=0
        count=0
        temp2=num
        #following loop will count number of digits in number
        while(temp!=0):
            count+=1
            temp=temp//10
        print("number of digits in",num," = ",count)
        while(temp2!=0):
            rem=temp2%10
            sum=sum+rem**count
            temp2//=10
            #temp2=temp2//10
        if(num==sum):
            print(num, " is an armstrong no")
        else:
            print(num, " is not an armstrong no")
        break


        

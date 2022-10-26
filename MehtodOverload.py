class MethodOverloadTest:

    def show(self,x=None,y=None):
        if(x==None and y ==None):
            print("show -1")
        elif(x==None or y ==None):
            print("show - 2")
        else:
            print("show - 3")
m = MethodOverloadTest()
m.show()
m.show(10)
m.show(10,20)

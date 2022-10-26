class MethodOverloadTest:
    def show(self):
        print("show - 1")
    def show(self,x):
        print("show - 2")
    def show(self,x,y):
        print("show - 3")
m = MethodOverloadTest()
#m.show()
#m.show(10)
m.show(10,20)

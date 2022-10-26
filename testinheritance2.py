class Bank:
    name = "SBI"
    def showBankInfo(self):
        print(self.name)
class Dept(Bank):
    def __init__(self,name,staff):
        self.dname=name
        self.noOfStaff = staff
    def showDeptInfo(self):
        print(self.dname)
        print(self.noOfStaff)
b=Bank()
d = Dept("Accounts",50)  #constructor call
d.showDeptInfo()
d.showBankInfo()

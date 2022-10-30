from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        pass
    def display(self):
        print("display called")

class B(A,ABC):
    def greet(self):
        print("greet called")
class C(B):
    def demo(self):
        print("demo called")
    def show(self):
        print("c show")
c = C()
c.show()


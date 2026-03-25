class Person:
    def disp(self):
        print("This is Parent class.")
class Employee(Person):
    def disp(self):
       super().disp()
e1 = Employee()
e1.disp()
class   Grandfather:
    def __init__(self,name):
        self.name=name
class Father(Grandfather):
    def __init__(self,name,age,address):
        super().__init__(name)
        self.age=age
        self.address=address
    def decrease_age(self,age):
        age=int(input("Enter an age:"))
        self.age=self.age-8
        print("The decreased age is:",self.age)
class Son(Father):
    def __init__(self,name,age,address):
        super().__init__(name,age,address)
        self.address=address
    def change_address(self,place):
        self.address=place
        p1=input("Enter an address:")
        print("The changed place is:",self.address)
a1=Son("Abhishek",23,"Balasore")
a1.decrease_age(3)
a1.change_address("Bhubaneswar")
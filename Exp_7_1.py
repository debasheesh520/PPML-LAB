class Vehicle:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
class Car(Vehicle):
    def __init__(self,brand,price,model):
        super().__init__(brand,price)
        self.model=model
    def display(self):
        print("The brand of the car:",self.brand)
        print("The price of the car is:",self.price)
        print("The model of the car is:",self.model)
p1=Car("Mercedes",230000,"Benz")
p1.display()
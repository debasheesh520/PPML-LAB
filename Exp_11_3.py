class Employee:
    def __init__(self,name,id,address,salary):
        self.name=name
        self.id=id
        self.address=address
        self.salary=salary
    def show(self):
        print("The name of the Employee:",self.name)
        print("The id of the Employee:",self.id)
        print("The address of the Employe:",self.address)
        print("The salary of the Employee:",self.salary)
    def increase_salary(self,amount):
        self.salary=self.salary+amount
        print("The Updated salary:",self.salary)
e1=Employee("Subham",222,"Balasore",90000)
e1.show()
e1.increase_salary(9000)      

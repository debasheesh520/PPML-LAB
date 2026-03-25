class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def enter_marks(self):
        n = int(input("Enter number of subjects: "))
        for i in range(n):
            m = float(input("Enter marks of subject {}: ".format(i+1)))
            self.marks.append(m)

    def calculate_cgpa(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        cgpa = percentage / 9.5
        return total, percentage, cgpa

    def display_result(self):
        total, percentage, cgpa = self.calculate_cgpa()

        print("\n----- Student Result -----")
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("CGPA:", round(cgpa, 2))
        print("----------")


class ResultSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        s = Student(name, roll)
        s.enter_marks()
        self.students.append(s)

    def show_results(self):
        for s in self.students:
            s.display_result()


system = ResultSystem()

while True:
    print("\n1. Enter Student Marks")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.show_results()

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid choice")
side1=int(input("Enter a number:"))
side2=int(input("Enter a number:"))
side3=int(input("Enter a number:"))
if(side1==side2==side3):
    print("It is an Equilateral triangle")
elif(side1==side2!=side3):
    print("It is an Isoscales traingle")
elif(side1!=side2==side3):
    print("It is an Isoscales traingle")
elif(side1!=side2!=side3):
    print("It is a scalane triangle")
else:
    print("Invalid Input")
num=int(input("Enter a given number:"))
if(num<25):
    print("You are in grade F")
elif( num>=25 and num<=45):
    print("You are in grade E")
elif(num>45 and num<=50):
    print("You are in grade D")
elif(num>50 and num<=60):
    print("You are in grade C")
elif(num>60 and num<=80):
    print("You are in grade B")
elif(num>80):
    print("You are in grade A")
else:
    print("Invalid Input")
n=int(input("Enter a number:"))
fast_digit=abs(n)//100
second_digit=abs((n)//10)%10
last_digit=abs(n)%10
sum=fast_digit+second_digit+last_digit
print("Sum",sum)
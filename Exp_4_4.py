numbers=[1,2,3,4,5]
try:
    numbers.remove(6)
except ValueError as e:
    print("Value Error Occured:",e)

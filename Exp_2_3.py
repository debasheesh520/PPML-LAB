class Calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        self.a=a
        self.b=b
        c=a+b
        print("The addition of a and b is:",c)
    def sub(self,c,d):
        self.c=c
        self.d=d
        e=c-d
        print("The substraction of c and d is:",e)
    def mul(self,m,n):
        self.m=m
        self.n=n
        o=m-n
        print("The multiplication of m and n is:",o)
    def div(self,p,q):
        self.p=p
        self.q=q
        r=p/q
        print("The division of p and q is:",r)
c1=Calculator()
c1.add(2,3)
c1.sub(5,4)
c1.mul(6,9)
c1.div(6,3)


x=int(input("Enter 1st Number"))
y=int(input("Enter 2nd Number"))
print("Select any option")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
def add(x,y):
    add=x+y
    return add
def sub(x,y):
    sub=x-y
    return sub
def mul(x,y):
    mul=x*y
    return mul
def div(x,y):
    div=x/y
    return div
while True:
    choice=int(input("Enter choice 1/2/3/4"))
    if choice==1:
        k=add(x,y)
        print("The sum of",x,"and",y,"is",'{}'.format(k))
    elif choice==2:
        l=sub(x,y)
        print("The subtraction of",x,"and",y,"is",'{}'.format(l))
    elif choice==3:
        m=mul(x,y)
        print("The Multiplication of",x,"and",y,"is",'{}'.format(m))
    elif choice==4:
        n=div(x,y)
        print("The Division of",x,"and",y,"is",'{}'.format(n))
    else:
        print("Invalid Input")

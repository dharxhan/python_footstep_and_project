def calculation(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return add,sub,mul
    print("After return keyword")
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
add,sub,mul=calculation(a,b)
print("Addition:",add)
print("Substraction:",sub)
print("Multiplication:",mul)
print("After funciton call")

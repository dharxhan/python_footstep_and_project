"""Swap two numbers with variable
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The numbers before swapping",a,b)
c=a
d=b
a=d
b=c
print("The swapped numbers are:",a,b)"""

"""Swap two numbers without variable"""
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The numbers before swapping",a,b)
a=a+b
b=a-b
a=a-b
print("The numbers after swapping:",a,b)

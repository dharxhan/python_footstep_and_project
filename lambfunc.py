"""value = lambda x:x*5
print("Result is :",value(10))"""
"""
value = lambda x,y:x if x>y else y
print("Result is :",value(10,20))
"""
"""
value = lambda x,y:[x if x>y else y]
print("Result is :",value(10,20))"""

value = lambda x,y,z:x if (x>y and x>z) else y if (y>z and y>x) else z
print("Result is :",value(10,20,30))

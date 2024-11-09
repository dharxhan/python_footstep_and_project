#1
"""def print_odd(numbers):
    for data in numbers:
        if data % 2==1:
            yield data
data =[10,5,20,15,6,7]
for x in print_odd(data):
    print(x)
"""
#2
"""
def SquareOfNums():
    x=1
    while True:
        yield x*x
        x+=1
for num in SquareOfNums():
    if num>32:
        break
    print("num is:",num)
"""
#3

def menu_card():
    print("1")
    yield("Idly")
    print("1")

    yield("Dosa")
    print("1")

    yield("Poori")
    print("1")

    yield("Vada")
    print("1")
    
#to stop infinte loop
    
for item in menu_card():
    print("Next item is:",item)
    
"""
object=menu_card()
print("Next item is:",next(object))
print("Next item is:",next(object))
print("Next item is:",next(object))
print("Next item is:",next(object))
print("Next item is:",next(object))
print("Next item is:",next(object))
"""











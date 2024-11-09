"""data=[1,2,3,4,5]
d_obj=iter(data)
print(next(d_obj))
print(next(d_obj))
print(next(d_obj))
print(next(d_obj))
print(next(d_obj))
print(next(d_obj))
"""

class OwnIterator:
    def __init__(self, num=0):
        print("Con")
        self.number = num

    def __iter__ (self):
        print("iter")
        self.x=1

        return self
    def __next__(self):
        if self.x<=self.number:
            own_iterator=self.x
            self.x +=1
            return own_iterator
        else:
            raise StopIteration

for x in OwnIterator(10):
    print("Num is:",x)

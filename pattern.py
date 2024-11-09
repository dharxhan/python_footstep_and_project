"""for row in range(1,6):
    for col in range(row):
        print("*",end=" ")
    print("\n")"""
"""
name="python"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
"""

name="python"
for i in range(len(name)):
    print(name[i])
for j in range(-6,0):
    print(name[j])
for k in range(-len(name),0):
    print(name[k])
print("\nReverse")
for l in range(1,len(name)+1):
    print(name[-l])

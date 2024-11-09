a=input("Enter the word:")
b=0
vowels=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for i in a:
    if i in vowels:
        b+=1
print("The number of vowels are:",b)

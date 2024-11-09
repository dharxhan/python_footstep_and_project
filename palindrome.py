a=input("Enter the word:")
b=""
for i in range(1,len(a)+1):
    b+=a[-i]
print(b)
if a==b:
    print("The word is palindrome")
else:
    print("The word is not a palindrome")


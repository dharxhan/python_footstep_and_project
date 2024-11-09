num=int(input("Enter the number:"))
sum1=0
while num>0:
    rem=num%10
    num=num//10
    sum1=sum1+rem
print("sum1 is:",sum1)


"""
num=int(input("Enter the number: "))
count=0
for i in range(2,(num//2)+1):
    if num%1==0:
        count=count+1
        print("no of entries:",count)
        break
if count==0:
    print("The number is prime:",num)
else:
    print("The number is not prime:",num)
"""

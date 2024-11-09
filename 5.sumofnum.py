 """
7.sum of a given number:

numbers = input("Enter numbers separated by spaces: ")
number_list = numbers.split()
total = 0
for number in number_list:
    total += int(number)
print("The sum of the numbers is:", total)


8.products of a given number
numbers = input("Enter numbers separated by spaces: ")
number_list = numbers.split()
total = 1
for number in number_list:
    total *= int(number)
print("The sum of the numbers is:", total)



9.print a given number in reverse
reversed = 0
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10    
    reversed = reversed* 10 + digit  
    num = num // 10         
    
print("Reversed number:", reversed)


10.palindrome or not

reversed = 0
num = int(input("Enter a number: "))
a=num
while num > 0:
    digit = num % 10    
    reversed = reversed* 10 + digit  
    num = num // 10         
    
print("Reversed number:", reversed)

if a==reversed:
    print("It is palindrome")
else:
    print("It is not a palindrome")

11.armstrong number or not

num = int(input("Enter a number: "))
sum = 0
a = num
while a > 0:
   digit = a % 10
   sum += digit ** 3
   a //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   
12.leap year or not

year = int(input("Enter the year:"))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

13.pattern

for row in range(1,6):
    for col in range(row):
        print("*",end=" ")
    print("\n")
    
14.reverse pattern

for row in range(6,0,-1):
    for col in range(row):
        print("*",end=" ")
    print("\n")

15.numbers pattern

for row in range(1,6):
    for col in range(row):
        print(row,end=" ")
    print("\n")

16.consecutive number pattern
for row in range(1,6):
    for col in range(row):
        print(col+1,end=" ")
    print("\n")

17.reverse numbers
for row in range(6,0,-1):
    for col in range(row):
        print(row,end=" ")
    print("\n")

17,(ii).reverse consecutive numbers

for row in range(6,0,-1):
    for col in range(row):
        print(col+1,end=" ")
    print("\n")

18.first 100 even numbers among 1000 number

even = []
for num in range(1, 1001):
    if num % 2 == 0:
        even.append(num)
        if len(even) == 100:
            break
print("The first 100 even numbers are:")
print(even)

19.first 100 prime numbers among 1000 number
prime = []
for num in range(2, 1001):
    isprime = True
    for i in range(2, int(num // 2) + 1):
        if num % i == 0:  
            isprime = False
            break
    if isprime:
        prime.append(num)
        if len(prime) == 100:
            break
print("The first 100 prime numbers are:")
print(prime)

20.basic calculator

operation = input("Enter the operation: ").strip().lower()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operation == 'add':
    result = num1 + num2
elif operation == 'subtract':
    result = num1 - num2
elif operation == 'multiply':
    result = num1 * num2
elif operation == 'divide':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operation"
print(f"The result is: {result}")

21.multiplication table

num = int(input("Entet the number:"))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

22.gross salary

basic_salary = float(input("Enter basic salary: "))
hra = float(input("Enter house rent allowance: "))
medical_allowance = float(input("Enter medical allowance: "))
other_allowances = float(input("Enter other allowances: "))
deductions = float(input("Enter total deductions: "))
gross_salary = basic_salary + hra + medical_allowance + other_allowances - deductions
print("Gross Salary:",gross_salary)

23.percentage for 6 subjects

print("Enter the marks in each subjects:")
a,b,c,d,e,f=map(int, input().split())
mean=(a+b+c+d+e+f)/6
per=(mean/600)*600
print("Percentage:",per)

24.Swap two numbers without using a variable

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a, b = b, a
print("After swapping:","a:",a,"b:",b)

25.Swap two numbers 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c=0
c=a
a=b
b=c
print("After swapping:","a:",a,"b:",b)

26.perfect number or not

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print("It is a Perfect Number" ,Number)
else:
    print("It is not a Perfect Number" ,Number)

27.Factorial of a given number

num = int(input("Enter a number: "))
factorial = 1
for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",num,"is",factorial)

28.fibonacci series

tot= int(input("total fib "))
a, b = 0, 1
count = 0
if tot <= 0:
   print("Please enter a positive integer")
elif tot == 1:
   print("Fibonacci sequence upto",tot,":")
   print(a)
else:
   print("Fibonacci sequence:")
   while count < tot:
       print(a)
       c = a + b
       a = b
       b = c
       count += 1

29.ASCII table

for i in range(256):
    ch = chr(i)
    print('ASCII value of', i, 'is =', ch)

30.0 1 pattern

rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()

31.Print star horizontal tri

rows = 5
for i in range(1, rows + 1):
    print("*" * i)
for i in range(rows, 0, -1):
    print("*" * i)


32.vowel or not

input_string = input("Enter a string: ").lower()
vowel = 0
vowels = 'aeiou'
for char in input_string:
    if char in vowels:
        vowel += 1
if vowel > 0:
    print(f"The string contains vowel",vowel)
else:
    print("The string does not contain any vowels.")

33.sum of natural numbers

sum_of_numbers = 0

for number in range(1, 11):
    sum_of_numbers += number
print(f"The sum of the first 10 natural numbers is: {sum_of_numbers}")

34.postive or negative

a=int(input("Enter the number:"))
if a>=0:
    print("The number is positive")
else:
    print("The number is negative")

35.alphabet or not

a= input("Entet the aplhabet:")
if len(a)==1 and a.isalpha():
    print("This is an alphabet")
else:
    print("This is not an alphabet")

36.factors of a num

num = int(input("Enter a number: "))
factors = []
for i in range(1, num + 1):
    if num % i == 0:  
        factors.append(i)
print(f"The factors are:",factors)
"""

















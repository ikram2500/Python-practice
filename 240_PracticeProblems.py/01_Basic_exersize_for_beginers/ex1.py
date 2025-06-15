"""#1. Swap the number without using third variable
x = int(input("enter the first number"))
y = int(input('enter the second number'))

print(x,y)

x = x+y
y= x-y
x=x-y

print(x,y)
"""
'''#2. Write a program to extract each digit from an integer in the reverse order.
n = input("enter the no:  ")
y = n[::-1]
print(y)
k = " ".join(y)

print(k)'''

# Write a program that will give you the sum of 3 digits.
x = int(input('Please inter three digit number'))
a= x%10
print(a)
num = x//10
b =num%10 
print(num)
c=num//10
print(c)
print(a+b+c)


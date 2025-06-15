'''a = input('Enter a number: ')
b = input('Enter another number: ') 
try:
    c = int(a) + b 
    print('The sum of the numbers is:', c)

#except Exception as e: or you can use only except
except:
    print('There was an error:')'''

# try with else clause 
'''a = int(input('Enter a number: '))
try:
    if a % 2 == 0:
        print(f'{a} is even')
    else:
        print('The number is odd')
except Exception as e:
    print('There was an error:', e)
else:
    print('The code ran successfully')
'''
#Finally clause

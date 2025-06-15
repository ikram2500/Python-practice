a=8
b=2
try:
    k = a//b
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero ")
finally:
    print('this is always execute')
assert b!=0 , 'Divide by 0 error'
print(a / b)

def fun():
    var1 = 10
    def gun():
        nonlocal var1
        var1= var1 + 10
        print(var1)
    gun()
fun()
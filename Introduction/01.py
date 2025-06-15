#Python Keywords
"""Keywords in Python are reserved words that can not be used as a variable name, function name, or any other identifier.
and,as,asser,class,continue,def,del,elif,else,except,false,finally,for,from,global,if,import,is,in,lambda,none,nonlocal,not
or,pass,raise,return,true,try,while,with,yield"""
import keyword
 
# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

# using "in" to loop through
for i in 'geeksforgeeks':
    print(i, end=" ")
 
print("\r")
"""Iteration Keywords – for, while, break, continue
for: This keyword is used to control flow and for looping.
while: Has a similar working like “for”, used to control flow and for looping.
break: “break” is used to control the flow of the loop. The statement is used to break out of the loop and passes the control to the statement following immediately after loop.
continue: “continue” is also used to control the flow of code. The keyword skips the current iteration of the loop but does not end the loop.
Example: For, while, break, continue keyword"""

for i in range(10):
 
    print(i, end=" ")
    # break the loop as soon it sees 6
    if i == 6:
        break


    # loop from 1 to 10
i = 0
while i < 10:
 
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        i += 1
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
 
    i += 1

    def fun():
        s = 0
        for i in range(10):
            s +=i
            return s
    print (fun())
 


 
#https://www.youtube.com/watch?v=-65r_3r-nN4&t=2730s 

#f = open("demo.txt")

'''with open("demo.txt", "r") as f:
    content = f.read()
    print(content)
'''
'''with open("demo.txt", "w") as f:
    f.write("This is a new line")
    f.close()'''

'''with open("demo.txt", "a") as f:
    added_text = f.write("\nThis is append mode")
    print(added_text)
    f.close()'''

'''f = open("demo.txt", "r")
data_read = f.read()
count = len(data_read)
print(count)
f.close()'''

f = open("demo.txt", "r")
#f.write("This is a new line")
#f.write("\nThis is a new line")
#f.write("\nTopics are open, read, write, append, close")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close


#global keyword


a=10

def add():
    global a
    a=5
    a+=2
    print(a)
add()
print(a)
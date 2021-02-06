import sys

size=int(input("Enter the size of stack:"))
top=0
stk=[]
n=1
def push():
    element=int(input("Enter the elements into the stack:"))
    global top
    if(top<size):
        stk.insert(top,element)
        print(element,"pushed in")
        top+=1
    else:
        print("stack overflow")

def pop():
    global top
    top-=1
    if(top<0):
        print("stack is empty")
    else:
        print(stk[top],"popped out")


def display():
    for i in range(0,top):
        print(stk[i])

def ext():
    sys.exit()

while(n!=0):
    option=int(input("Enter 1.push 2.pop 3.display 4.exit"))

    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    elif option==4:
        ext()
    else:
        print("Invalid option")

    n=int(input("do you want to continue press 0 to exit"))
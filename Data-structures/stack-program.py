#stack program

size=int(input("Enter the size of stack:"))
top=0
stk=[]
n=1

def push():
    element=int(input("Enter the element:"))
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
    if top<0:
        print("stack is empty")
    else:
        print(stk[top],"popped out")

def display():
    for i in range(0,top):
        print("elements in stack:",stk[i])


while(n!=0):
    option=int(input("Enter operations press 1.push 2.pop 3.display"))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    else:
        print("Invalid option")

    n=int(input("Do you want to continue press 0 for exit"))




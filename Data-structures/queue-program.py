import sys

size=int(input("Enter the size of queue"))
rear=0
front=0
queue=[]
n=1

def insrt():
    element=int(input("Enter the element to insert into queue"))
    global rear

    if (rear < size):
        queue.insert(rear, element)
        rear += 1
        print(element, "is inserted")
    else:
        print("queue is full")


def delet():
    global front

    if(front==rear):
        print("queue is empty")
    else:
        print(queue[front],"is deleted")
        front+=1


def display():
    for i in range(0,rear):
        print(queue[i])


def ext():

    sys.exit()


while(n!=0):
    option=int(input("Enter the options 1.Insert 2.Delete 3.Display 4.Exit"))
    if option==1:
        insrt()
    elif option==2:
        delet()
    elif option==3:
        display()
    elif option==4:
        ext()
    else:
        print("Invalid option")
    
    n=int(input("do you want to continue press 0 to exit"))

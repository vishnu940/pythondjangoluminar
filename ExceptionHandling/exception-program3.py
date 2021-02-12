n1=int(input("num1"))
n2=int(input("num2"))
try:
    res=n1/n2
    print(res)
except:
    n2 = int(input("num2"))
try:
    res = n1 / n2
    print(res)
except:
    n2 = int(input("num2"))
    res = n1 / n2
    print(res)
finally:
    print("i have created file operation")
    print("i have created database")
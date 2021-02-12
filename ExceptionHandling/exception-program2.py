lst=[20,30,40]
ps=int(input("Enter the position to search:"))
n1=int(input("num1"))
n2=int(input("num2"))
try:
    res = n1 / n2
    print(res)
except Exception as e:
    print(e.args)

try:
    print(lst[ps])
except Exception as e:
    print(e.args)

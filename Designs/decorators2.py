def subtract(func):

    def inner(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return func(num1,num2)
    return inner

@subtract
def sub(num1,num2):
    return num1-num2

res=sub(10,20)
print(res)


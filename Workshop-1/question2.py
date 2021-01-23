#Find Sum of the Series
#Given a natural number n (where 1≤n≤9), find the sum of the series having n number of numbers such that
# the series is n,nn,nnn,…nnn…n times.


num=input("Enter number:")#'2'
i=1
a=0
ch=""
while(i<=int(num)):#1<=2
    res=num*i#'2'*1='2'
    ch=ch+"+"+res
    a+=int(res)#0+2=2
    i+=1
ch=ch.lstrip("+")
print(ch,"=",a)
#print("=",a)
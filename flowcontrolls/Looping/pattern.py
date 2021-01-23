num=input("Enter number:")#"2"
i=1
data=0
ch=""
while(i<=int(num)):#1<=2 2<=2 3<=2
    res=num*i#res="2"*1="2" "2"*2="22"
    ch=ch+"+"+res
    data+=int(res)#data=data+int(res) 8+2=2 2+int("22") 2+22=24
    i+=1#i=2 3
ch=ch.lstrip("+")
print(ch)
print("=",data,end="")#24

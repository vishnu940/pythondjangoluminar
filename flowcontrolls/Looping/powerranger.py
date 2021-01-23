num=int(input("Enter number:"))#3
lower=int(input("Enter lower limit:"))#3
upper=int(input("Enter upper limit:"))#28
for i in range(1,(upper+1)):#checks limit from 1,28
    if i**num in range(lower,upper):#1**3 in (3,28) 2**3 in (3,28)
        print(i)



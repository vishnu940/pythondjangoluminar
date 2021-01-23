f=open("covid_19_india.csv","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    break
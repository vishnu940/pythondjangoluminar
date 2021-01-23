#program to search name

lst=["Infosys","Tcs","Wipro","Cognizant","Ey","Sutherland"]
flag=0
element=input("Enter the company name to search:")
for comp in lst:
    if(comp==element):
      flag+=1
      break
    else:
        pass
if(flag==0):
    print("company not found")
else:
    print("company found")
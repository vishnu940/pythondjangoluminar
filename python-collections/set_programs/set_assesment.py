lst1=["David","Harry","Kiran","John","Kiran","Joseph"]
lst2=["David","Harry"]
st1=set(lst1)
st2=set(lst2)
passed_st=st1.difference(st2)
print("passed students:",passed_st)
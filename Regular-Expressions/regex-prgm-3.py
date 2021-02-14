#quantifiers

from re import *

#pattern="a"#check for any number of a
#pattern="a+"#check for any number of a excluding 0 number of a
#pattern="a*" #check for any number of a including 0 number of a
#pattern ="a?"#check any number of a(takes single a), including 0 number of a
#pattern="a{2}"#check for 2 number of a
#pattern='a{2,4}'#check for maximum and minimum number of a
matcher=finditer(pattern,"abbaaaabbbabbaabbabaaaa")
for match in matcher:
    print(match.start(),"-->",match.group())

#[1,2,3,4,5,6] [4,5,6,1,2,3]#check array rotation
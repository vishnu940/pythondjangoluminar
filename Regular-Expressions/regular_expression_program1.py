#Regular expressions

#step 1 import re module
#from re import *

#Regular expressions are used to match patterns

from re import *

pattern="ab"

matcher=finditer(pattern,"abababbbbbbaaaaaababab")#returns iterable
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)



from re import *

# pattern='ab'#check for either a or b
#
# matcher=finditer(pattern,"abcba _627@fc")
# for match in matcher:
#     print(match.start())#0 1
#     print(match.group())#a b

#predefined character set
# pattern="[a-z]"#will check for lower case a to z
# matcher=finditer(pattern,"abc _627@fc")
# for match in matcher:
#     print(match.start())#0 1
#     print(match.group())#a b

#pattern="[A-Z]"#will check for upper case A to Z
#pattern='[a-zA-Z]'#checks for both lower and upper case
#pattern='[0-9]'#check for digits
#pattern='[^0-9]'#will check for except 0-9
#(^) symbol is used to check for except
#pattern='[a-zA-Z0-9]'#check for lower case a to z,upper case A to Z,digits from 0-9
#pattern='[^a-zA-Z0-9]'#check for except lower case a to z,upper case A to Z,digits from 0-9
# matcher=finditer(pattern,"aBc _123@FC")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#predefined characters

#pattern='\s'#checks for spaces
#pattern='\d'#checks for digits[0-9]
#pattern="\D"#checks except digits[^0-9]
#pattern='\w'#checks for all words except special characrers [a-zA-Z0-9_]
pattern='\W'#except words
matcher=finditer(pattern,"aBc _123@FC$&*")
for match in matcher:
    print(match.start(),"->",match.group())

#string is a sequence of characters
#how we represent string in python

#name="Luminar Technolab"
#print(name)

#name="""Luminar Technolab
#       Kakkanad
#       Kochi"""
#print(name)

#name="Luminar Technolab Software Training Institution"
#spliting string
#words=name.split(" ")
#print(words)

#name="My,name,is,David"
#words=name.split(",")
#print(words)

#converting name into uppercase

#name="luminar technolab"
#str=name.upper()
#print(str)

#converting name into lower case
#name="LUMINAR TECHNOLAB"
#str=name.lower()
#print(str)

#Remove character from begining

#name="dDavid"
#str=name.lstrip("d")
#print(str)

#Remove character from end

#name="Davide"
#str=name.rstrip("e")
#print(str)

#name="ddDavidee"
#name=name.lstrip("dd")
#name=name.rstrip("ee")
#print(name)

#name="TTLuminar TechnolabTT"
#name=name.lstrip("TT")
#print("name=",name)
#name=name.rstrip("TT")
#print("name=",name)

#print first letter of string

name="David"
print(name[2])
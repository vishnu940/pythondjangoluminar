#find first recursive character A
pattern="ABABBAC"
dict={}

for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,"recursive character")

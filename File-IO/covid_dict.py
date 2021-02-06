#print the confirmed and cured cases in state kerala

f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cured=data[6]
    death=data[7]
    confirmed=data[8]

    if state not in dict:
        dict[state]={"state":state,"cured":cured,"death":death,"confirmed":confirmed}
    else:
        dict[state] = {"state": state, "cured": cured, "death": death, "confirmed": confirmed}
print(dict)

def covid_data(**kwargs):
    state=kwargs["state"]
    if state in dict:
        print("state:",dict[state]["state"])
        print("confirmed cases:", dict[state]["confirmed"])
        if "crd" in kwargs:
            crd=kwargs["crd"]
            print("cured cases:",dict[state][crd])
    else:
        print("Data does not exist")
covid_data(state="Kerala",crd="cured")



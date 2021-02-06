#print the confirmed and cured cases in state kerala

f=open("covid_19_india.csv","r")
covid={}
for lines in f:
    id,date,time,state,indian,foreign,cured,death,confirmed=lines.rstrip("\n").split(",")
    if id not in covid:
        covid[id]={"id":id,"date":date,"time":time,"state":state,"indian":indian,"foreign":foreign,"cured":cured,
                   "death":death,"confirmed":confirmed}
    else:
        covid[id] = {"id": id, "date": date, "time": time, "state": state, "indian": indian, "foreign": foreign,
                     "cured": cured,
                     "death": death, "confirmed": confirmed}

        #print(covid[id])

def covid_data(**kwargs):
    id=kwargs["id"]

    if id in covid:
        print("state:",covid[id]["state"])

        if "cnfrm" in kwargs:
            cnfrm=kwargs["cnfrm"]
            print("confirmed cases:",covid[id][cnfrm])
        else:
            pass
        if id in covid:
            if "cure" in kwargs:
                cure=kwargs["cure"]
                print("cured cases:",covid[id][cure])
            else:
                pass

    else:
        print("Data does not exist")


covid_data(id="7558",cnfrm="confirmed",cure="cured")
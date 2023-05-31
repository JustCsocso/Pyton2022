class radio:
    def __init__(self,ora,perc,adas,nev):
        self.ora=ora
        self.perc=perc
        self.adas=adas
        self.nev=nev
    def __repr__(self):
        return f"{self.ora} {self.perc} {self.adas} {self.nev}"
    
f=open("cb.txt")
adatok=[]
for sorok in f:
    temp=sorok.strip().split(";")
    adatok.append(radio(*temp))

f.close()
elso=adatok.pop(0)
print(adatok)

print("3. feladat: ")
print(f"Bejegyzések száma: {len(adatok)} db")

print("4. feladat: ")
adasok=[]
for e in adatok:
    if e.adas=="4":
        print("Volt négy adást indító sofőr")
        break
else:
    print("Nem volt négy adást indító sofőr")


print("5. feladat: ")
hasznal=input("Kérek egy nevet: ")
for e in adatok:
    if e.nev==hasznal:
        print(f"{hasznal} {len(e.nev)}x használta a CB-rádiót")
        break
else:
    print("Nincs ilyen nevű sofőr")


print("6. feladat")
def AtszamolPercre():
    
    osszeg=ora*60+perc
    #print(osszeg)
AtszamolPercre()



print("8. feladat: ")
becen=[]
print("9.feladat: Legtöbb adást indító sofőr: ")
nagy=[e.adas for e in adatok]
nagyon=max(nagy)
for e in adatok:
    if e.adas==nagyon:
        print(f"Név: {e.nev}\nAdások száma: {e.adas} alkalom")
    
 






    



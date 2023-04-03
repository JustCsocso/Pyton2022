
f=open("EUcsatlakozas.txt")
adatok=[]
for e in f:
    temp=e.replace("\n","")
    adatok.append(temp)
   

f.close()
#print(adatok)

print("3. feladat: EU tagállamainak száma: {} db".format(len(adatok)))

print("4. feladat: ")

ev=0
for e in adatok:
    if e[-10:-6]=="2007":
        ev+=1

print(f"2007-ben {ev} ország csatlakozott")

print("5. feladat: ")
      
magyar=[]
for e in adatok:
    if e[:12]=="Magyarország":
        magyar.append(e[-10:])


print(f"Magyarország csatlakozása dátuma: {magyar[0]}")

print("6. feladat: ")

if magyar[0][5:7] =="05":
    print("Májusban volt csatlakozás!")
else:
    pass

print("7. feladat: ")

utolso=[]
for e in adatok:
    if e[-10:-6]==max:
        utolso=e[0]


print("8. feladat: ")


        





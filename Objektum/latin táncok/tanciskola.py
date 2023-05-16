class tanc:
   def __init__(self,tanc,fiu,lany):
      self.tanc=tanc
      self.fiu=fiu
      self.lany=lany
   def __str__(self):
      return "Tánc: {}, lány: {}, fiú: {}".format(self.tanc,self.lany,self.fiu)

    def isVilma(self):
        return self.lany=="Vilma"

        #másik megoldás
        #if self.lany=="Vilma":
        #   return True
        #else:
        #    return False

        


   
f=open("tancrend.txt")

sorok=[]
#2. megoldás
tancok2=[]
temp=[]

for e in f:
   sorok.append(e.strip())
   #2. megoldás
   if len(temp)<3:
      temp.append(e)
   else:
      tancok2.append(tanc(temp[0],temp[1],temp[2]))

f.close()

print(sorok)      
print(sorok[:3])

#1. megoldás
tancok=[]
for i in range(len(sorok)//3):
   tancnev=sorok[i*3]
   lany=sorok[i*3+1]
   fiu=sorok[i*3+2]
   tancok.append(tanc(tancnev,lany,fiu))


#print(tancok)
print("2. feladat")
print("Első tánc: {}, utolsó: {}".format(tancok[0].tanc,tancok[-1].tanc))

db=0
for egyTanc in tancok:
    if egyTanc.tanc=="samba":
        db+=1

print("Ennyi samba volt: {}".format(db))

print("Vilma ezekben szerepelt: ")

for egyTanc in tancok:
    if egyTanc.isVilma():
        print(egyTanc.tanc)

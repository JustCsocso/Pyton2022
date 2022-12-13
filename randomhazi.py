import random

#y=0
#while y==0:
#    szam=random.randint(1000,9999)
#    if szam %6==0: 
#        y=1
#        print(szam)
#    elif szam %12!=0:
#        y=1
#print(szam)

#más megoldás
#print(random.randrage(167,1667,2)*6)

#más megoldás
print((random.randint(83,832)*2+1)*6)

szavak=["alma","körte","barack","banán","dinnye","szőlő"]

#random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))

#[["alma",14]],["körte",18],[]...]
print("-",20)

nagyLista=[]
for e in szavak:
    print(e)
    kisLista=[]
    kisLista.append(e)
    kisLista.append(random.randint(12,312))
    print(kisLista)
    nagyLista.append(kisLista)
    
print(nagyLista)

for e in nagyLista:
    print(e[0].ljust(10),str(e[1]).rjust(5),"kg")

def oszlopVissza(hanyadik):
    oszlop=[]
    for e in tabla:
        oszlop.append(e[hanyadik-1])
    return oszlop




    


gyumolcsok=["alma","szőlő","körte","barac","dragonfruit","licsi"]

print("Ennyi gyümölcs van: {}".format(len(gyumolcsok)))



#print(gyumolcsok[3])
#gyumolcsok[3]+="k"
#gyumolcsok[3]="barack"

print(gyumolcsok.index("barac"))

#gyumolcsok[gyumolcsok.index("barac")]+="k"

index=gyumolcsok.index("barac")
gyumolcsok[index]+="kos pite"




print(gyumolcsok[3])

print("Rövid gyümölcsök")

#for i in range(len(gyumolcsok)):
#      if len(gyumolcsok[i])<5:
#        print(gyumolcsok[i])

rovid=[]
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])

print(rovid)


rovid=[]
for e in gyumolcsok:
    if len(e)<5:
        rovid.append(e)

print(rovid)

rovid=[e for e in gyumolcsok if len(e)<5]

print(rovid)

rovid=[]
i=0
while i<len(gyumolcsok):
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
    i+=1

print(rovid)




rovid=[]
i=0
while True:
    print(i)
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
    i+=1
    if len(gyumolcsok)-1==i:
        break
    

print(gyumolcsok[:2])
        
print(gyumolcsok[len(gyumolcsok)-2:])

    
       
print(gyumolcsok[1:-1])

paratlan=gyumolcsok[1::2]

print(paratlan)

paros=gyumolcsok[0::2]

print(paros)

masolat=gyumolcsok
masolat.reverse()
print(", ".join(gyumolcsok[::-1]))


tabla=[]
for i in range(20):
    sor=[]
    for k in range(10):
        sor.append((i+1)*(k+1))
    tabla.append(sor)

print(tabla)

        
oszlop=[]
for e in tabla:
    oszlop.append(e[0])

print(oszlop)
print(oszlopVissza(5))
print(oszlopVissza(10))




beSzam=0

while beSzam<2 or beSzam>5:
    beSzam= int(input("Adj meg egy számot 2 és 5 között: "))

autok=[]
for i in range(0, beSzam):
    autok.append(input("Kérem a(z) " +str(i+1)+ ". autó márkát: "))
    
print(autok)

szo="banánfa"

mgh=["ö","ő","ü","ű","a","á","é","e","o","ó","i","í","u"]
if szo.lower()[0] in mgh:
    print("az")
else:
    print("a")

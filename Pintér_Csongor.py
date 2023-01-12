#1. feladat: Kérj be 8 számot egy megfelelő adatszerkezetbe!
szamok=[]
for i in range(8):
    szamok.append(int(input("Kérek egy számot: ")))
#szamok=[1,2,3,4,5,6,7,8]
print(szamok)

#2. feladat: A bekért számokat írasd ki egymás mellé!
for i in szamok:
    print(str(i)+"\t",end="")

print()
#3. feladat: A bekért számokat írasd ki 4 oszlopba!
for i in range(8):
    print(str(szamok[i])+"\t",end="")
    if i%6==3:
        print()

print()   
#4. feladat: Számold ki a bekért számok összegét!
osszeg=sum(szamok)
print("Összeg: ",osszeg)

#5. feladat: A mellékelt szöveget tárold el a programodban:
szoveg="Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."
#6,7:
betu=""
while betu!="end":
    betu=input("Kérek egy betűt: ")
    szoveg2=szoveg.count(betu)
    print(szoveg2)

#8. feladat: Az eltárolt szöveget írasd ki fordított sorrendben (betűnként)!
print(szoveg[::-1])

#9. feladat: Az eltárolt szövegből töröld az "orna" szöveget! Mekkora most a mérete?
szoveg2=szoveg.replace("orna","")
print(len(szoveg2))

#10. feladat: Készíts egy függvényt, ami bekér 1 karaktert (addig folytatja, amíg 1-et nem kap)! A bekért karakterrel rajzolja ki a következő ábrát:
def fuggveny():
    kari=""
    while kari!="1":
        kari=int(input("Kérek egy karaktert: "))
       
    
    
    

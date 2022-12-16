import random
import math

minimumErtek=int(input("Add meg a kezdés helyét: "))
maximumErtek=int(input("Add meg, hogy hol legyen vége: "))
darab=int(input("Hány darab kell: "))


lista=[]
for i in range(darab):
    lista.append(random.randint(minimumErtek,maximumErtek))
print(lista) 

legnagyobb=max(lista)
egyseg=80/legnagyobb
for e in lista:
    print("**"*math.floor(e*egyseg))

#3 jegyű szám bekérése:
szam="12"
while len(szam)!=3:
    szam=input("Kérek egy 3 jegyű számot: ")

szam=int(szam)
if szam%12==0:
    print("Osztható")
print(szam)


szoveg="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean efficitur nunc at aliquam varius. Praesent odio neque, malesuada nec dolor ac, sagittis pretium neque. Nullam mollis lorem id turpis ullamcorper fringilla non a augue. Maecenas blandit massa lectus, euismod interdum diam vehicula eget. Mauris lectus dui, vehicula at velit ac, fermentum blandit eros. Integer tristique sed erat at fringilla. Ut a dui ac nulla tristique maximus in in diam."
betu=""
print(len(szoveg.split(" ")))
szoveg2=szoveg.replace(betu,betu.upper())
print(szoveg2)

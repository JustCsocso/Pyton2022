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
    print("**"(e*egyseg))



lista=["Bence","László","Ferenc"]
lista.append("Oszkár")
try:
    print(lista[3])
except:
    print("valami nem jó!")
else:
    print("Sikeres lefutás!")
finally:
    print("Ez a vége")

try:
    szam=int(input("Kérek egy számoz :"))
except:
    pass


print(szam)

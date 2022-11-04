

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

szam=""
while szam=="":
    try:
        szam=int(input("Kérek egy számoz: "))
    except ValueError as e:
        print(e)
        print("Ez nem szám!")            
    except ValueError:
        print("Ismeretlen hiba")
print(szam)

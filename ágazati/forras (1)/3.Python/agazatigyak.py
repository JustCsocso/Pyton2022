szoveg=input("Kérek egy szöveget: ")

while True:
    try:
        szam=int(input("Kérek egy egész számot: "))
        break
    except:
        print("Ez nem egész szám! ")
        
try:
    for i in range(szam):
        print(szoveg[szam],end="")
except:
    print("Sajnos nincs ilyen betű")

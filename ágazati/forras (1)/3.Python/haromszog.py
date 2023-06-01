lista=[]
def haromszog():
    try:
        a=int(input("Kérek egy egész számot: "))
        b=int(input("Kérek egy egész számot: "))
        c=int(input("Kérek egy egész számot: "))
        lista.append(a,b,c)
    except:
        print("Ez nem egész szám! ")

haromszog()

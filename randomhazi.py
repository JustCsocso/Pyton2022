import random

y=0
while y==0:
    szam=random.randint(1000,9999)
    if szam %6==0: 
        y=1
        print(szam)
    elif szam %12!=0:
        y=1
        print(szam)

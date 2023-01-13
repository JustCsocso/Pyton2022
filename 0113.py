#100.000 születési dátum középiskolás diákoknak
import random
f=open("datum.txt","w")

for i in range(100000):
    ev=random.randint(2003,2008)
    ho=random.randint(1,12)
    #nap=random.randint(1,30)
   
    if ho==1 or ho==3 or ho==5 or ho==7 or ho==8 or ho==10 or ho==12:
        nap=random.randint(1,31)
    
    elif ho==4 or ho==6 or ho==9 or ho==11:
        nap=random.randint(1,30)
    else:
        nap=random.randint(1,28)
    if ho==1 or ho==2 or ho==3 or ho==4 or ho==4 or ho==5 or ho==6 or ho==7 or ho==8 or ho==9:
        nap="0" + str(ho)
    if nap==1 or nap==2 or nap==3 or nap==4 or nap==4 or nap==5 or nap==6 or nap==7 or nap==8 or nap==9:
        nap="0" + str(nap)  


    szoveg=str(ev) + "." + str(ho) + "." + str(nap) + "\n"
    #print(szoveg)
    
    f.write(szoveg)
f.close()

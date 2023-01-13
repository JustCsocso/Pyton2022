#100.000 születési dátum középiskolás diákoknak
import random

ev=[]
ho=[]
nap=[]

for i in range(10):
    ev.append(random.randint(2003,2008))
for i in range(10):
    ho.append(random.randint(1,12))
for i in range(10):
    nap.append(random.randint(1,31))

print("Év: "+ str(ev))
print("Hónap: "+ str(ho))
print("Nap: "+ str(nap))


    

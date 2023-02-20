
def ido2mp():
    pass



#1.feladat
eredmenyek=[]
f=open("triatlon.txt")
for egySor in f:
    temp=egySor.replace("\n","").split(";")
    eredmenyek.append(temp)

    

f.close()


eredmenyek.pop(0)
print(eredmenyek)

#print("2. feladat: A versenyen "+str(len(eredmenyek))+ " induló volt")
print("2. feladat: A versenyen {} induló volt".format(len(eredmenyek)))

print("3. feladat")

import json
file=open('bemenet.json')
tablak=json.load(file)
file.close()

import random
tablaszam=random.randint(0,0)

import fuggvenyek
fuggvenyek=fuggvenyek
tabla=tablak[tablaszam]
fuggvenyek.megjelenites(tabla)

ures=fuggvenyek.ures_db_szam(tabla)
#while(ures!=0):

x=int(input())
y=int(input())
szam=int(input())
tabla=fuggvenyek.beker(x,y,szam,tabla)
fuggvenyek.megjelenites(tabla)
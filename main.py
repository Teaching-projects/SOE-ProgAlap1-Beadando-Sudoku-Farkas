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
"""
while(ures!=0):
    x=int(input())
    y=int(input())
    szam=int(input())
    import copy
    uj_tabla=fuggvenyek.beker(x,y,szam,copy.deepcopy(tabla))
    if(uj_tabla==tabla):
        continue
    else:    
        fuggvenyek.megjelenites(uj_tabla)
        ures-=1
    tabla=copy.deepcopy(uj_tabla) 
    print(ures)  

"""    
valami=[[3,1,2],[1,2,3],[1,2,3]]
fuggvenyek.ellenorzes(valami)


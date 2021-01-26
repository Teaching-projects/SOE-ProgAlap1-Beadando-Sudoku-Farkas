import json
file=open('bemenet.json')
tablak=json.load(file)
file.close()



import random
tablaszam=random.randint(0,4)



import fuggvenyek
fuggvenyek=fuggvenyek
tabla=tablak[tablaszam]
fuggvenyek.megjelenites(tabla)



ures=fuggvenyek.ures_db_szam(tabla)



while(ures!=0):
    print("kerlek ird be eloszor a poziciot, majd a szamot!")
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



vegeredmeny=fuggvenyek.ellenorzes(tabla)



if vegeredmeny==True:
    print("Gratulálok, megoldottad a feladványt :)")
else: print("Sajnálom, helytelen megoldás :(")


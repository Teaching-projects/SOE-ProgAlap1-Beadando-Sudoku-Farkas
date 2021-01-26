def megjelenites(tabla:list):
   
    """Ez a Függvény a megejelenítésért felelős.

    Args:
        tabla (list): A fő programban megadott táblát jeleníti meg.
    """

    for i in range(len(tabla)):
        sor="|"
        for j in range(len(tabla)):
            if(tabla[i][j]==-1):
                sor=sor+" "+"|"
            else: sor=sor+str(tabla[i][j])+"|"                
        print(sor)    




def beker(xpoz:int,ypoz:int,ertek:int,tabla:list):
    """Ez a függvény a bekérést segíti elő. A bekért érteékeket ellenőrzi, a játék szabályai alapján.
       Ha minden feltételnek megfelel, akkor be kerül a számunk a játék táblájába. 

    Args:
        xpoz (int): az x pozíció(koordináta)
        ypoz (int): az y pozíció(koordináta)
        ertek (int): az a szám amit az x,y koordináta helyére írunk be
        tabla (list): a játék táblája 

    Returns:
        [list]: a jelenlegi táblát írja ki
    """

    if(xpoz<=9 and xpoz>=1 and ypoz<=9 and ypoz>=1 and ertek<=9 and ertek>=1):
        if(tabla[xpoz-1][ypoz-1]==-1):
            tabla[xpoz-1][ypoz-1]=ertek
        else: print("hibas pozicio")    
    else: print("add meg újra") 
    return tabla



def ures_db_szam(tabla:list):
    
    """Ez a függvény megadja, hány üres mező van a táblánkon.

    Args:
        tabla (list): a jelenlegi tábla

    Returns:
        [int]: az üres mezők száma
    """

    db=0
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if(tabla[i][j]==-1):
                db+=1
    return db            



def ellenorzes(tabla:list):
    
    
    """Ez a függvény ellenőrzi, hogy jól oldottuk-e meg a feladatot. Először a sorokat, oszlopokat járja be, majd
        a 3x3-as négyzeteket vizsgálja. 

    Args:
        tabla (list): az ellenőrizendő tábla

    Returns:
        [bool]: igaz, ha jól oldottuk meg
    """


    for i in range(len(tabla)):
        sor=set()
        for j in range(len(tabla[i])):
            sor.add(tabla[i][j])
        if len(sor)!=9:
            return False    


    for i in range(len(tabla)):
        oszlop=set()
        for j in range(len(tabla[i])):
            oszlop.add(tabla[j][i])
        if len(oszlop)!=9:
            return False 


    for i in range(0,3):
        for j in range(0,3):
            negyzet=set()
            for k in range(0,3):
                for l in range(0,3):
                    negyzet.add(tabla[i*3+k][j*3+l])
            if len(negyzet)!=9:
                return False
    return True    
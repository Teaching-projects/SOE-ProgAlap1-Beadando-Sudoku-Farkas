def megjelenites(tabla:list):
    for i in range(len(tabla)):
        sor="|"
        for j in range(len(tabla)):
            if(tabla[i][j]==-1):
                sor=sor+" "+"|"
            else: sor=sor+str(tabla[i][j])+"|"                
        print(sor)    

def beker(xpoz:int,ypoz:int,ertek:int,tabla:list):
    if(xpoz<=9 and xpoz>=1 and ypoz<=9 and ypoz>=1 and ertek<=9 and ertek>=1):
        if(tabla[xpoz-1][ypoz-1]==-1):
            tabla[xpoz-1][ypoz-1]=ertek
        else: print("hibas pozicio")    
    else: print("add meg újra") 
    return tabla

def ures_db_szam(tabla:list):
    db=0
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if(tabla[i][j]==-1):
                db+=1
    return db            

def ellenorzes(tabla:list):
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

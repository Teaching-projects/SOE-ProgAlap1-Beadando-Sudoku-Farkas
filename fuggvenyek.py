def megjelenites(tabla:list):
    for i in range(len(tabla)):
        sor="|"
        for j in range(len(tabla)):
            if(tabla[i][j]==-1):
                sor=sor+" "+"|"
            else: sor=sor+str(tabla[i][j])+"|"                
        print(sor)    

def beker(xpoz:int,ypoz:int,ertek:int,tabla:list):
    #tupple
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


       
        
            

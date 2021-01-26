import fuggvenyek
fuggv=fuggvenyek

tabla=[[-1,6,3,1,7,4,2,5,8],[-1,7,8,3,2,5,6,4,9],[2,5,4,6,8,9,7,3,1],[8,2,1,4,3,7,5,9,6],[4,9,6,8,5,2,3,1,7],[7,3,5,9,6,1,8,2,4],[5,8,9,7,1,3,4,6,2],[3,1,7,2,4,6,9,8,5],[6,4,2,5,9,8,1,7,3]]

#első függvény teszt: megjelenítés

print("elso fuggv. teszt:")
fuggv.megjelenites(tabla)
print("teszt vege\n")

#harmadik függvény teszt: üres számlálás

print("harmadik fuggv. teszt:")
print(fuggv.ures_db_szam(tabla))
print("teszt vege\n")

#második függvény teszt: bekérés

print("masodik fuggv. teszt:")
x=int(input())
y=int(input())
szam=int(input())
fuggv.beker(x,y,szam,tabla) #jól működik, ha nem ad vissza semmilyen választ, csak befejezi a folyamatot
print("teszt vege\n")

#harmadik függvény teszt: üres számlálók 

print("harmadik fuggv. teszt:")
print(fuggv.ures_db_szam(tabla))
print("teszt vege\n")


#negyedik függvény teszt: ellenőrzés

print("negyedik fuggv. teszt:")
kesz_tabla=[[9,6,3,1,7,4,2,5,8],[1,7,8,3,2,5,6,4,9],[2,5,4,6,8,9,7,3,1],[8,2,1,4,3,7,5,9,6],[4,9,6,8,5,2,3,1,7],[7,3,5,9,6,1,8,2,4],[5,8,9,7,1,3,4,6,2],[3,1,7,2,4,6,9,8,5],[6,4,2,5,9,8,1,7,3]]
print(fuggv.ellenorzes(kesz_tabla)) #igaz, ha jól működik
print("teszt vege")
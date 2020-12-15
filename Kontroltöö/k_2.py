from random import randint

# Kirjutan funktsiooni mis arvutab  kalorid
def kalorid(a, b):
    return (a * b / 1000) * 120
print(float(kalorid(7,30))) #kontroll, kas funktsioon töötab?


# Küsime kasutajalt sisestatda andmed
raja_pikkus = int(input("Sisestage 1 basseini ots 25 või 50 m: "))

kord_arv = int(input("Sisestage kui palju korda käisite: "))


# Genereerime basseini otsad
basseiniotste_arv = []
for x in range(kord_arv):
    i = randint(30, 50)
    basseiniotste_arv.append(i)

kogu_kulumine = 0

# Arvutame ringis iga korda kalaoriate kuulumine
for y in range(len(basseiniotste_arv)):
    kulumine = kalorid(basseiniotste_arv[y], raja_pikkus)
    kogu_kulumine += kulumine
    print("Kaloreid kulus: " + str(round(kulumine, 1)))

# Arvutame kõik kaloriate kulumine antud periiodi joksul
print("Kokku kulus: "+str(round(kogu_kulumine, 1)))








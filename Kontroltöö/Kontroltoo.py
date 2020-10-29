from random import randint

fail = open("konekestused.txt", encoding="UTF-8")
konekestused = []
for rida in fail:
    konekestused.append(int(rida))
fail.close()

konemin_hind = float(input("Sisestage kõneminuti hind: "))
konede_arv = int(input("Sisestage kõnede arv: "))


konekestus = 0
while(konekestus <= 600):
    taring = randint(1, 1000)
    print(taring)
    konekestus += 60

konekestused = [210, 30, 140, 610]

if konekestus in konekestused:
    min_hind = (konemin_hind * konede_arv)
    print("Kõne maksumus: " + str(min_hind))

else:
    max_hind = (konemin_hind * 10 * konede_arv)
    print("Kõne maksumus: " + str(max_hind))






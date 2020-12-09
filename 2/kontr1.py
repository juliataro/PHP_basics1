from random import randint

#funktsioon mis defineerib kui palju tugistikud tulevad ühe nastkonnale

def inimeste_arv (naiskondade_arv, uhenaiskonna_tug):
    if naiskondade_arv < 15:
        return uhenaiskonna_tug(10)
    else:
        return uhenaiskonna_tug(8)
    return (naiskondade_arv * (22 + tugiisikute_arv))


#Küsime kasutajalt sisestad andmeid
koht = input('Sisestage finaalturniiride toimumiskoha: ')
print('Turnirid toimusid '+koht+'l')
turn_koguarv = int(input('Sisestage turniiride koguarv: '))


#genereerime naiskondade arv vastavalt sisustatud turniiri kogu arvele
naiskondade_arv = []

for x in range(turn_koguarv):
    a = randint(10, 30)
    naiskondade_arv.append(a)
print(naiskondade_arv)

# will count the sum
summa = 0
for y in naiskondade_arv:
    print('Uhevõistluskonnal on ' + str(inimeste_arv(y, uhenaiskonna_tug)))   # one competition group
    summa += y   # all competition groups

print('Inimeste kokku on ' + str(summa))







from random import randint

koht = input('Sisestage finaalturniiride toimumiskoha: ')
print('Turnirid toimusid '+koht+'l')
turn_koguarv = int(input('Sisestage turniiride koguarv: '))

def inimesi_kokku(a, b):
    inimeste_arv = a * (22 + b)
    return inimeste_arv


naiskondade_arv = []
tugiisikute_arv = 0

for x in range(turn_koguarv):
    a = randint(10, 30)
    naiskondade_arv.append(a)

    if x > 15:
        tugiisikute_arv = 10
    else:
        tugiisikute_arv = 8


one_tournir = inimesi_kokku(naiskondade_arv, tugiisikute_arv)
all_tournirs = 0
for y in naiskondade_arv:     # one competition group
    print('Turniril oli' + str(naiskondade_arv) +'ja vastavalt inimesi '+ str(one_tournir))
# all competition groups
all_tournirs += one_tournir
print('Kokku oli kõikidel turniridel: ' + str(all_tournirs))







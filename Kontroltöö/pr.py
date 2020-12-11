from random import randint

koht = input('Sisestage finaalturniiride toimumiskoha: ')
print('Turnirid toimusid '+koht+'l')
turn_koguarv = int(input('Sisestage turniiride koguarv: '))

def inimesi_kokku(naiskondade_arv, tugiisikute_arv):

    if naiskondade_arv > 15:
        return tugiisikute_arv == 10
    elif naiskondade_arv < 15:
        return tugiisikute_arv == 8
    else:
        return naiskondade_arv * (22 + tugiisikute_arv)

print(inimesi_kokku(7,8))


naiskondade_arv = []
tugiisikute_arv = 0

for a in range(turn_koguarv):
    x = randint(10, 30)
    naiskondade_arv.append(x)

inimeste_arv = naiskondade_arv * (22 + tugiisikute_arv)
naiskondade_arv.append(inimeste_arv)
all_tournirs = 0

for y in naiskondade_arv:  # one competition group
        print('Turniril oli ' + str(y) + ' ja vastavalt inimesi ' + str(inimeste_arv))

all_tournirs += inimeste_arv
print('Kokku oli kõikidel turniridel: ' + str(all_tournirs))

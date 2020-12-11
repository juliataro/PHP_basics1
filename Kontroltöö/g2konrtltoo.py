from random import randint

#kirjutame funktsiooni, mis arvutab inimesi ühes turniris
def inimeste_arv(a, b):
    return a * (22 + b)
print(inimeste_arv(7,8)) # funktsiooni toimumise kontroll


# Küsime andmeid
koht = input('Sisestage finaalturniiride toimumiskoha: ')
print('Turnirid toimusid '+koht+'l')
turn_koguarv = int(input('Sisestage turniiride koguarv: '))

#Leiame juhusliku naiskondade arvud vastavalt sisestatud turniri kogu arvule

i = turn_koguarv
kokku_turnirides = 0

while i > 0:
    naisekondade_arv = randint(10, 30)
    if naisekondade_arv < 15: #tugiisikute arvu sõltuvus juhusliku genereeritud naiskondadearvust
        tugiisikute_arv = 10
    else:
        tugiisikute_arv = 8


    # Arvutame erali tänu funktsioonile inimesi ühes turniris
    uhes_turniris = inimeste_arv(naisekondade_arv, tugiisikute_arv)
    kokku_turnirides += uhes_turniris

    # Väljastame kui palju gruppid olid ja kokku inimesi ühes turniiris
    print("Turniril oli "+str(naisekondade_arv)+' ja kokku oli turniril '+ str(uhes_turniris))
    x -= 1

#Väljastame kui palju olid inimesi vastaval kõik sisestatud turniride arvu ja genereeritud arvud
print("Kokku kõik turniirides oli "+str(kokku_turnirides))






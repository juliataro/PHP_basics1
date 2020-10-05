from random import randint

istekohta_valik = input("Kas soovite istekohta valida või loosida ?")

if istekohta_valik == 'ise':
    print("Valisite ise.")
    koht = input("Kas soovite istuda akna ääres või mitte ? ")
    if koht == 'aken':
        print("Aknakoht")
    else:
        print("Vahekäigukoht")

else:
    loos = randint(1, 3)
    if loos == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print("Istkoht loositi. Vahekäigukoht")













ringide_arv = int(input("sesesta ringide arv: "))
ringi_number = 1
porgandite_arv = 0
while(ringi_number <= ringide_arv):
    print(ringi_number)
    if(ringi_number % 2 == 0):
        porgandite_arv = porgandite_arv + ringi_number
        print("said " + str(ringi_number) + "porgandid")
        print("kokku hetkel on " + str(porgandite_arv) + "porgandid")
    ringi_number += 1
print("porgandite koguarv " + str(porgandite_arv))

soovitud =int(input("Sesestage taringude arv: "))
#viskame täringut nii kaua, kui soovitud arv viske on tehtud
#selleks paneme korrad lugema

kord = 1
while(kord <= soovitud_kord)
    #teeme vise
    taring = randint(1, 6)
    #kontrollime, kpalju tuli
    print(taring)
    #liiigume järgmisele visele
    kord += 1

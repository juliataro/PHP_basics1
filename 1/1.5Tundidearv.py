#arvud
ainepunkt = int(input("Sistege ainepunkt: "))
ainepunkti_arv = int(input("Sisestage ainepunktide arv: "))
õppiaine_pikkus = int(input("Sisestage õppimis pikkus: "))

'#arvutused'
ajakulu = (ainepunkt * ainepunkti_arv) // õppiaine_pikkus
print("Ajakulu on " + str(ajakulu))
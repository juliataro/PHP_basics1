
#Sisu
vanus = int(input("Sisestage enda vanus "))
sugu = input("Sisestage enda sugu ")
treeningu_tüüp = input("Sisestage treeningu tüüp ")

#arvestus
if sugu == 'M' or sugu == 'm':
    max_pulsisagedus = (220 - vanus)
if sugu == 'N' or sugu == 'n':
    max_pulsisagedus = 206 - (vanus / 100) * 88

if treeningu_tüüp == '1':
    puls = (max_pulsisagedus / 100) * 50 or (max_pulsisagedus / 100) * 70
    print("Pulsisagedus peab olema vahemikus " + str(puls))
if treeningu_tüüp == '2':
    puls =  puls = (max_pulsisagedus / 100) * 70 or (max_pulsisagedus / 100) * 80
    print("Pulsisagedus peab olema vahemikus " + str(puls))
if treeningu_tüüp == '3':
    puls = puls = (max_pulsisagedus / 100) * 80 or (max_pulsisagedus / 100) * 87
    print("Pulsisagedus peab olema vahemikus " + str(puls))




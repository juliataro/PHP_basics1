#arvud

inimeste_arv = int(input("Sisestage inimeste arv: "))
kohad_bussis = int(input("Sesestage kohtade arv bussis: "))


#arvutused

inimeste_arv_ühes_bussis = (inimeste_arv / kohad_bussis)
print(int(inimeste_arv_ühes_bussis))

busside_arvu_mahtunud_inimeste_arvu = (inimeste_arv // kohad_bussis)
print(int(busside_arvu_mahtunud_inimeste_arvu))

mahajäänud_inimeste_arvu = (inimeste_arv % kohad_bussis)
print(int(mahajäänud_inimeste_arvu))



nimi = input("Sisesta Leedu Perekonnanimi")
nimi_lõpp = nimi[-2:]
print(nimi_lõpp)
#abielus
if(nimi[-2:] == "ne"):
    print("abiellus")
elif(nimi[-2:] =="te"):
    print("vallaline")
elif(nimi[-1:] == "e" and (nimi[-2:] != "te") or (nimi[-2:] != "te")):
    print("märamata")
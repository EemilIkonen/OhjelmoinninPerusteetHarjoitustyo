"""
Tekijä: Eemil Ikonen
Ryhmä:TTV20S2
Tehtävä Harjoitustyö
Kuvaus:

Ohjelma on salasanageneraattori johon käyttäjä syöttää salasanan pituuden ja siinä käytettävät merkit. 
Tämän jälkeen ohjelma luo salasanan jonka se tallentaa tiedostoon
"""

from random import randint
import string

#
#Eri merkit suoraan stringistä
#
pienetkirjaimet = string.ascii_lowercase
isotkirjaimet = string.ascii_uppercase
numerot = string.digits
merkit = string.punctuation

#
#Eri arvojen asettaminen
#
salasananmerkit = []
salasana = ""

#
#Ohjeiden tulostus
#
print("Tervetuloa käyttämään Salasanageneraattoria!")
print("Tämä ohjelma kysyy sinulta minkälaisen salasanan haluat luoda ja tallentaa sen tiedostoon nimeltä salasana.txt")
print("Jos haluat vastata kysymykseen kyllä vastaa y, jos haluat vastata ei vastaa n")
print("")
print("Tekijä: Eemil Ikonen")
print("")


#
#Tässä määritetään salasanan pituus
#
while True:
    try:
        pituus = int(input("Syötä haluamasi salasanan pituus kokonaislukuna välillä 8-30: "))
        if 8 <= pituus <= 30:
            break
        else:
             print("Syöttämäsi arvo ei ollut väliltä 8-30! Syötä arvo uudelleen")
    except ValueError:
        print("Syöttämäsi arvo ei ollut kokonaisluku")


#
#Tässä määritetään salasanassa käytettävät merkit
#
while True:
    while True:
        pienet = str(input("Käytetäänkö salasanassa pieniä kirjaimia? [y/n]: "))
        if pienet == "y" or pienet == "Y":
            pieniakirjaimia = 1
            break
        elif pienet == "n" or pienet == "N":
            pieniakirjaimia = 0
            break
        else:
            print("Syöttämäsi arvo ei ollut y tai n! Syötä arvo uudelleen")

    while True:
        isoja = str(input("Käytetäänkö salasanassa isoja kirjaimia? [y/n]: "))
        if isoja == "y" or isoja == "Y":
            isojakirjaimia = 1
            break
        elif isoja == "n" or isoja == "N":
            isojakirjaimia = 0
            break
        else:
            print("Syöttämäsi arvo ei ollut y tai n! Syötä arvo uudelleen")

    while True:
        merkkeja = str(input("Käytetäänkö salasanassa erikoismerkkejä? [y/n]: "))
        if merkkeja == "y" or merkkeja == "Y":
            merkkeja = 1
            break
        elif merkkeja == "n" or merkkeja == "N":
            merkkeja = 0
            break
        else:
            print("Syöttämäsi arvo ei ollut y tai n! Syötä arvo uudelleen")

    while True:
        numeroja = str(input("Käytetäänkö salasanassa numeroita? [y/n]: "))
        if numeroja == "y" or numeroja == "Y":
            numeroita = 1
            break
        elif numeroja == "n" or numeroja == "N":
            numeroita = 0
            break
        else:
            print("Syöttämäsi arvo ei ollut y tai n! Syötä arvo uudelleen")

    if pieniakirjaimia == 0 and isojakirjaimia == 0 and numeroita == 0 and merkkeja == 0:
        print("Sinun pitää valita vähintään yhdet merkit! Vastaa kysymyksiin uusiksi")
    else:
        break

#
#Tässä luodaan salasana
#
while True:
    if len(salasananmerkit) == pituus:
            break
        
    mikavalitaan = randint(1,4)

    while True:

        if mikavalitaan == 1:
            if pieniakirjaimia == 1:
                merkinmaaritys = randint(1, 26)
                salasananmerkit.append(pienetkirjaimet[merkinmaaritys-1])
                break
            else:
                break
        
        elif mikavalitaan == 2:
            if isojakirjaimia == 1:
                merkinmaaritys = randint(1, 26)
                salasananmerkit.append(isotkirjaimet[merkinmaaritys-1])
                break
            else:
                break
            
        elif mikavalitaan == 3:
            if merkkeja == 1:
                merkinmaaritys = randint(1, 32)
                salasananmerkit.append(merkit[merkinmaaritys-1])
                break
            else:
                break

        elif mikavalitaan == 4:
            if numeroita == 1:
                merkinmaaritys = randint(1, 10)
                salasananmerkit.append(numerot[merkinmaaritys-1])
                break
            else:
                break

#
#Tässä tallennetaan salasana tiedostoon
#
try:
    for i in salasananmerkit:
        salasana += i 
    
    file = open("exercises/Harkkatyo/salasana.txt", "a")
    file.write(salasana + "\n")
    file.close()
    print("Salasana on nyt tallennettu tiedostoon salasana.txt alimmalle riville")
except:
    print("Odottamaton virhe tapahtui! Kokeile käynnistää ohjelma uudelleen")

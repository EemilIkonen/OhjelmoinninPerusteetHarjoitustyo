"""
Tekijä: Eemil Ikonen
Ryhmä:TTV20S2
Tehtävä Harjoitustyö
Kuvaus:

Ohjelma on salasanageneraattori johon käyttäjä syöttää salasanan pituuden ja siinä käytettävät merkit. 
Tämän jälkeen ohjelma luo salasanan jonka se tallentaa tiedostoon

Toteutus on hieman kömpleö koska ohjelmaan on lisätty aliohjelmat ja luokat jälkikäteen. 
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
#Ohjeiden tulostus
#
print("Tervetuloa käyttämään Salasanageneraattoria!")
print("Ohjelma kysyy sinulta ensin montako salasanaa haluat luoda")
print("Tämän jälkeen ohjelma kysyy sinulta minkälaisen salasanan haluat luoda ja tallentaa sen tiedostoon nimeltä salasana.txt")
print("Tämän jälkeen ohjelma kysyy sinulta samat asiat niin monta kertaa kun olet valinnut salasanoja luotavan")
print("Jos haluat vastata kysymykseen kyllä vastaa y, jos haluat vastata ei vastaa n")
print("")
print("Tekijä: Eemil Ikonen")
print("")

def salasanageneraattori(montako):

    #
    #Luodaan luokka joka pitää sisällään tiedot salasanasta
    #
    class Merkit:
        kirjaimetpienet = ""
        kirjaimetisot = ""
        erikoismerkit = ""
        numeroita = ""
        salasananpituus = ""

    salasanantiedot = Merkit()

    #
    #Eri arvojen asettaminen
    #
    salasananmerkit = []
    salasana = ""

    for x in range(montako):

        #
        #Tässä määritetään salasanan pituus
        #
        while True:
            try:
                salasanantiedot.salasananpituus = int(input("Syötä salasanan {} pituus kokonaislukuna välillä 8-30: ".format(x+1)))
                if 8 <= salasanantiedot.salasananpituus <= 30:
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
                pienet = str(input("Käytetäänkö salasanassa {} pieniä kirjaimia? [y/n]: ".format(x+1)))
                if pienet == "y" or pienet == "Y":
                    salasanantiedot.kirjaimetpienet = 1
                    break
                elif pienet == "n" or pienet == "N":
                    salasanantiedot.kirjaimetpienet = 0
                    break
                else:
                    print("Syöttämäsi arvo ei ollut y tai n! Syötä arvo uudelleen")

            while True:
                isoja = str(input("Käytetäänkö salasanassa {} isoja kirjaimia? [y/n]: ".format(x+1)))
                if isoja == "y" or isoja == "Y":
                    salasanantiedot.kirjaimetisot = 1
                    break
                elif isoja == "n" or isoja == "N":
                    salasanantiedot.kirjaimetisot = 0
                    break
                else:
                    print("Syöttämäsi arvo ei ollut y tai n! Syötä arvo uudelleen")

            while True:
                merkkeja = str(input("Käytetäänkö salasanassa {} erikoismerkkejä? [y/n]: ".format(x+1)))
                if merkkeja == "y" or merkkeja == "Y":
                    salasanantiedot.erikoismerkit = 1
                    break
                elif merkkeja == "n" or merkkeja == "N":
                    salasanantiedot.erikoismerkit = 0
                    break
                else:
                    print("Syöttämäsi arvo ei ollut y tai n! Syötä arvo uudelleen")

            while True:
                numeroja = str(input("Käytetäänkö salasanassa {} numeroita? [y/n]: ".format(x+1)))
                if numeroja == "y" or numeroja == "Y":
                    salasanantiedot.numeroita = 1
                    break
                elif numeroja == "n" or numeroja == "N":
                    salasanantiedot.numeroita = 0
                    break
                else:
                    print("Syöttämäsi arvo ei ollut y tai n! Syötä arvo uudelleen")

            if salasanantiedot.kirjaimetpienet == 0 and salasanantiedot.kirjaimetisot == 0 and salasanantiedot.numeroita == 0 and salasanantiedot.erikoismerkit == 0:
                print("Sinun pitää valita vähintään yhdet merkit! Vastaa kysymyksiin uusiksi")
            else:
                break

        #
        #Tässä luodaan salasana
        #
        while True:
            if len(salasananmerkit) == salasanantiedot.salasananpituus:
                    break
                
            mikavalitaan = randint(1,4)

            while True:

                if mikavalitaan == 1:
                    if salasanantiedot.kirjaimetpienet == 1:
                        merkinmaaritys = randint(1, 26)
                        salasananmerkit.append(pienetkirjaimet[merkinmaaritys-1])
                        break
                    else:
                        break
                
                elif mikavalitaan == 2:
                    if salasanantiedot.kirjaimetisot == 1:
                        merkinmaaritys = randint(1, 26)
                        salasananmerkit.append(isotkirjaimet[merkinmaaritys-1])
                        break
                    else:
                        break
                    
                elif mikavalitaan == 3:
                    if salasanantiedot.erikoismerkit == 1:
                        merkinmaaritys = randint(1, 32)
                        salasananmerkit.append(merkit[merkinmaaritys-1])
                        break
                    else:
                        break

                elif mikavalitaan == 4:
                    if salasanantiedot.numeroita == 1:
                        merkinmaaritys = randint(1, 10)
                        salasananmerkit.append(numerot[merkinmaaritys-1])
                        break
                    else:
                        break

        #
        #Tässä tallennetaan salasana tiedostoon ja tyhjennetään muuttujat
        #
        try:
            for i in salasananmerkit:
                salasana += i 
            
            file = open("salasana.txt", "a")
            file.write(salasana + "\n")
            file.close()
            print("Salasana {} on nyt tallennettu tiedostoon salasana.txt alimmalle riville".format(x+1))
            salasana = ""
            salasananmerkit.clear()
        except:
            print("Odottamaton virhe tapahtui! Kokeile käynnistää ohjelma uudelleen")



#
#Tässä päätetään montako salasanaa luodaan
#
while True:
    try:
        montako = int(input("Montako salasanaa haluat luoda? (1-10): "))
        if 1 <= montako <= 10:
            break
        else:
            print("Syöttämäsi arvo ei ollut 1-10")
    except:
        print("Jokin meni vikaan, yritä uudelleen")

#
#Tässä kutsutaan salasanageneraattoria
#

salasanageneraattori(montako)

# Nummer Raad Spel:

import random

def nummer_raad_spel():
    lager_nummer = 1
    hoger_nummer = 100
    geheim_nummer = random.randint(lager_nummer, hoger_nummer)
    max_pogingen = 10
    aantal_pogingen = 0

#De speler heeft 10 pogingen om het nummer te raden
    
    print("nummer raad spel :-")
    print(f"raad een nummer tussen {lager_nummer} en {hoger_nummer}. Je hebt {max_pogingen} pogingen.")

# spel loopt
    while aantal_pogingen < max_pogingen:
        gok = input("voer je gok in: ")   #vraag de speler om een getal in te voeren
        if not gok.isdigit():
            print("voer een geldig getal in")  #controleer of de gok een geldig nummer is
            continue
        gok = int(gok)  #zet de input nom naar een integer
        aantal_pogingen += 1

        if gok < geheim_nummer:   #geef hints op de basis van de gok
         print("hoger!")
        elif gok > geheim_nummer:
         print("lager!")
        else:
            print(f"gefeliciteerd! je hebt het nummer geraden in {aantal_pogingen} pogingen")
            return

    # Als het nummer niet geraden is
    print(f"helaas!het juiste nummer was{geheim_nummer}. probeer het opnieuw!") 



# Dagboek:

import json       #(JAVAScript Object Nation)
import os         #controleren van bestanden


# Wachtwoord instellen
wachtwoord = "1234"

def controleer_wachtwoord():
    ingevoerd_wachtwoord = input("Voer het wachtwoord in: ")
    if ingevoerd_wachtwoord == wachtwoord:
        return True
    else: 
        print("Wachtwoord is niet correct.")
        return False

# Dagboek invoer
def voeg_invoer_toe(datum, tekst):
    dagboek_data = laad_dagboek()
    if datum in dagboek_data:
        keuze = input(f"Er bestaat al een invoer voor {datum}. Wil je tekst herschrijven? (ja / nee): ")
        if keuze.lower() != "ja":
            return

    dagboek_data[datum] = tekst
    opslaan_dagboek(dagboek_data)
    print(f"Invoer voor {datum} toegevoegd! ")

# Tekst opvragen voor een specifieke datum
def lees_invoer(datum):
    dagboek_data = laad_dagboek()
    if datum in dagboek_data:
        print(f"Invoer voor {datum}: {dagboek_data[datum]}")
    else:
        print(f"Geen invoer gevonden voor {datum}. ")

    
# Tekst bewerken
def bewerk_invoer(datum):
    dagboek_data = laad_dagboek()
    if datum in dagboek_data:
        print(f"Huidig invoer voor {datum}: {dagboek_data[datum]}")
        nieuwe_tekst = input("Voer een nieuwe tekst in: ")
        dagboek_data[datum] = nieuwe_tekst
        opslaan_dagboek(dagboek_data)
        print(f"Invoer voor {datum} bijgewerkt! ")
    else:
        print("Geen invoer gevonden voor {datum}.")

# Laad het dagboekbestand
def laad_dagboek():
    if not os.path.exists("dagboek.json"):
        return{}
    with open ("dagboek.json", "r") as f:
        return json.load(f)

# Sla het dagboekbestand op
def opslaan_dagboek(dagboek_data):
    with open("dagboek.json", "w") as f:
        json.dump(dagboek_data, f, indent=4)

# Dagboek menu
def dagboek_menu():
    if not controleer_wachtwoord():
        return

    while True:
        print("\n ---Dagboek---")
        print("1. Voeg je nieuwe invoer toe: ")
        print("2. Lees je invoer--")
        print("3. Bewerk je invoer--")
        print("4. --Stop--")

        keuze = input("Kies een optie (1. 2. 3. 4.): ")

        if keuze == "1":
            datum = input("Voer een datum in (bijv. 2024-10-13): ")
            tekst = input("Voer je invoer in: ")
            voeg_invoer_toe(datum, tekst)
        elif keuze == "2":
            datum = input("Voor welke datum wil je invoer lezen? voer een datum in. bijv. (2024-10-13): ")
            lees_invoer(datum)
        elif keuze == "3":
            datum = input("Voor welke datum wil je de invoer bewerken? voer een datum in. bijv. (2024-10-13): ")
            bewerk_invoer(datum)
        elif keuze == "4":
            print("Uw dagboek app is afgesloten.")
            return
        else:
            print("Ongeldig keuze, probeer opnieuw alstublieft.")

# Start dagboek
    dagboek_menu()



# Rekenmachine:

def rekenmachine():

   nummer1 = float(input("Voer het eerste nummer in: "))
   nummer2 = float(input("Voer het tweede nummer in: "))
   operatie = input("Kies een bewerking (+ , - , * , / ): ")   # Een optie kiezen


    

# Reken en toen resultaat
   if operatie == "+":
      print("Resultaat:", nummer1 + nummer2)
   elif operatie == "-":
      print("Resultaat:", nummer1 - nummer2)
   elif operatie == "*":
      print("Resultaat:", nummer1 * nummer2)
   elif operatie == "/":
     if nummer2 != 0:
        print("Resultaat:", nummer1 / nummer2)
     else:
        ("kan niet door nul delen, sorry!")
   else:
    print("Ongeldige bewerking.")



# Vakantie Opties:

def vakantie_opties():
    vakantie_opties = {
     "Afrika": ["1 Marokko--", "2 Kaapverdie--", "3 Egypte--"],
     "Europa": ["1 Netherland--", "2 Zwitserland--", "3 Spanje--"],
     "Azie": ["1 Japan--", "2 Thailand--", "3 India--"],
     "Noord-Amerika": ["1 Canada--", "2 verenigde staten--", "3 Mexico--"],
     "Zuid-Amerika": ["1 Brazilie--", "2 Argentinie--", "3 Peru--"],
     "Antarctica": ["N/A"],
     "Australie": ["1 Australie--", "2 Nieuw-Zeeland--", "3 Fiji--"]
  }

# Gebruiker kiest een continent
    continent = input("Kies een continent waar je graag op vakantie willen gaan: Afrika, Europa, Azie, Noord-Amerika, Zuid-Amerika, Antarctica, Australie:  ")

# Toen drie Top landen van de continent
    if continent in vakantie_opties:
     print("Top drie beste landen in dit continent om te bezoeken:", ",".join(vakantie_opties[continent]))
    else:
     print("Voer een geldig continent naam in.")


# HET KEUZE MENU::::::::::--------------------------------------

def main_menu():
    print("Welkom bij IntroVerse_Hub!")
    while True:
        print("\n1. ----Nummer Raad Spel----")
        print("2. ----Dagboek----")
        print("3. ----Rekenmachine----")
        print("4. ----Vakantie Opties----")
        print("5. ----Afsluiten----")

        keuze = input("Kies een optie...:  ")

        if keuze == "1":
            nummer_raad_spel()
        elif keuze == "2":
            dagboek_menu()
        elif keuze == "3":
            rekenmachine()
        elif keuze == "4":
            vakantie_opties()
        elif keuze == "5":
            print("introVerse_Hub afgesloten, 'we wensen je een heel mooie dag verder!")
            break
        else:
            print("Ongeldig keuze, kies opnieuw alstublieft...")

# Start het programma
main_menu()



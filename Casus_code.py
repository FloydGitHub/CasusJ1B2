def kiezen_gebruiker(keuze = False):
    if keuze == False:
        keuze = input("Kies een rol (organisator/presentator/bezoeker): ").lower()
    gebruiker = ["organisator", "presentator", "bezoeker"]
    try:            
        if keuze in gebruiker:
            return (f"{keuze.capitalize()}")
        else:
            raise ValueError
    except:
        return ("Ongeldige keuze. Kies uit: organisator, presentator of bezoeker.")
 #input meegeven aan unittest

def functies_organisator(keuze_organisator = False):
    if keuze_organisator == False:
        keuze_organisator = input("Kies een functie (presentaie invoegen/planning bekijken/planning verwijderen/presentatie verwijderen/terug): ").lower()
    functies = ["presentaie invoegen", "planning bekijken","planning verwijderen", "presentatie verwijderen", "terug"]
    try:
        if keuze_organisator in functies:
            return (f"{keuze_organisator.capitalize()}")
        else:
            raise ValueError
    except:
        return ("Ongeldige keuze. Kies uit: presentaie invoegen, planning bekijken, planning verwijderen, presentatie verwijderen of terug.")
    
def functies_presentator(keuze_presentator = False):
    if keuze_presentator == False:
        keuze_presentator = input("Kies een functie (presentatie aanpassen/presentatie anuleren/terug): ").lower()
    functies = ["presentatie aanpassen", "presentatie anuleren", "terug"]
    try:
        if keuze_presentator in functies:
            return (f"{keuze_presentator.capitalize()}")
        else:
            raise ValueError
    except:
        return ("Ongeldige keuze. Kies uit: presentatie aanpassen, presentatie anuleren, of terug.")
    

def functies_bezoeker(keuze_bezoeker = False):
    if keuze_bezoeker == False:
        keuze_bezoeker = input("Kies een functie (persoonlijke planning bekijken/inschrijven presentatie/uitschrijven presentatie/terug.").lower()
    functies = ["persoonlijke planning bekijken", "inschrijven presentatie", "uitschrijven presentatie", "terug"]
    try:
        if keuze_bezoeker in functies:
            return (f"{keuze_bezoeker.capitalize()}")
        else:
            raise ValueError
    except:
        return ("Ongeldige keuze. Kies uit: persoonlijke planning bekijken, inschrijven presentatie, uitschrijven presentatie of terug.")
    
def WatAanpassenPresentator(Wat_Aanpassen = False):
    if Wat_Aanpassen == False:
        Wat_Aanpassen = input("Kies wat je wil aanpassen (naam, eindtijd, beschrijving, benodigdheden)").lower()
    functies = ["naam", "eindtijd", "beschrijving", "benodigdheden", "terug"]
    try:
        if Wat_Aanpassen in functies:
            return (f"{Wat_Aanpassen.capitalize()}")
        else:
            raise ValueError
    except:
        return ("Ongeldige keuze. Kies uit: naam, eindtijd, beschrijving, benodigdheden of terug.")
    
    
    
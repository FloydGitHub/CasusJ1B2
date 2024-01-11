import Casus_code

keuze = False
gebruiker = Casus_code.kiezen_gebruiker()

if gebruiker == 'Organisator':
    #functies van organisator
    functie_organisator = Casus_code.functies_organisator()
elif gebruiker == 'Presentator':
    #functies van presenattor
    functie_presentator = Casus_code.functies_presentator()

else:
    #functies van bezoeker
    functiebezoeker = Casus_code.functies_bezoeker()
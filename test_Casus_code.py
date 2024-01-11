import pytest
from Casus_code import *

test001=[
    ('organisator','Organisator'),
    ('presentator', 'Presentator'),
    ('bezoeker', 'Bezoeker'),
    (5, 'Ongeldige keuze. Kies uit: organisator, presentator of bezoeker.'),
    ]

@pytest.mark.parametrize('a,resultaat', test001)
def test_kiezen_gebruiker(a,resultaat):
    assert kiezen_gebruiker(a) == resultaat

test002=[
    ('presentaie invoegen', 'Presentaie invoegen'),
    ('planning bekijken', 'Planning bekijken'),
    ('planning verwijderen', 'Planning verwijderen'),
    ('presentatie verwijderen', 'Presentatie verwijderen'),
    ('terug', 'Terug'),
    ('p', 'Ongeldige keuze. Kies uit: presentaie invoegen, planning bekijken, planning verwijderen, presentatie verwijderen of terug.'),
    ]

@pytest.mark.parametrize('a,resultaat', test002)
def test_functies_organisator(a,resultaat):
    assert functies_organisator(a) == resultaat

test003=[
    ('presentatie aanpassen', 'Presentatie aanpassen'),
    ('presentatie anuleren', 'Presentatie anuleren'),
    ('terug', 'Terug'),
    (99, 'Ongeldige keuze. Kies uit: presentatie aanpassen, presentatie anuleren, of terug.')
    ]

@pytest.mark.parametrize('a,resultaat', test003)
def test_functies_presentator(a,resultaat):
    assert functies_presentator(a) == resultaat

test004=[
    ('persoonlijke planning bekijken', 'Persoonlijke planning bekijken'),
    ('inschrijven presentatie', 'Inschrijven presentatie'),
    ('uitschrijven presentatie', 'Uitschrijven presentatie'),
    ('terug', 'Terug'),
    (69, 'Ongeldige keuze. Kies uit: persoonlijke planning bekijken, inschrijven presentatie, uitschrijven presentatie of terug.')
    ]

@pytest.mark.parametrize('a,resultaat', test004)
def test_functies_bezoeker(a,resultaat):
    assert functies_bezoeker(a) == resultaat

test005=[
    ('naam', 'Naam'),
    ('eindtijd', 'Eindtijd'),
    ('beschrijving', 'Beschrijving'),
    ('benodigdheden', 'Benodigdheden'),
    ('terug', 'Terug'),
    ('Olifant', 'Ongeldige keuze. Kies uit: naam, eindtijd, beschrijving, benodigdheden of terug.')
    ]

@pytest.mark.parametrize('a,resultaat', test005)
def test_WatAanpassenPresentator(a,resultaat):
    assert WatAanpassenPresentator(a) == resultaat
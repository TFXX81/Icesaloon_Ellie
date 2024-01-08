#importeer vraag 12
from algemene_functies import mijn_functie_2

#de functie aanbieding vraag5
def aanbieding_1(smaak, prijs, korting):
    korting_bedrag = prijs*korting
    nieuwe_prijs = prijs - korting_bedrag
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

smaak = "aardbei"
prijs = 4
korting = 0.1

resultaat = aanbieding_1(smaak, prijs, korting)
print(resultaat)
#de functie inkomsten totaal vraag 6 + 7
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    totaal_met_btw = totaal + btw_bedrag
    uitkomst = f"het totaal van alle inkomsten van deze week is {totaal_met_btw} euro, waarover {btw_bedrag} euro btw dient betaald te worden."
    return uitkomst

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09

uitkomst = inkomsten_totaal(inkomsten_per_dag, btw_percentage)
print (uitkomst)

#de functie laag en hoog vraag 8
def laag_en_hoog(mijn_lijst):
    laagste = min (mijn_lijst)
    hoogste = max (mijn_lijst)
    return [laagste, hoogste]

inkomsten_per_dag = [200, 430, 125, 160, 205, 90, 345]
laag_hoog = laag_en_hoog(inkomsten_per_dag)
print (laag_hoog)

#de functie gemiddelde vraag 9 + 10
def gemiddelde(mijn_lijst):
    som = sum(mijn_lijst)
    aantal_elementen = len (mijn_lijst)
    gemiddelde_waarde = som/aantal_elementen
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde} euro."

inkomsten_per_dag = [200, 430, 125, 160, 205, 90, 345]
resultaat = gemiddelde(inkomsten_per_dag)
print (resultaat)

#de functie meervoudig
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
mijn_invoerlijst = [10, 5, 3, 2, 1, 2, 9]
resultaat_meervoudig= meervoudig(mijn_invoerlijst)
print (resultaat_meervoudig)

#vervolg vraag 12
def combinatie (invoer_lijst_2):
    korte_lijst = laag_en_hoog (invoer_lijst_2)
    resultaat_combinatie = mijn_functie_2(korte_lijst)
    return resultaat_combinatie

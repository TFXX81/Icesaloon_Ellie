from helper import decoreer

def print_aanbiedingen():
    prijzen={
        "aardbei" : 3 ,
        "vanille" : 4 ,
        "chocolade" : 5
    }

    aanbieding = (prijzen["aardbei"]*0.8)

    reclame_tekst = (f"Vandaag in de aanbieding: vanille ijs, 1 liter - slechts € {aanbieding}")

    reclame_tekst2 = reclame_tekst[:63]

    reclame_tekst3 = reclame_tekst2.upper()

    reclame_tekst4 = reclame_tekst3.split()

    mijn_string = reclame_tekst4
    for el in mijn_string:
        lengte_string = len (mijn_string)
        if lengte_string <5:
            print (el.lower())
        else:
            print (el.upper())

decoreer("aanbieding")
print_aanbiedingen()
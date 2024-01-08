def mijn_functie_1(a):
      return a ** 2
a=4
resultaat= mijn_functie_1(a)
print (resultaat)

def mijn_functie_2(a,b):
      som = a+b
      verschil = a-b
      product = a*b
      quotiënt = a/b
      return[som, verschil, product, quotiënt]
teruggeefwaardes = mijn_functie_2 (12,3)
print (teruggeefwaardes)
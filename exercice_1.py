largeur = float(input("largeur : "))
longeur = float(input("longeur : "))
profondeur = float(input("profondeur : "))
poids = float(input("poids : "))

volume = largeur * longeur * profondeur

lourd = poids > 30
encombrant = volume > 1000

if encombrant and lourd :
    print("rejeté")
elif not encombrant and not lourd:
    print("standard")
else:
    print("spécial")
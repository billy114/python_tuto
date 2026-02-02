largeur = float(input("Largeur : "))
longueur = float(input("Longueur : "))
profondeur = float(input("Profondeur : "))
poids = float(input("Poids : "))

# Calcul du volume
volume = largeur * longueur * profondeur

# Critères
lourd = poids > 30
encombrant = volume > 1000

# Classification du colis
if encombrant and lourd:
    print("Rejeté")
elif not encombrant and not lourd:
    print("Standard")
else:
    print("Spécial")
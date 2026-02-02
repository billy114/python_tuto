# ======================================
# SÉANCE 2 — LISTES & BOUCLES
# ======================================

# --------------------------------------
# MANIPULATION DES LISTES
# --------------------------------------

numbers = [10, 16, 33, 40, 33]

print(len(numbers))        # nombre d’éléments
print(numbers[1])          # accès par index

# Ajouter un élément à la fin
numbers.append(88)
print(numbers)

# Insérer un élément à un index précis
numbers.insert(2, 50)
print(numbers)

# Supprimer une valeur (première occurrence)
numbers.remove(33)
print("Après remove :", numbers)

# Supprimer une valeur seulement si elle existe
val = 40
if val in numbers:
    numbers.remove(val)
print(numbers)

# Supprimer le dernier élément
numbers.pop()
print(numbers)

# Supprimer un élément par index
numbers.pop(1)
print(numbers)

# Fonctions intégrées
print(sum(numbers))
print(min(numbers))
print(max(numbers))


# --------------------------------------
# BOUCLE FOR AVEC CONDITIONS
# --------------------------------------

days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

for day in days:
    if day in ["Samedi", "Dimanche"]:
        print("Week-end")
    else:
        print(day)


# --------------------------------------
# BOUCLE FOR AVEC range
# --------------------------------------

for i in range(1, 5):
    print("Bonjour :", i)


# --------------------------------------
# BOUCLE WHILE — SUPPRESSION MULTIPLE
# --------------------------------------

tab = [11, 44, 55, 3, 44]
val_a_supprimer = 44

while val_a_supprimer in tab:
    tab.remove(val_a_supprimer)

print(tab)


# --------------------------------------
# BOUCLE WHILE CLASSIQUE
# --------------------------------------

i = 0
while i < len(tab):
    print("On est dans la boucle")
    i += 1

print("Sortie de la boucle")


# --------------------------------------
# LISTE MIXTE ET TYPE DES ÉLÉMENTS
# --------------------------------------

tab_mix = [12, "Bleu", True]

for val in tab_mix:
    print(f"{val} est de type {type(val)}")


# --------------------------------------
# PARCOURIR UNE LISTE À L’ENVERS
# --------------------------------------

i = len(days) - 1
while i >= 0:
    print(days[i])
    i -= 1
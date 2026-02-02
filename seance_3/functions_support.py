# ==================================
# LES FONCTIONS
# ==================================

# ----------------------------------
# 1 - Fonction sans paramètre
# ----------------------------------
def show_menu():
    print("Bienvenue dans le menu, veuillez choisir une option")
    print("1 - Créer un utilisateur")
    print("2 - Modifier un utilisateur")
    print("3 - Supprimer un utilisateur")

# Appel de la fonction
show_menu()

# ----------------------------------
# 2 - Fonction avec paramètre (sans return)
# ----------------------------------
def greet(name):
    print("Salut " + name)

greet("Billel")
greet("David")

# ----------------------------------
# 3 - Fonction avec paramètre (calcul simple)
# ----------------------------------
def square(number):
    print(number * number)

square(4)

# ----------------------------------
# 4 - Fonction avec paramètre et return
# ----------------------------------
def square_2(number):
    result = number * number
    return result

print(square_2(4))

# ----------------------------------
# 5 - Fonction qui retourne un booléen
# ----------------------------------
def is_major(age):
    if age >= 18:
        return True
    else:
        return False

if is_major(20):
    print("Vous pouvez entrer")
else:
    print("Vous ne pouvez pas entrer")


# ----------------------------------
# 6 - Fonction avec plusieurs paramètres
# ----------------------------------
def add(x, y):
    return x + y

print(add(3, 5))

# ----------------------------------
# 7 - Fonction qui retourne une chaîne
# ----------------------------------
def full_name(firstname, lastname):
    return firstname + " " + lastname

firstname = "Billel"
lastname = "ABBES"
print("Salut " + full_name(firstname, lastname))


# ----------------------------------
# 8 - Fonction avec un tableau en paramètre
# ----------------------------------
def sum_table(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

table = [1, 10, 13]
print(sum_table(table))


# ----------------------------------
# 9 - Fonction sans return (affichage)
# ----------------------------------

def min_max(numbers):
    print("Le maximum est :", max(numbers))
    print("Le minimum est :", min(numbers))

min_max(table)

# ----------------------------------
# 10 - Fonction qui retourne plusieurs valeurs
# ----------------------------------
def min_max_2(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


tab_1 = [1, 3, 77, 55]
tab_2 = [33, 12, 55, 55]

minimum_tab_2, maximum_tab_2 = min_max_2(tab_2)
print("Minimum :", minimum_tab_2)
print("Maximum :", maximum_tab_2)

# ----------------------------------
# 11 - Fonction qui découpe un nom complet et retourne le prénom et le nom.
# ----------------------------------
def cut_full_name(fullname):
    words = fullname.split()

    firstname = words[0]
    lastname = words[1]

    return firstname, lastname


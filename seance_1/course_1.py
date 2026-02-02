# ======================================
# Programmation en Python — Séance 1
# ======================================

"""
Ceci est un commentaire
sur plusieurs lignes.
Il peut servir de documentation.
"""

# -------------------------------------
# 1 - Les variables et les types
# -------------------------------------

my_number = 10          # int : nombre entier
my_float = 3.14         # float : nombre décimal
my_str = "On est en cours de Python"  # str : chaîne de caractères
my_bool = True          # bool : vrai / faux

print(my_number)
print(my_float)
print(my_str)
print(my_bool)

print(type(my_number))
print(type(my_float))
print(type(my_str))
print(type(my_bool))


# -------------------------------------
# 2 - Les opérations
# -------------------------------------

a = 10
b = 3

# Opérations arithmétiques
print(a + b)    # addition
print(a - b)    # soustraction
print(a * b)    # multiplication
print(a / b)    # division
print(a // b)   # division entière
print(a % b)    # modulo

# Opérations de comparaison
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

my_number = 12
my_string = "12"
print(my_number == my_string)  # False (types différents)


# -------------------------------------
# 3 - Les opérateurs logiques
# -------------------------------------

print(not False)
print(False or True)
print(True and False)
print(True or (False and True))


# -------------------------------------
# 4 - Les conditions
# -------------------------------------

if a == b:
    print("a est égal à b")
    print("On est dans le if")
else:
    print("a n'est pas égal à b")
    print("On est dans le else")

print("Fin de la condition")


# -------------------------------------
# 5 - Entrées utilisateur (input)
# -------------------------------------

firstname = input("Prénom : ")
age = input("Âge : ")

print(type(age))          # str

converted_age = int(age)
print(type(converted_age))  # int

print("Le prénom est :", firstname)
print("Fin du programme")


# -------------------------------------
# 6 - Chaînes de caractères (str)
# -------------------------------------

first_name = "Billel"
last_name = "ABBES"
full_name = first_name + " " + last_name
print(full_name)

message = "Bonjour " + first_name
print(message)

age = 30
message = f"Je m'appelle {full_name} et j'ai {age} ans"
print(message)

message = f"La somme de 1 + 1 = {1 + 1}"
print(message)

print(f"True or False est : {True or False}")

text = "On est en cours de Python"

# Longueur
print(len(text))

# Accès aux caractères et sous-chaînes
print(text[-1])
print(text[18:25])
print(text[:7])
print(text[18:])
print(text[-6:])
print(text[:3])

# Vérifier la présence d'un mot
print("Python" in text)

# Transformations
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

# Vérifications
print(text.isupper())
#======================================
# Programmation en Python
#======================================
"""
Ceci c'est un commentaire
sur plusieurs lignes
"""

#-------------------------------------
# 1 - Les variables et les types
#--------------------------------------

my_number = 10
my_float = 3.14
my_str = "On est en cours de python"
my_bool = True

print(my_number)
print(my_float)
print(my_str)
print(my_bool)

print(type(my_number))
print(type(my_float))
print(type(my_str))
print(type(my_bool))

#-------------------------------------
# 2 - Les opération
#--------------------------------------

a = 10
b = 3

# Les opération arithmétiques

print(a + b) # addition
print(a - b) # soustraction
print(a * b) # multiplication
print(a / b) # divsion
print(a // b) # divsion arrondi
print(a % b) # modulo

# Les opération de comparaison
print(a == b) # égale : il faut avoir la même valeur et le même type
print(a > b) # supérieur
print(a < b) # inferieur
print(a >= b) # superieur ou égal
print(a <= b) # inférieur ou égal

my_number = 12
my_string = "12"
print(my_number == my_string) # False

# Opération de logique
print("Les Opérations de logique")
print(not False)
print(False or True)
print(True and False)
print(True or (False and True))

#-------------------------------------
# 2 - Les conditions
#--------------------------------------

if a == b:
    print("a est egal b")
    print("on est dans le if")
else:
    print("a n'est pas egal à b")
    print("on est dans le else")
print("fin de condition")

firstname = input("firstname : ")

age = input("age : ")
print(type(age))
converted_age = int(age)
print(type(converted_age))

print("le prénom est : " + firstname)
print("fin de programme")

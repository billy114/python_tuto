# on analyse le mot de passe
# le mot de passe doit avoit plus de 8 caractères
# il doit contenir au moins un majuscule, un miniscule, une lettre et un chiffre
password = input("Entrez votre mot de passe : ")

has_upper = False
has_lower = False
has_digit = False
has_alpha = False

for c in password:
    if c.isupper():
        has_upper = True
    if c.islower():
        has_lower = True
    if c.isalpha():
        has_alpha = True
    if c.isdigit():
        has_digit = True

if len(password) < 8:
    print("Mot de passe doit avoir plus de 8 caractères")

elif not has_upper:
    print("il doit contenir au moins un majuscule")
elif not has_lower:
    print("il doit contenir au moins un miniscule")
elif not has_alpha:
    print("il doit contenir au moins une lettre")
elif not has_digit:
    print("il doit contenir au moins un chiffre")
else:
    print("Mot de passe accepté")


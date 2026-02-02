# Analyse du mot de passe
# Règles :
# - au moins 8 caractères
# - au moins une majuscule
# - au moins une minuscule
# - au moins une lettre
# - au moins un chiffre

password = input("Entrez votre mot de passe : ")

has_upper = False
has_lower = False
has_digit = False
has_alpha = False

# Parcours du mot de passe caractère par caractère
for c in password:
    if c.isupper():
        has_upper = True
    if c.islower():
        has_lower = True
    if c.isalpha():
        has_alpha = True
    if c.isdigit():
        has_digit = True

# Vérifications
if len(password) < 8:
    print("Le mot de passe doit contenir au moins 8 caractères")
elif not has_upper:
    print("Le mot de passe doit contenir au moins une majuscule")
elif not has_lower:
    print("Le mot de passe doit contenir au moins une minuscule")
elif not has_alpha:
    print("Le mot de passe doit contenir au moins une lettre")
elif not has_digit:
    print("Le mot de passe doit contenir au moins un chiffre")
else:
    print("Mot de passe accepté")
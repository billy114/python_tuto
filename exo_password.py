# on analyse le mot de passe
# le mot de passe doit avoit plus de 8 caractères
# il doit contenir au moins un majuscule, un miniscule, une lettre et un chiffre
password = input("Entrez votre mot de passe : ")

if len(password) < 8:
    print("Mot de passe doit avoir plus de 8 caractères")
elif password.islower():
    print("il doit contenir au moins un majuscule")
elif password.isupper():
    print("il doit contenir au moins un miniscule")
elif password.isdigit():
    print("il doit contenir au moins une lettre")
elif password.isalpha():
    print("il doit contenir au moins un chiffre")
else:
    print("Mot de passe accepté")


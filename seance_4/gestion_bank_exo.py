def menu():
    print("Veuillez choisir une option : ")
    print("1 - Créer un compte bancaire")
    print("2 - clôturer un compte bancaire")
    print("3 - Faire un dépôt d'argent")
    print("4 - Faire un retrait d'argent")
    print("5 - Faire un virement bancaire")
    print("6 - Afficher tous les comptes")
    print("7 - Afficher le solde d'un compte")
    print("8 - quitter")
    return int(input("Votre choix : "))

compte_1 = {
    "id" : 4,
    "name" : "David",
    "sold" : 1200,
    "status" : "actif"
}

compte_2 = {
    "id" : 3,
    "name" : "Marine",
    "sold" : 700,
    "status" : "actif"
}

comptes = [compte_1, compte_2]

def create_account():
    id = int(input("id : "))
    name = input("name : ")
    compte = {
        "id" : id,
        "name" : name,
        "sold" : 0,
        "status" : "actif"
    }
    comptes.append(compte)
    print("Compte créé avec succes")

def close_account():
    id = int(input("id : "))
    is_found = False
    for compte in comptes:
        if compte["id"] == id:
            compte["status"] = "inactif"
            is_found = True
            break

    if not is_found:
        print("compte introuvable")


def deposit():
    print("on cloture un compte")

def withdraw():
    print("on cloture un compte")

def transfert():
    print("on cloture un compte")

def show_accounts():
    print(comptes)

def show_sold():
    id = int(input("id : "))
    is_found = False
    for compte in comptes:
        if compte["id"] == id:
            print(compte["sold"])
            is_found = True
            break

    if not is_found:
        print("compte introuvable")

while True:
    choice = menu()
    if choice == 1 :
        create_account()
    elif choice == 2 :
        close_account()
    elif choice == 3 :
        deposit()
    elif choice == 4 :
        withdraw()
    elif choice == 5 :
        transfert()
    elif choice == 6 :
        show_accounts()
    elif choice == 7 :
        show_sold()
    elif choice == 8:
        break
    else:
        print("Choix invalid")


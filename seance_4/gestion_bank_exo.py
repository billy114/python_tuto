def menu():
    print("Veuillez choisir une option : ")
    print("1 - Créer un compte bancaire")
    print("2 - clôturer un compte bancaire")
    print("3 - Faire un dépôt d'argent")
    print("4 - Faire un retrait d'argent")
    print("5 - Faire un virement bancaire")
    print("6 - quitter")
    return int(input("Votre choix : "))

def create_account():
    print("on crée un compte")

def close_account():
    print("on cloture un compte")

def deposit():
    print("on cloture un compte")

def withdraw():
    print("on cloture un compte")

def transfert():
    print("on cloture un compte")

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
    elif choice == 6:
        break
    else:
        print("Choix invalid")


# 📝 Exercice — Traitement d’une commande.
# Écrivez une fonction calcul_price qui prend en paramètres :
# 	•	une quantité
# 	•	un prix unitaire
# La fonction doit retourner :
# 	•	"Commande invalide" si la quantité ou le prix est inférieur ou égal à 0
# 	•	le montant total de la commande avec :
# 	•	une remise de 10 % si la quantité est supérieure ou égale à 10
# 👉 La fonction doit retourner le résultat à l’aide de return.

def calcul_price (price, quantity):
    if quantity <= 0 or price <= 0:
        return "Commande invalide"

    total = price * quantity
    if quantity >= 10 :
        remise = total * 0.1
        return total - remise

    return total

def is_major (age):
    if age >= 18:
        return  True

    return False

print(calcul_price(12, 3))
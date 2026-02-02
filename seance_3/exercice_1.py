def cut_full_name (fullname):
    words = fullname.split()
    firstname = words[0]
    lastname = words [1]
    return firstname, lastname

# 📝 Exercice — Traitement d’une commande.
# Écrivez une fonction calcul_price qui prend en paramètres :
# 	•	une quantité
# 	•	un prix unitaire
# La fonction doit retourner :
# 	•	"Commande invalide" si la quantité ou le prix est inférieur ou égal à 0
# 	•	le montant total de la commande avec :
# 	•	une remise de 10 % si la quantité est supérieure ou égale à 10
# 👉 La fonction doit retourner le résultat à l’aide de return.
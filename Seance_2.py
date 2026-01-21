# from statistics import median
#
# numbers = [10, 16, 33, 40, 33]
# print(len(numbers))
# print(numbers[1])
# # append
# numbers.append(88)
# print(numbers)
# # insert
# numbers.insert(2, 50)
# print(numbers)
# # remove
# numbers.remove(33)
# print("Après le remove : ")
# print(numbers)
#
# val = 40
# if val in numbers:
#     numbers.remove(val)
# print(numbers)
# # pop
# numbers.pop()
# print(numbers)
#
# numbers.pop(1)
# print(numbers)
#
# #
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# print(median(numbers))

days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
for day in days:
    if day in ["Samedi", "Dimanche"]:
        print("Week end")
    else:
        print(day)

for var in range(1,5):
    print("Bonjour : " + str(var))

tab = [11, 44, 55, 3, 44] # --> [11, 55, 3]
val_a_supprimer = 44
while val_a_supprimer in tab:
    tab.remove(val_a_supprimer)
print(tab)

i = 0
while i < len(tab):
    print("on est dans la boucle")
    i += 1
print("sort de la boucle")

tab_mix = [12, "Bleu", True]
for val in tab_mix:
    print(f"{val} est de type : {type(val)}")
# 12 de type int
# "Blue de type str

i = len(days) - 1
while i >= 0:
    print(days[i])
    i -= 1 # i = i - 1


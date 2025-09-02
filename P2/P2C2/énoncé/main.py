nombres = input("Saisissez une liste de nombres, séparés par des virgules (ex : 1,2,3,4,5) : ")

liste = nombres.split(",")
resultat = 0
valide = 0
superieur = 0

for nombre in liste:
    if str.isnumeric(nombre):
        resultat += int(nombre)
        valide += 1

moyenne = round(resultat / valide, 2)

for nombre in liste:
    if str.isnumeric(nombre) and int(nombre) > moyenne:
        superieur += 1

print(f"La somme des nombres saisis est égale à {resultat}")
print(f"La moyenne des nombres saisis est égale à {moyenne}")
print(f"Nombre de nombres saisis supérieurs à la moyenne : {superieur}")
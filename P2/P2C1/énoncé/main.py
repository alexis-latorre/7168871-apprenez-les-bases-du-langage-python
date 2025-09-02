operations = ("-", "+", "*", "/")

nombre1 = input("Entrez une valeur pour le premier nombre : ")
nombre2 = input("Entrez une valeur pour le deuxième nombre : ")

if not str.isnumeric(nombre1) or not str.isnumeric(nombre2):
    raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("Quelle opération voulez-vous effectuer (+, -, * ou /) ? ")

if not operation in operations:
    raise SystemExit("Fin du programme")

match operation:
    case "+": 
        resultat = nombre1 + nombre2
    case "-":
        resultat = nombre1 - nombre2
    case "*":
        resultat = nombre1 * nombre2
    case "/":
        if nombre2 == 0:
            raise SystemExit("Fin du programme")            
        resultat = round(nombre1 / nombre2, 2)

print(resultat)
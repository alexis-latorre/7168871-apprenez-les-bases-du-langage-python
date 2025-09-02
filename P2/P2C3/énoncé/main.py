def salaire_mensuel(salaire_annuel):
    return round(salaire_annuel / 12, 2)

def salaire_hebdomadaire(salaire_mensuel):
    return round(salaire_mensuel / 4, 2)

def salaire_journalier(salaire_hebdomadaire):
    return round(salaire_hebdomadaire / 5, 2)

def salaire_horaire(salaire_hebdomadaire, heures_travailles):
    return round(salaire_hebdomadaire / heures_travailles, 2)

annuel = round(int(input("Saisissez votre salaire annuel : ")) * 0.766, 2)
heures = float(input("Saisissez votre temps de travail par semaine (en heures) : "))

mensuel = salaire_mensuel(annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
journalier = salaire_journalier(hebdomadaire)
horaire = salaire_horaire(hebdomadaire, heures)

print(f"Votre salaire mensuel est de {mensuel} €")
print(f"Votre salaire hebdomadaire est de {hebdomadaire} €")
print(f"Votre salaire journalier est de {journalier} €")
print(f"Votre salaire horaire est de {horaire} €")
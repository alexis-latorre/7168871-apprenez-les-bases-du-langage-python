from boite_a_outils import BoiteAOutils
from marteau import Marteau
from tournevis import Tournevis

boite = BoiteAOutils()

marteauNoir = Marteau()
marteauRouge = Marteau()
marteauRouge.peindre('rouge')
marteauRouge.couleur = 'bleu'

tournevis = Tournevis(10)

boite.ajouter_outil(marteauRouge)
boite.ajouter_outil(tournevis)
boite.ajouter_outil(marteauNoir)
boite.retirer_outil(tournevis)
boite.ajouter_outil(tournevis)

print(boite)
print(boite.outils)
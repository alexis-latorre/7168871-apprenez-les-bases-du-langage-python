from outil import Outil

class Marteau(Outil):
    def __init__(self):
        super().__init__('marteau')
        self.couleur = 'noir'

    def peindre(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur
        print(f"Le marteau a été peint en {self.couleur}")

    def __repr__(self):
        return f"Marteau {self.couleur}"
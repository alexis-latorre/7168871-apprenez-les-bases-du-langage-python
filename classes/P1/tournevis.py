from outil import Outil

class Tournevis(Outil):
    def __init__(self, taille = 0):
        super().__init__('tournevis')
        self.taille = taille

    def serrer():
        print('serrer')

    def desserrer():
        print('desserrer')

    def __repr__(self):
        return f"Tournevis de {self.taille} mm"
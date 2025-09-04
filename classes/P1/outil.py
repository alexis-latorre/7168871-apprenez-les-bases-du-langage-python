class Outil:
    def __init__(self, name):
        self.name = name
        print(f"Création d'un outil de type {self.name}")
    
    def __repr__(self):
        return self.name
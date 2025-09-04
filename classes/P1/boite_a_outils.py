class BoiteAOutils:
    outils = []

    def ajouter_outil(self, outil):
        self.outils.append(outil)

    def retirer_outil(self, outil):
        self.outils.remove(outil)

    def __repr__(self):
        return f"Nombre d'outils dans la boîte : {len(self.outils)}"
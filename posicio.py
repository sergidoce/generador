class Posicio:

    def __init__(self, assig, grup):
        
        self.assig = assig
        self.grup = grup

    def print_posicio(self):
        print(self.assig + self.grup)

    def get_grupo(self):
        return self.grup

    def get_assig(self):
        return self.assig
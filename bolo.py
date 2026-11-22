from produto import Produto

class Bolo(Produto):
    def __init__(self, nome, preco, kg):
        super().__init__(nome, preco)
        self.__kg = None
        self.kg = kg

    @property
    def kg(self):
        return self.__kg
    @kg.setter
    def kg(self, peso):
        if peso > 0:
            self.__kg = peso
        else:
            raise ValueError("Informe um peso válido.")
    def calcular_preco(self):
        return (self.preco) + (0.30*self.__kg)

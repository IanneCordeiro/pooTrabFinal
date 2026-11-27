from produto import Produto

class Doce(Produto):
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
        return self.preco + (0.15*self.__kg)
    def __str__(self):
        return f"{self.nome} | R$ {self.preco:.2f} | Peso: {self.kg} kg"

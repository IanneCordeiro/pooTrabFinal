from produto import Produto

class KitEvento(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.__tamanho = None
        self.tamanho = tamanho

    @property
    def tamanho(self):
        return self.__tamanho
    @tamanho.setter
    def tamanho(self, tmn):
        if self.tmn == "pequeno" or self.tmn == "medio" or self.tmn == "grande":
            self.__tamanho = tmn
        else:
            print("Informe um tamanho disponivel.")
        
    def calcular_preco(self):
        if self.__tamanho == "pequeno":
            return (self.preco)
        if self.__tamanho == "medio":
            return (self.preco) + 15
        if self.__tamanho == "grande":
            return (self.preco) + 30

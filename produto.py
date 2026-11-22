from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome, preco):
        self.__nome = None
        self.__preco = None
        self.nome = nome   
        self.preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, name):
        if not name.strip():
            raise ValueError("O nome do produto deve ser preenchido.")
        else:
            self.__nome = name

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preço deve ser um valor positivo.")
        else:
            self.__preco = valor

    @abstractmethod
    def calcular_preco(self, quantidade):
       pass

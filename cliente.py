from pedidoinvaliderror import PedidoInvalidoError

class Cliente:
    def __init__(self, nome, contato):
        self.__nome = None
        self.__contato = None
        self.__historico_pedido = []

        self.nome = nome
        self.contato = contato

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self.__nome = nome

    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, contato):
        if not contato.strip():
            raise ValueError("O contato não pode ficar vazio.")
        self.__contato = contato

    @property
    def historico_pedido(self):
        return list(self.__historico_pedido)

    def adicionar_pedido(self, novo_pedido):
        if novo_pedido is None:
            raise PedidoInvalidoError("O pedido não pode ser vazio.")

        self.__historico_pedido.append(novo_pedido)

    def __str__(self):
        return f"{self.nome} | Contato: {self.contato}"

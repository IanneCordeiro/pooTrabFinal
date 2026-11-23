from produto import Produto
from pedidoInvalidoError import PedidoInvalidoError

class Cliente(Produto):
    def __init__(self, nome, contato):
        super().__init__(nome)
        self.contato = contato
        self.historico_pedido = []

    def adicionar_pedido(self, novo_pedido):
        if novo_pedido.strip() < 1:
            raise PedidoInvalidoError("O pedido não pode ta vazio")
        else:
            self.historico_pedido.append(novo_pedido)
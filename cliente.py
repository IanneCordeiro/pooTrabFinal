from pedidoInvalidoError import PedidoInvalidoError
class Cliente():
    def __init__(self, nome, contato):
        self.nome = nome)
        self.contato = contato
        self.historico_pedido = []

    def adicionar_pedido(self, novo_pedido):
        if novo_pedido.strip() < 1:
            raise PedidoInvalidoError("O pedido não pode ta vazio")
        else:
            self.historico_pedido.append(novo_pedido)

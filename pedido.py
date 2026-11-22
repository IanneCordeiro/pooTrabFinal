from produto import Produto
from pedidoinvaliderror import PedidoInvalidoError
class Pedido:
    def __init__(self, cliente=None):
        self.__cliente = cliente
        self.__itens = []
        self.__status = False

    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status

    def adicionar_item(self, produto, quantidade):
        if self.__status: #aqui ele testa se é true
            raise ValueError("O pedido já foi finalizado.")

        if not isinstance(produto, Produto): #funcao que testa se existe dentro de uma classe, victor nao ensinou
            raise PedidoInvalidoError("O item deve ser um produto válido.")

        if quantidade <= 0:
            raise PedidoInvalidoError("A quantidade deve ser positiva.")
        self.__itens.append((produto, quantidade))

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.__itens:
            total += produto.calcular_preco() * quantidade
        return total

    def finalizar_pedido(self):
        if not self.__itens:
            raise ValueError("O pedido está vazio.")
        self.__status = True

    def exibir_pedido(self):
    print("---- PEDIDO ----")
    print(f"Cliente: {self.__cliente}")
    for produto, quantidade in self.__itens:
        subtotal = produto.calcular_preco() * quantidade
        print(f"Produto: {produto.nome} - Quantidade: {quantidade}")
        print(f"Preço unitário: R$ {produto.calcular_preco():.2f}")
    print(f"TOTAL: R$ {self.calcular_total():.2f}")
    if self.__status:
        print("Status: Finalizado")
    else:
        print("Status: Em aberto")


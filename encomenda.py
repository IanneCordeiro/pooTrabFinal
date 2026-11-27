from pedido import Pedido
from produto import Produto
from pedidoinvaliderror import PedidoInvalidoError
class Encomenda(Pedido):
    def __init__(self, cliente):
        super().__init__(cliente)
#def calcular
#def mudar status
#adicionar item
    def calcular(self):
        total = 0
        for produto, quantidade in self.__itens:
            total += produto.calcular_preco() * quantidade
        return total


    def adicionar_item(self, produto, quantidade):
        if self.status == "Finalizado":
            raise ValueError("A encomenda já foi concluída.")

        if not isinstance(produto, Produto):
            raise PedidoInvalidoError("Item inexistente.")

        if quantidade <= 0:
            raise PedidoInvalidoError("Quantidade inválida.")

        super().adicionar_item(produto, quantidade)

    def __str__(self):
        return f"Encomenda | Cliente: {self.cliente.nome} | Status: {self.status} | Total: R$ {self.calcular_total():.2f}"

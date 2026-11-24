from pedido import Pedido
from produto import Produto
from pedidoinvaliderror import PedidoInvalidoError
class Encomenda(Pedido):
    def __init__(self, cliente):
        super().__init__(self, cliente)
#def calcular
#def mudar status
#adicionar item
    def calcular(self):
        total = 0
        for produto, quantidade in self.__itens:
            total += produto.calcular_preco() * quantidade
        return total

    def mudar_status(self, situacao):
        if len(self.__itens) < 1:
            raise PedidoInvalidoError("O pedido nâo pode estar vazio.")
        if situacao in ("Pendente", "Finalizado", "Cancelado"):
            self.__status = situacao

    def adicionar_item(self, produto, quantidade):
        if self.__status == "Finalizado":
            raise ValueError("O pedido já foi concluido")
        if not isinstance(produto, Produto): 
            raise PedidoInvalidoError("Item inexistente")
        if quantidade <= 1:
            raise PedidoInvalidoError("Quantidade invalida")
        self.__itens.append((produto, quantidade))

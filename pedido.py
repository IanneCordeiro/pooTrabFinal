from produto import Produto
from pedidoinvaliderror import PedidoInvalidoError
class Pedido:
    def __init__(self, cliente=None):
        self.__cliente = cliente
        self.__itens = []
        self.__status = "Pendente"

    @property
    def itens(self):
        return list(self.__itens)
    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, situacao):
        if situacao in ("Pendente", "Finalizado", "Cancelado"):
            self.__status = situacao
        else:
            raise PedidoInvalidoError("Situação inválida.")

    def adicionar_item(self, produto, quantidade):
        if self.__status == "Finalizado":
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
        self.__status = "Finalizado"
    
    def exibir_pedido(self):
        print("---- PEDIDO ----")
        print(f"Cliente: {self.__cliente}")
        for produto, quantidade in self.__itens:
            print(f"Produto: {produto.nome} - Quantidade: {quantidade}")
            print(f"Preço unitário: R$ {produto.calcular_preco():.2f}")
        print(f"TOTAL: R$ {self.calcular_total():.2f}")
        print(f"Situação: {self.__status}")

    def cancelar_pedido(self):
        if self.__status == "Finalizado":
            print("Não é possível cancelar esse pedido")
        else:
            self.__status = "Cancelado"

    def mudar_status(self, situacao):
        if not self.__itens:
            raise PedidoInvalidoError("O pedido não pode estar vazio.")

        if situacao not in ("Pendente", "Finalizado", "Cancelado"):
            raise PedidoInvalidoError("Situação inválida.")

        self.__status = situacao

    def __str__(self):
        texto = "---- PEDIDO ----\n"
        texto += f"Cliente: {self.__cliente}\n"

        for produto, quantidade in self.__itens:
            texto += f"Produto: {produto.nome} - Quantidade: {quantidade}\n"
            texto += f"Preço unitário: R$ {produto.calcular_preco():.2f}\n"
            texto += f"Subtotal: R$ {produto.calcular_preco() * quantidade:.2f}\n"

        texto += f"TOTAL: R$ {self.calcular_total():.2f}\n"
        texto += f"Situação: {self.__status}"

        return texto




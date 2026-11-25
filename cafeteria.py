
from produto import Produto
from pedidoinvaliderror import PedidoInvalidoError
from pedido import Pedido
from cliente import Cliente
from encomenda import Encomenda

class Cafeteria:
    def __init__(self):
        self.__produtos = []
        self.__clientes = []
        self.__pedidos = []
        self.__encomendas = []

    @property
    def produtos(self):
        return list(self.__produtos)
    @property
    def clientes(self):
        return list(self.__clientes)
    @property
    def pedidos(self):
        return list(self.__pedidos)
    @property
    def encomendas(self):
        return list(self.__encomendas)

    def cadastrar_produto(self, produto):
        if not isinstance(produto, Produto):
            raise PedidoInvalidoError("Produto inválido.")
        else:
            self.__produtos.append(produto)
            print("Produto cadastrado com sucesso!")

    def cadastrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise ValueError("Cliente inválido.")
        else:
            self.__clientes.append(cliente)
            print("Cliente cadastrado com sucesso!")

    def buscar_cliente(self, nome):
        for cliente in self.__clientes:
            if cliente.nome.strip().lower() == nome.strip().lower():
                return cliente
        else:
            raise ValueError( "Cliente não encontrado")

    def buscar_produto(self, nome):
        for produto in self.__produtos:
            if produto.nome.strip().lower() == nome.strip().lower():
                return produto
        else:
            raise ValueError( "Produto não encontrado")

    def realizar_pedido(self, pedido):
        if not isinstance(pedido, Pedido):
            raise PedidoInvalidoError("Pedido inválido.")
        if len(pedido.itens) == 0:
            raise PedidoInvalidoError("O pedido precisa ter pelo menos um item.")
        self.__pedidos.append(pedido)

    def registrar_encomenda(self, encomenda):
        if len(encomenda.itens) == 0:
            raise PedidoInvalidoError("A encomenda precisa ter pelo menos um item.")
        else:
            self.__encomendas.append(encomenda)
            encomenda.cliente.adicionar_pedido(encomenda)

    def encomendas_pendentes(self):
        resultado = []
        for encomenda in self.__encomendas:
            if encomenda.status == "Pendente":
                resultado.append(encomenda)
        return resultado

    def historico_do_cliente(self, nome):
        cliente = self.buscar_cliente(nome)
        if cliente is None:
            raise ValueError("cliente não localizado no banco de dados.")
        return cliente.historico_pedido

    def faturamento_total(self):
        total = 0
        for pedido in self.__pedidos + self.__encomendas:
            total += pedido.calcular_total()
        return total

    def listar_produtos(self):
        print("\n--- Produtos cadastrados ---")
        if len(self.__produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self.__produtos:
                print(produto)

    def listar_clientes(self):
        print("\n--- Clientes cadastrados ---")
        if len(self.__clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.__clientes:
                print(cliente)

    def listar_pedidos(self):
        print("\n--- Pedidos cadastrados ---")
        if len(self.__pedidos) == 0:
            print("Nenhum pedido cadastrado.")
        else:
            for pedido in self.__pedidos:
                print(pedido)

    def listar_encomendas(self):
        print("\n--- Encomendas cadastradas ---")
        if len(self.__encomendas) == 0:
            print("Nenhuma encomenda cadastrada.")
        else:
            for encomenda in self.__encomendas:
                print(encomenda)

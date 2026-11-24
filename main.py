from bolo import Bolo
from cafe import Cafe
#from cafeteria import Cafeteria
from cliente import Cliente
from doce import Doce
from encomenda import Encomenda
from kit_evento import KitEvento
from pedido import Pedido
from pedidoinvaliderror import PedidoInvalidoError
from produto import Produto

doce_codigo = Cafeteria()
#adicionando os produtos do cardapio (bolo, cafe, doce e kitevento)
doce_codigo.adicionar_produto("Bolo")
doce_codigo.adicionar_produto("Doce")
doce_codigo.adicionar_produto("Cafe")
doce_codigo.adicionar_produto("KitEvento")

#adicionar pedido


#adicionando cliente 
cliente1 = "Julia", "51 99987-6543"
doce_codigo.adicionar_cliente(cliente1)


from cafeteria import Cafeteria
from cliente import Cliente
from cafe import Cafe
from doce import Doce
from bolo import Bolo
from kit_evento import KitEvento
from pedido import Pedido
from pedidoinvaliderror import PedidoInvalidoError
from encomenda import Encomenda
from cadastroerro import CadastroDuplicadoError

cafeteria = Cafeteria()

def menu(cafeteria):
    while True:
        print("\n------ DOCE CÓDIGO ------")
        print("0 - Criar pedido (crie um cliente antes)")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar produto")
        print("3 - Criar encomenda")
        print("4 - Listar clientes")
        print("5 - Listar produtos")
        print("6 - Buscar cliente")
        print("7 - Buscar produto")
        print("8 - Listar pedidos")
        print("9 - Listar encomendas")
        print("10 - Listar encomendas pendentes")
        print("11 - Consultar histórico de cliente")
        print("12 - Consultar faturamento total")
        print("13 - Sair")

        opcao = input("\nEscolha uma opção: ")
        try:
            if opcao == "0":
                print("\n--- CRIAR PEDIDO ---")
                nome = input("Digite o nome do cliente: ")

                try:
                    cliente = cafeteria.buscar_cliente(nome)
                    pedido = Pedido(cliente)

                    while True:
                        print("\n--- CARDÁPIO ---")
                        contador = 1

                        for produto in cafeteria.produtos:
                            print(f"{contador} - {produto}")
                            contador += 1

                        print("0 - Finalizar pedido")
                        escolha = input("\nEscolha o número do produto: ")

                        if escolha == "0":
                            break

                        if not escolha.isdigit():
                            print("Digite um número válido.")
                            continue

                        escolha = int(escolha)

                        if escolha < 1 or escolha > len(cafeteria.produtos):
                            print("Opção inválida.")
                            continue

                        produto = cafeteria.produtos[escolha - 1]
                        quantidade = int(input("Digite a quantidade: "))
                        pedido.adicionar_item(produto, quantidade)

                    cafeteria.realizar_pedido(pedido)
                    print("Pedido cadastrado com sucesso!")
                    print(f"Total: R$ {pedido.calcular_total():.2f}")

                except ValueError as erro:
                    print(f"Não foi possível criar o pedido: {erro}")

            elif opcao == "1":
                nome = input("Digite o nome do cliente: ")
                contato = input("Digite o contato do cliente: ")

                cliente = Cliente(nome, contato)
                cafeteria.cadastrar_cliente(cliente)

            elif opcao == "2":
                print("\n--- CADASTRAR PRODUTO ---")
                print("1 - Bolo")
                print("2 - Doce")
                print("3 - Café")
                print("4 - Kit Evento")

                tipo = input("Escolha o tipo de produto: ")

                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))

                if tipo == "1":
                    kg = float(input("Digite o peso em kg: "))
                    produto = Bolo(nome, preco, kg)

                elif tipo == "2":
                    kg = float(input("Digite o peso em kg: "))
                    produto = Doce(nome, preco, kg)

                elif tipo == "3":
                    tamanho = input("Digite o tamanho: ")
                    produto = Cafe(nome, preco, tamanho)

                elif tipo == "4":
                    tamanho = input("Digite o tamanho: ")
                    produto = KitEvento(nome, preco, tamanho)

                else:
                    print("Tipo inválido!")
                    continue

                cafeteria.cadastrar_produto(produto)

            elif opcao == "3":
                print("\n--- CRIAR ENCOMENDA ---")
                nome = input("Digite o nome do cliente: ")

                cliente = cafeteria.buscar_cliente(nome)
                encomenda = cafeteria.criar_encomenda(cliente)

                while True:
                    print("\n--- CARDÁPIO ---")
                    contador = 1

                    for produto in cafeteria.produtos:
                        print(f"{contador} - {produto}")
                        contador += 1

                    print("0 - Finalizar encomenda")
                    escolha = input("\nEscolha o número do produto: ")

                    if escolha == "0":
                        break

                    if not escolha.isdigit():
                        print("Digite um número válido.")
                        continue

                    escolha = int(escolha)

                    if escolha < 1 or escolha > len(cafeteria.produtos):
                        print("Opção inválida.")
                        continue

                    produto = cafeteria.produtos[escolha - 1]
                    quantidade = int(input("Digite a quantidade: "))
                    encomenda.adicionar_item(produto, quantidade)

                cafeteria.registrar_encomenda(encomenda)
                print("Encomenda cadastrada com sucesso!")
                print(encomenda)

            elif opcao == "4":
                cafeteria.listar_clientes()

            elif opcao == "5":
                cafeteria.listar_produtos()

            elif opcao == "6":
                nome = input("Digite o nome do cliente: ")
                cliente = cafeteria.buscar_cliente(nome)
                print(cliente)

            elif opcao == "7":
                nome = input("Digite o nome do produto: ")
                produto = cafeteria.buscar_produto(nome)
                print(produto)

            elif opcao == "8":
                cafeteria.listar_pedidos()

            elif opcao == "9":
                cafeteria.listar_encomendas()

            elif opcao == "10":
                encomendas = cafeteria.encomendas_pendentes()
                print("\n--- ENCOMENDAS PENDENTES ---")

                if len(encomendas) == 0:
                    print("Não existem encomendas pendentes.")
                else:
                    for encomenda in encomendas:
                        print(encomenda)

            elif opcao == "11":
                nome = input("Digite o nome do cliente: ")
                historico = cafeteria.historico_do_cliente(nome)

                print("\n--- HISTÓRICO DO CLIENTE ---")

                if len(historico) == 0:
                    print("Esse cliente não possui pedidos.")
                else:
                    for pedido in historico:
                        print(pedido)

            elif opcao == "12":
                total = cafeteria.faturamento_total()
                print(f"\nFaturamento total: R$ {total:.2f}")

            elif opcao == "13":
                print("Obrigado por visitar a Doce Código!")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except CadastroDuplicadoError as erro:
            print(f"Erro no cadastro: {erro}")

        except PedidoInvalidoError as erro:
            print(f"Erro no pedido: {erro}")

        except ValueError as erro:
            print(f"Valor inválido: {erro}")

        except TypeError as erro:
            print(f"Tipo de dado inválido: {erro}")

        except Exception as erro:
            print(f"Ocorreu um erro: {erro}")

# cardapio
bolo = Bolo("Bolo de cenoura", 60.00, 2.0)
doce = Doce("Brigadeiro", 3.50, 0.1)
cafe = Cafe("Cappuccino", 9.50, "medio")
kit = KitEvento("Kit festa 200 pessoas", 450.90, "pequeno")
cafeteria.cadastrar_produto(bolo)
cafeteria.cadastrar_produto(doce)
cafeteria.cadastrar_produto(cafe)
cafeteria.cadastrar_produto(kit)
# cliente
cliente1 = Cliente("Julia", "51 99987-6543")
cafeteria.cadastrar_cliente(cliente1)
# pedido
pedido1 = Pedido(cliente1)

# produtos do pedido
pedido1.adicionar_item(cafe, 2)
pedido1.adicionar_item(doce, 4)

# Registra o pedido
cafeteria.realizar_pedido(pedido1)

#encomenda
encomenda1 = Encomenda(cliente1)
encomenda1.adicionar_item(bolo, 1)
encomenda1.adicionar_item(doce, 10)
cafeteria.registrar_encomenda(encomenda1)

encomenda2 = Encomenda(cliente1)
encomenda2.adicionar_item(kit, 1)
encomenda2.adicionar_item(cafe, 5)
cafeteria.registrar_encomenda(encomenda2)
encomenda2.mudar_status("Finalizado")

#tem algum erro na encomenda, vou tentar reolver no fds

print("\n--- TESTE DE BUSCA DE PRODUTO ---")
cafeteria.listar_produtos()

print("---- Teste busca de produto ----")
print("Busca:", cafeteria.buscar_produto("Bolo de cenoura"))
menu(cafeteria)

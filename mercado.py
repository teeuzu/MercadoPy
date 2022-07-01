from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

# Menu de opções
def menu() -> None:
    print('\n')
    print('==============================')
    print('======= Bem-vindo(a) =========')
    print('======== Rio Market ==========')
    print('==============================')
    print('\n')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Produto')
    print('6 - Sair do sistema')

    opcao: int = int(input())
    
    # Redirecionando a opção para a função desejada
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida!')
        sleep(1)
        menu()

    # Cadastrando Produto
def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    # Adicionando produtos dentro do sistema
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

    # Listando Produtos
def listar_produtos() -> None:
    if len(produtos) > 0: # Se a quantidade de produtos cadastrados forem maior que o vazio (0), retorne a impressão com cada produto
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('-------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()

    # Comprando produtos cadastrados que foram cadastrados
def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('=================== Produtos Disponíveis =====================')
        for produto in produtos:
            print(produto)
            print('----------------------------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        # Verificando se este item no carrinho já foi inserido
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False # usando uma variável auxiliar 
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1 # Inserindo a quantidade do produto no carrinho
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho: # Caso o produto adicionado não tenha sido inserido no carrinho, a sua unidade será inserida
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()

# Visualizando os ítens que estão no carrinho
def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)

    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

# Fechando pedido
def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}') # Valor total a ser pago
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

    # Pegando produto através do código cadastrado
def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()


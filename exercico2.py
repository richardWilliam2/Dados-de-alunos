produtos = {}

def cadastro_produto():
    codigo = input("Digite o codigo: ")
    nome = input("Digite o nome do produto: ")
    Preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade:"))
    produtos[codigo]={'nome': nome, 'preço':Preco, 'quantidade':quantidade}
    print("Seu produto foi cadastrado")
    print(produtos)

def alterar_preco():

    novo_preco = float(input("Digite o novo preço: "))
    codigo = input("Entre o codigo do produto")
    if(codigo in produtos):
        produtos[codigo]['preco'] = novo_preco
        print("Preço alterado !")

def pesquisar_codigo():
    codigo = input("Codigo do produto: ")
    produtosenco = produtos.get(codigo)
    if produtosenco:
        print("Produto encontrado")
        print(produtosenco)


while(True):

    print("\nMenu: ")
    print("1-adicionar produto")
    print("2-Alterar preço produto")
    print("3-pesquisa por codigo")
    print("4-Sair")
    print("###########################")


    opcao=int(input("Escolha uma opção:  "))
    if(opcao == 1):
        cadastro_produto()
    elif(opcao == 2):
        alterar_preco()
    elif(opcao == 3):
        pesquisar_codigo()
    elif(opcao == 4):
        break
    else:
        print("Escolha a opção correta")


produtos = {}

i = 3
while True:
    codigo = input("Digite o codigo: ")
    nome = input("Digite o nome do produto: ")
    Preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade:"))
    produtos[codigo]={'nome': nome, 'preço':Preco, 'quantidade':quantidade}
    print("Seu produto foi cadastrado")
    print(produtos)
    
    i+=3


    opcao = int(input("1- adicionar prod. 0-Não adicionar prod. : "))
    if(opcao==0):
        print(produtos)
        break
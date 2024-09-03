dados = {}

def Aluno():
    nome = input("Digite o nome: ")
    data_nasc = input("Digite a data de nascimento: ")
    email = input("Digite o email: ")
    telef = float(input("Digite a telefone:"))
    endereco = input("Digite o Indereço:")
    dados[nome]={ 'data_de_nascimento':data_nasc, 'E-Mail':email, 'endereço':endereco}
    print("Seu Aluno foi cadastrado")
    print(dados)

def Aluno_pesquisado():
    nome = input("Pesquisar aluno: ")
    Alunop = Alunop.get(nome)
    if Alunop:
        print("Produto encontrado")
        print(dados)

def Tod_aluno():
    print(dados)

def alt_ender():
    novo_endereco = input("Digite o novo endereço: ")
    nome = input("entre no aluno?: ")
    if(nome in dados):
        dados[nome]['endereço'] = novo_endereco
        print("endereço alterado !")



while(True):

    print("\nMenu: ")
    print("1-adicionar Aluno")
    print("2-Alterar endereço do aluno")
    print("3-pesquisa por aluno")
    print("4-Todos os alunos")
    print("5-Sair")
    print("###########################")


    opcao=int(input("Escolha uma opção:  "))
    if(opcao == 1):
        Aluno()
    elif(opcao == 2):
         alt_endereçoo()
    elif(opcao == 3):
         Aluno_pesquisado()
    elif(opcao == 4):
        Tod_aluno()
    elif(opcao == 5):
        break
    else:
        print("Escolha a opção correta")
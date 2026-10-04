from controller import PessoaController

while True:
    desicao = int(input("digite 1 para salvar uma pessoa ou 2 para ver pessoa salva ou 3 para sair : "))
    if desicao==3:
        break
    elif desicao==1:
        nome = input("digite seu nome : ")
        idade = input("digite sua idade: ")
        cpf = input("digite seu cpf: ")
        if PessoaController.Cadastrar(nome , idade , cpf):
            print("pessoa cadastrada com sucesso")
        else:
            print("digite valores validos")

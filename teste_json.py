import json
from pathlib import Path

arquivo = Path(__file__).parent/"teste.json"
def converter():
    with open(arquivo , 'r' , encoding='utf-8')as arq:
        pessoa = json.load(arq)
        return pessoa


pessoa = converter()


def salvar():
    with open(arquivo , 'w', encoding='utf-8') as arq:
        json.dump(pessoa , arq, indent=4 ,ensure_ascii=False)

def adicionar_dicionario():
    while True:
        desicao = int(input("1 para adicionar e 2 para não adicionar: "))
        if desicao == 1:
            checagem = True
            valor_nome = input("digite o nome: ")
            valor_idade = input("digite sua idade: ")
            valor_cpf = input("digite seu cpf: ")
            for i in pessoa:
                if valor_cpf == i["cpf"]:
                    print("erro de cadastro : ja tem um cpf anexado a estas informações")
                    checagem = False
                    break
            if checagem == True :
                p={
                    "nome":valor_nome,
                    "idade":valor_idade,
                    "cpf": valor_cpf
                }
                pessoa.append(p)
        elif desicao== 2:
            break


def pesquisa():
    lupa = input("pesquise o pelo cpf : ")
    achar = False
    for i in pessoa:
        if lupa == i["cpf"]:
            achar = True
            print(i)
            return i
    if achar == False:
        print("cpf não encontrado")
        


def editar():
    print("digite o cpf da pessoa que deseja alterar os dados")
    i = pesquisa()
    if i == None:
        print("cpf invalido para editar")
        return
    desicao = input("deseja alterar algo? 1 para sim e 2 para não : ")
    if desicao == "1":
        novo_valor_key = input("digite a oq quer alterar: nome , idade ou cpf: ")
        if novo_valor_key == "nome":
            nm = input("digite o novo nome: ")
            i["nome"] = nm
            print("dados alterados")
            print(i)
        elif novo_valor_key == "idade":
            idad = input("digite o nova idade: ")
            i["idade"] = idad
            print("dados alterados")
            print(i)
        elif novo_valor_key == "cpf":
            Cpf = input("digite o novo cpf: ")
            i["cpf"] = Cpf
            print("dados alterados")
            print(i)
    elif desicao == "2":
        print("ok , nada será alterado")
    elif desicao != "1" and desicao!="2": print("esta escolha não existe")

def delete():
    print("selecione a pessoa que deseja excluir pelo cpf: ")
    i = pesquisa()
    if i == None:
            print("cpf invalido para editar")
            return
    p = pessoa.index(i)
    print(p)
    desicao= input("tem certeza que essa é a pessoa que deseja deletar? 1 para sim e 2 para não: ")
    if desicao=="1":
        del pessoa[p]
        print("cadastro deletado com sucesso")
    else:pass

def rodar():
    desicao = input("digite 1 ler a lista , digite 2 para pesquisar na lista, digite 3 para editar a lista , 4 para adcionar a lista, digite 5 para deletar algum registro:  ")
    if desicao == "1":
        with open(arquivo , 'r' , encoding='utf-8')as arq:
            leitura = json.load(arq)
            print(leitura)
    elif desicao == "2":
        pesquisa()
    elif desicao == "3":
        editar()
    elif desicao == "4":
        adicionar_dicionario()
    elif desicao == "5":
        delete()
    salvar()




rodar()
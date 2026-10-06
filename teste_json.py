import json
from pathlib import Path

pessoa = []
def criar_dicionario():
    valor_nome = input("digite o nome")
    valor_idade = input("digite sua idade")
    p={
        "nome":valor_nome,
        "idade":valor_idade
    }
    pessoa.append(p)

def adicionar_dicionario():
    while True:
        desicao = int(input())
        if desicao == 1:
            criar_dicionario()
        else:
            break
    
def salvar():
    arquivo = Path(__file__).parent/"teste.json"
    with open(arquivo , 'w', encoding='utf-8') as arq:
        json.dump(pessoa , arq, indent=4 ,ensure_ascii=False)



adicionar_dicionario()
salvar()
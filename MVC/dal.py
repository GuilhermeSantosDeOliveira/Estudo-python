from pathlib import Path

from model import Pessoa


class PessoaDal:
    @classmethod
    def salvar(cls , pessoa:Pessoa):
        arquivo = Path(__file__).parent / "pessoa.txt"
        with open(arquivo , 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) +" " + str(pessoa.cpf))


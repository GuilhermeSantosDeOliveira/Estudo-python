from dal import PessoaDal
from model import Pessoa


class PessoaController:
    @classmethod
    def Cadastrar(cls , nome , idade,cpf):
        if len(nome) >= 3 and (int(idade) > 0 and int(idade) < 100) and len(cpf)==11:
            try:
                PessoaDal.salvar(Pessoa(nome , idade , cpf))
                return True
            except:  # noqa: E722
                return False

        else : 
            return False

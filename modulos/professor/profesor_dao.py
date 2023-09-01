from modulos.database import *

professores = []

class Professor (Usuario):

    def __init__(self, nome, senha):
        super().__init__(nome, senha)
    

    def set_matricula(self):
        return gerador_matricula(PROF)
    
    def dados_pessoais(self, email, telefone_pessoal, cpf,
                        cep, rua, bairro, cidade, numero_casa):
        
        super().dados_pessoais(email, telefone_pessoal, cpf)
        
        

        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero_casa = numero_casa


def buscar_professores (matricula):

    for professor in professores:
        if professor.get_matricula() == matricula:
            return professor
    
    return None

def criar_professor (usr):
    professores.append (usr)

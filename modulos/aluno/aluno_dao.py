from modulos.database import *

alunos = []

class Aluno (Usuario):

    def __init__(self, nome, senha):
        super().__init__(nome, senha)
    

    def set_matricula(self):
        return gerador_matricula(ALU)
    
    def dados_pessoais(self, email, telefone_pessoal, cpf,
                       nome_responsavel,numero_responsavel1, numero_responsavel2,
                        cep, rua, bairro, cidade, numero_casa):
        
        super().dados_pessoais(email, telefone_pessoal, cpf)
        
        self.nome_responsavel = nome_responsavel
        self.numero_responsavel2 = numero_responsavel1
        self.numero_responsavel1 = numero_responsavel2

        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero_casa = numero_casa



def buscar_alunos (matricula):

    for aluno in alunos:
        if aluno.get_matricula() == matricula:
            return aluno
    
    return None

def criar_aluno (usr):
    alunos.append (usr)

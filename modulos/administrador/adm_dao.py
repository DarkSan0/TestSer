from modulos.database import *
from modulos.aluno import alunos, Aluno, criar_aluno
from modulos.professor import professores, Professor, criar_professor

admins = []

class Administrador (Usuario):

    def __init__(self, nome, senha):
        super().__init__(nome, senha)
    
    def set_matricula(self):
        return gerador_matricula(ADM)
    
    def dados_pessoais(self, email, telefone_pessoal, cpf):
        super().dados_pessoais(email, telefone_pessoal)



def buscar_adiministradores (matricula):

    for adiministrador in admins:
        if adiministrador.get_matricula() == matricula:
            return adiministrador
    
    return None


def criar_adiministrador (usr):
    admins.append (usr)

from .base import *
from .users import *
from .constant import *




def criar_aluno(nome, idade, sexo, email, senha,nome_responsavel,numero_responsavel1, numero_responsavel2, cep, rua, bairro, cidade, numero_casa, cpf="000.000.000-00"):
    
    global  dados
    aluno = Aluno(nome,idade,sexo,email,nome_responsavel,numero_responsavel1,numero_responsavel2,cep,rua,bairro,cidade,numero_casa,cpf)
    
    
    (dados[ALU])[aluno.matricula] = {
        
        "dados": aluno,
        "senha": senha
    }
    return


def criar_professor( nome, idade, sexo, email, cpf, numero_telefone, cep, rua, bairro, cidade, numero_casa,senha):
    
    
    global  dados
    professor = Professor( nome, idade, sexo, email, cpf, numero_telefone, cep, rua, bairro, cidade, numero_casa)
    
    
    (dados[PROF])[professor.matricula] = {
        
        "dados": professor,
        "senha": senha
    }
    return


def criar_administrador (nome,idade,sexo,senha):
    
    global dados
    
    adm = Administrador(nome,idade,sexo)
    (dados[ADM])[adm.matricula] = {
        "dados":adm,
        "senha":senha
    }
    
    return


def get_user (tipo, matricula):
    
    global dados
    
    if tipo in dados:
        if matricula in dados[tipo]:
            return tipo, matricula
        
    return False

def Verificador_Usuario (senha, *usr):
    
    global dados
    
    if get_user(usr):
        tipo, matricula = usr
        if senha == ((dados[tipo])[matricula])["senha"]:
            return usr
        
    return False

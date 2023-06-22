from abc import abstractmethod, ABC
from ..func import gerador_matricula as gm
from ..constant import *



class Usuario (ABC):
    
    def __init__ (self,  nome, idade, sexo):
        
        self.__matricula = self.matricula_usr
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
    
    @abstractmethod
    def matricula_usr (self):
        pass
    
    @property
    def matricula (self):
        return self.__matricula


class Administrador (Usuario):
    
    def __init__(self,  nome, idade, sexo):
        super().__init__( nome, idade, sexo)
        
    def matricula_usr(self):
        return gm(ADM)



class Professor (Usuario):
    #Nome completo, cpf, numero,  email, cep, rua, bairro, cidade, casa
    def __init__(self,  nome, idade, sexo, email, numero_telefone, cep, rua, bairro, cidade, numero_casa, cpf):
        super().__init__( nome, idade, sexo)
        self.cpf = cpf
        self.numero_telefone = numero_telefone
        
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero_casa = numero_casa
        
    def matricula_usr(self):
        return gm(PROF)



class Aluno (Usuario):
    #Aluno: nome, cpf, numero do aluno, email, nome do responsavel, numero do responsavel 1 e 2, cep, rua, bairro, cidade, numero da casa
    def __init__(self,  nome, idade, sexo, email, nome_responsavel,
                numero_responsavel1, numero_responsavel2, cep, rua, bairro, cidade, numero_casa,
                cpf):
        super().__init__( nome, idade, sexo)
        self.cpf = cpf
        self.emil = email
        self.nome_responsavel = nome_responsavel
        
        self.numero_responsavel2 = numero_responsavel1
        self.numero_responsavel1 = numero_responsavel2
        
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero_casa = numero_casa
    
    
    def matricula_usr(self):
        return gm(ALU)
    

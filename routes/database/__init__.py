import datetime

ADM = 5
PROF = 6
ALU = 7


dados = {
    ADM: {},
    PROF: {},
    ALU: {}
    }

ano_set = "2023"
num_alu_ano = 0
num_prof_ano = 0
num_adm_ano = 0

def _gerador_matricula(tipo):
    global ano_set, num_alu_ano, num_prof_ano, num_adm_ano
    
    ano = datetime.datetime.now().date().strftime("%Y")
    if ano != ano_set:
        ano_set = ano
        num_alu_ano = 0
        num_prof_ano = 0
        num_adm_ano = 0
    
    if tipo == ALU:
        if num_alu_ano < 1000:
            string_alu = f"{num_alu_ano}"
            
            if num_alu_ano < 10:
                string_alu = f"00{num_alu_ano}"
            if num_alu_ano < 100 and num_alu_ano >= 10:
                string_alu = f"0{num_alu_ano}"

                
            num_alu_ano += 1
            return f"{ano_set}" + string_alu
    
    if tipo == PROF:
        if num_prof_ano < 100:
            string_alu = f"{num_prof_ano}"
            
            if num_prof_ano < 10:
                string_alu = f"0{num_prof_ano}"
                
            num_prof_ano += 1
            return f"{ano_set}" + string_alu
        
    if tipo == ADM:
        if num_adm_ano < 10:
            string_alu = f"{num_adm_ano}"    
            num_adm_ano += 1
            return f"{ano_set}" + string_alu




from abc import ABC, abstractmethod

class Usuario (ABC):
    
    def __init__ (self, nome, senha):
        
        self.__matricula = self.set_matricula()
        self.__nome = nome
        self.__senha = senha
    
    @abstractmethod
    def set_matricula (self):
        pass

    def get_senha (self):
        return self.__senha
    
    def get_matricula (self):
        return self.__matricula
    
    def get_dados_log (self):
        return self.__matricula, self.__senha
    
    def dados_pessoais (self, email, telefone_pessoal):
        self.email = email
        self.telefone_pessoal = telefone_pessoal
    
    






class Administrador (Usuario):

    def __init__(self, nome, senha):
        super().__init__(nome, senha)
    
    def set_matricula(self):
        return _gerador_matricula(ADM)
    
    def dados_pessoais(self, email, telefone_pessoal, cpf):
        super().dados_pessoais(email, telefone_pessoal)




class Professor (Usuario):

    def __init__(self, nome, senha):
        super().__init__(nome, senha)
    

    def set_matricula(self):
        return _gerador_matricula(PROF)
    
    def dados_pessoais(self, email, telefone_pessoal, cpf,
                        cep, rua, bairro, cidade, numero_casa):
        
        super().dados_pessoais(email, telefone_pessoal, cpf)
        
        

        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero_casa = numero_casa
    


class Aluno (Usuario):

    def __init__(self, nome, senha):
        super().__init__(nome, senha)
    

    def set_matricula(self):
        return _gerador_matricula(ALU)
    
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

    


if __name__ == "__main__":

    pr = Professor ("Jubileu", "12y7864")
    print (pr.get_matricula())
    dados[PROF] = {pr.get_matricula(): pr}
    
    print ((dados[PROF][pr.get_matricula()]).get_senha())
    
    #dados[PROF][pr.get_matricula] = pr
    print (dados)
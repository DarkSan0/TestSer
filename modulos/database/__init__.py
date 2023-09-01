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

def gerador_matricula(tipo):
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
        self.nome = nome
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



if __name__ == "__main__":

    pr = Professor ("Jubileu", "12y7864")
    print (pr.get_matricula())
    dados[PROF] = {pr.get_matricula(): pr}
    
    print ((dados[PROF][pr.get_matricula()]).get_senha())
    
    #dados[PROF][pr.get_matricula] = pr
    print (dados)
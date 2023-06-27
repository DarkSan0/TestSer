import datetime
from ..constant import *


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

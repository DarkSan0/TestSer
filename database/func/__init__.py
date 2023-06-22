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
        ant = num_alu_ano
        num_alu_ano += 1
        return f"{ano_set}{num_alu_ano}"
    
    if tipo == PROF:
        ant = num_alu_ano
        num_alu_ano += 1
        return f"{ano_set}{num_alu_ano}"
    
    if tipo == ADM:
        ant = num_adm_ano
        num_alu_ano += 1
        return f"{ano_set}{num_alu_ano}"

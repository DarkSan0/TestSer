from modulos.aluno.aluno_dao import buscar_alunos
from util.erros import Usuario_Invalido, Senha_Invalida

def validar_log_aluno (matricula, senha):
    
    usuario_encontrado = buscar_alunos(matricula)
    
    if not usuario_encontrado:
        raise Usuario_Invalido ("Usuario não Encontrado")
    
    if usuario_encontrado.get_senha() != senha:
        raise Senha_Invalida ("Senha Incorreta")
    
    
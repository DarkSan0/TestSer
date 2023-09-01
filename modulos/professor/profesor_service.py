from modulos.professor.profesor_dao import buscar_professores
from util.erros import Usuario_Invalido, Senha_Invalida


def validar_log_professor (matricula, senha):
    
    usuario_encontrado = buscar_professores(matricula)
    
    if not usuario_encontrado:
        raise Usuario_Invalido ("Usuario não Encontrado")
    
    if usuario_encontrado.get_senha() != senha:
        raise Senha_Invalida ("Senha Incorreta")
    
    
    
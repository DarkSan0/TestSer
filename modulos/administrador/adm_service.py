from modulos.administrador.adm_dao import buscar_adiministradores
from util.erros import Usuario_Invalido, Senha_Invalida


def validar_log_administrador (matricula, senha):
    
    usuario_encontrado = buscar_adiministradores (matricula)
    
    if not usuario_encontrado:
        raise Usuario_Invalido ("Usuario não Encontrado")
    
    if usuario_encontrado.get_senha() != senha:
        raise Senha_Invalida ("Senha Incorreta")
    
    
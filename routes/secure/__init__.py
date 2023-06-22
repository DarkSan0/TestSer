from flask import  render_template, request, redirect, url_for, session

def Redirecionador_PLOG (rota_logado,rota_deslogado):
    if session.get("usuario",None):
        return rota_logado
    return rota_deslogado
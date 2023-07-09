from flask import request, render_template, url_for, redirect, session, flash

from .secure import *
from .database import *
from .adm import *
from .professor import *
from .aluno import *


from routes import *

def redirecionador_home():
    
    status_usr = session.get("usuario")
    if status_usr:
        
        if len(status_usr) == ADM:
            return redirect(url_for('home_administrador'))
        
        if len(status_usr) == PROF:
            return redirect(url_for('home_professor'))
        
        if len(status_usr) == ALU:
            return redirect(url_for('home_aluno'))
    
    return redirect(url_for('login'))
    


def login ():
    if request.method == "POST":
        matricula = request.form.get("matricula", None)
        senha = request.form.get("senha", None)
        tamnho_mat = len(matricula)
        
        sucesso = Verificar_Tentativa_Log(dados, senha, matricula)
        if sucesso:
            session['usuario'] = sucesso
        if session.get('usuario'):
        
            return redirect(url_for('redirecionador_home'))
        flash("Matricula ou senha invalidas")
        return redirect(url_for("login"))
    
    
    if request.method == "GET":
        return render_template("Login.html")
    

    
def reset_senha ():
  return render_template("Esqueceu-Senha.html")



def visualizar ():
    return f"{dados}"


def deslogar ():
    del session['usuario']
    return redirect(url_for('redirecionador_home'))
from flask import request, render_template, url_for, redirect, session, flash

from .secure import *
from .database import *
from .adm import *
from .professor import *
from .aluno import *


from routes import *


def login ():
    if request.method == "POST":
        matricula = request.form.get("matricula", None)
        senha = request.form.get("senha", None)
        tamnho_mat = len(matricula)
        
        usr = Verificador_Usuario(senha, len(matricula),matricula)
        if usr:
            session.get["usuario"] = usr
            
            if tamnho_mat == ALU:
                return (redirect(url_for("home_alu")))
            
            if tamnho_mat == PROF:
                return (redirect(url_for("home_prof"))) 
            
            if tamnho_mat == ADM:
                return (redirect(url_for("home_admin"))) 
            
        flash("Matricula ou senha invalidas")
        return redirect(url_for("login"))
    
    
    if request.method == "GET":
        return render_template("index.html")
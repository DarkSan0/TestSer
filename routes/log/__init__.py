from flask import  render_template, request, redirect, url_for, session, flash
from ...database import *
from ..client import *
from ..admin import *


def login ():
    if request.method == "POST":
        matricula = request.form.get("matricula", None)
        senha = request.form.get("senha", None)
        tamnho_mat = len(matricula)
        
        usr = Verificador_Usuario(senha, len(matricula),matricula)
        if usr:
            session.get["usuario"] = usr
            
            if tamnho_mat == ALU:
                return (redirect(url_for(home_alu)))
            
            if tamnho_mat == PROF:
                return (redirect(url_for(home_prof))) 
            
            if tamnho_mat == ADM:
                return (redirect(url_for(home_admin))) 
        
        flash("Matricula ou Senha Invalidas")
        return redirect(url_for(login,_method="GET"))
    
    
    if request.method == "GET":
        return render_template("index.html")
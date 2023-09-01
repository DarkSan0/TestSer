from flask import Blueprint, render_template, session, flash, redirect, url_for
from util.security import permission

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

#@permission(['PROFESSOR'])
@professor_bp.route("/")
def home_professor():
    
    if not session.get("usuario"):
        flash ("Por favor realize o login")
        return redirect(url_for("login"))
    
    if not len(session.get("usuario")) == 6 :
        flash ("Permissão Negada")
        return redirect(url_for("redirecionador_home"))
    
    return render_template("Menu_professor.html")
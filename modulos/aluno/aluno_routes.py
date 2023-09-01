from flask import Blueprint, render_template, session, flash, redirect, url_for
from util.security import permission

aluno_bp = Blueprint("aluno", __name__, url_prefix="/aluno")

#@permission(['ALUNO'])
@aluno_bp.route("/")
def home_aluno():
    
    if not session.get("usuario"):
        flash ("Por favor realize o login")
        return redirect(url_for("login"))
    
    if not len(session.get("usuario")) == 7 :
        flash ("Permissão Negada")
        return redirect(url_for("redirecionador_home"))
    
    return render_template("Menu_aluno.html")
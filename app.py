from flask import Flask, render_template, request, redirect, url_for, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from modulos import aluno_bp, administrador_bp, professor_bp
from modulos import validar_log_aluno, validar_log_professor, validar_log_administrador
from util.autenticacao_form import LoginForm
from util.erros import Usuario_Invalido, Senha_Invalida
from flask_login import login_required



from modulos.administrador.adm_dao import criar_adiministrador, Administrador, admins
from modulos.professor.profesor_dao import criar_professor, Professor, professores
from modulos.aluno.aluno_dao import criar_aluno, Aluno, alunos

aluno0 = Aluno("Ronaldo", "1234")
professor0 = Professor("Vagner", "1234")
administrador0 = Administrador("Mario", "1234")

criar_adiministrador(administrador0)
criar_professor(professor0)
criar_aluno(aluno0)

app = Flask(__name__)
app.secret_key = "XUXA"

app.register_blueprint(aluno_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(administrador_bp)

@app.route ("/", methods = ["GET"])
def redirecionador_home():
    
    status_usr = session.get("usuario")
    if status_usr:
        
        if len(status_usr) == 5:
            return redirect(url_for('administrador.home_adm'))
        
        if len(status_usr) == 6:
            return redirect(url_for('professor.home_professor'))
        
        if len(status_usr) == 7:
            return redirect(url_for('aluno.home_aluno'))
    
    return redirect(url_for('login'))



##  --funções login--
@app.route ("/login", methods = ["GET", "POST"])
def login():
    if session.get("usuario"):
        return redirect(url_for("redirecionador_home"))
    
    loginForm = LoginForm()
    if request.method == "POST":
        if not loginForm.validate_on_submit():
            flash("Usuario ou senha Invalidos")
            return render_template("Login.html", form = loginForm)
            
            
        matricula = loginForm.matricula.data
        senha = loginForm.senha.data
        
            
        
        try:
            
            if len (matricula) == 5:
                validar_log_administrador(matricula, senha)
            
            if len (loginForm.matricula.data) == 6:
                validar_log_professor(matricula, senha)
                
                
            if len (loginForm.matricula.data) == 7:
                validar_log_aluno(matricula, senha)
            
            session["usuario"] = matricula
            return redirect(url_for("redirecionador_home"))
                
        except Usuario_Invalido:
            flash("Usuario Invalido")
            
        except Senha_Invalida:
            flash("Senha Incorreta")
        
    
    return render_template("Login.html", form = loginForm)

@app.route ("/deslogar")
def deslogar ():
    if session.get("usuario"):
        del session['usuario']
        
    return redirect(url_for('redirecionador_home'))
#######



@app.route ("/reset_senha")    
def reset_senha ():
    return render_template("Esqueceu-Senha.html")

@app.route ("/v")
def v ():
    texto = ""
    for usr in admins:
        texto += f"| matricula: {usr.get_matricula()},  senha: {usr.get_senha()}"
    texto += "/n"
    for usr in professores:
        texto += f"| matricula: {usr.get_matricula()},  senha: {usr.get_senha()}"
    texto += "/n"
    for usr in alunos:
        texto += f"| matricula: {usr.get_matricula()},  senha: {usr.get_senha()}"
    return texto

@app.route ("/logado")
def logado ():
    return f"{session.get('usuario', 'deslogado')}"



@app.route ("/tes")
def tes ():
    return render_template ("informacoes-professor.html")


if __name__ == "__main__":
    
    app.run(debug=True)
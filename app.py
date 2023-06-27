from flask import Flask, render_template, request, redirect, url_for, session, flash
#from flask_wtf import FlaskForm


#status: deslogado, logado

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XUXA'

"""class  LoginForm(FlaskForm):
  login = StringField("Usuário", validators = [DatarRequired()])
  senha = PasswordField("Senha", validators = [DatarRequired()])
  Olha o código do professor
  """
  

# Rotas Login
@app.route('/')
def acessando():
  status = session.get('usuario', None)
  if not status:
    return render_template('Login.html')
  else:
    return redirect(url_for('menu'))


# Rotas User, 'Esq-senha, logar e Deslogar'
@app.route('/user/login', methods = ['POST'])
def login():
  login = request.form.get('matricula','')
  senha = request.form.get('senha','')
  
  if login == 'aluno' and senha == '1234':

    session['usuario'] = 'aluno'
    return redirect(url_for("menu"))
  
  flash("Matricula ou senha incorreta")
  return redirect(url_for('acessando'))


@app.route ("/user/deslogar")
def deslogar ():
  del session["usuario"]
  return redirect(url_for("acessando"))


@app.route("/user/esqueceu-senha") 
def reset_senha ():
  return render_template("Esqueceu-Senha.html")



# Rotas Menu
@app.route("/menu")
def menu ():
  status = session.get('usuario', None)
  if status:
    return render_template ("Menu.html")
  return redirect(url_for("acessando"))



@app.route("/menu/adm/cadastrar/aluno")
def cadastrar_alu():
  return render_template("tela_de_cadastro-a.html")


@app.route("/menu/adm/cadastrar/professor")
def cadastrar_prof():
  return render_template("Cadastro-Professor")



"""
@app.route("/")
def redirecionador ():
  return redirect(url_for("login"))

app.add_url_rule("/login", "login", login)
"""

if __name__ == '__main__':
  app.run(debug= True)
from flask import Flask, render_template, request, redirect, url_for, session, flash
from routes.database import *
# from database import *
# from flask_wtf import FlaskForm


#status: deslogado, logado

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XUXA'

"""class  LoginForm(FlaskForm):
  login = StringField("Usuário", validators = [DatarRequired()])
  senha = PasswordField("Senha", validators = [DatarRequired()])
  Olha o código do professor
  """
  

# Rotas Login
# Rotas User, 'Esq-senha, logar e Deslogar'
@app.route('/', methods = ['GET', 'POST'])
def login():
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
              return (redirect(url_for("menu"))) 
          
          if tamnho_mat == ADM:
              return (redirect(url_for("home_admin"))) 
          
      flash("Matricula ou senha invalidas")
      return redirect(url_for("login"))
  
  
  if request.method == "GET":
      return render_template("Login.html")


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

  return render_template("Cadastro-Aluno.html")


@app.route("/menu/adm/cadastrar/professor", methods=['GET', 'POST'])
def cadastrar_prof():
  if request.method == 'POST':
    nome_professor = request.form.get('nome-prof')
    cpf_professor = request.form.get('cpf')
    numero_professor = request.form.get('numero-prof')
    data_nascimento = request.form.get('data-nascimento')
    email_professor = request.form.get('email')
    cep_professor = request.form.get('cep')
    rua_professor = request.form.get('rua')
    bairro_professor = request.form.get('bairro')
    cidade_professor = request.form.get('cidade')
    estado_professor = request.form.get('uf')
    numero_casa_professor = request.form.get('numero')

    global dados
    dados = criar_professor( nome_professor, data_nascimento, '', email_professor, cpf_professor, numero_professor, cep_professor, rua_professor, bairro_professor, cidade_professor, numero_casa_professor, '1234')

  return render_template("Cadastro-Professor.html")

@app.route('/v')
def vizualizar_cadastrado():
   return f'{dados}'

if __name__ == '__main__':
  app.run(debug= True)

from flask import Flask, render_template, request, redirect, url_for, session, flash
from routes import *

aluno0 = Aluno("Ronaldo", "1234")
professor0 = Professor("Vagner", "1234")
administrador0 = Administrador("Mario", "1234")

dados[ALU][aluno0.get_matricula()]= aluno0
dados[PROF][professor0.get_matricula()]= professor0
dados[ADM][administrador0.get_matricula()]= administrador0

app = Flask(__name__)
app.secret_key = "XUXA"


# inicio
app.add_url_rule("/", "redirecionador_home", redirecionador_home)
app.add_url_rule("/login", "login", login, methods = ["GET", "POST"])
app.add_url_rule("/esqueceu-senha", "reset_senha", reset_senha)

app.add_url_rule("/logout", "deslogar", deslogar)

app.add_url_rule("/v", "visualizar", visualizar)





# administar
app.add_url_rule("/menu/adm", "home_administrador",home_administrador)
app.add_url_rule("/menu/adm/cadastrar/adm", "cadastro_administrador",
                cadastro_administrador, methods = ["GET", "POST"])
app.add_url_rule("/menu/adm/cadastrar/p", "cadastro_professor",
                cadastro_professor, methods = ["GET", "POST"])
app.add_url_rule("/menu/adm/cadastrar/a", "cadastro_aluno",
                cadastro_aluno, methods = ["GET", "POST"])







# professor
app.add_url_rule("/menu/p", "home_professor",home_professor)







# aluno
app.add_url_rule("/menu/a", "home_aluno", home_aluno)




if __name__ == "__main__":
    
    app.run(debug=True)
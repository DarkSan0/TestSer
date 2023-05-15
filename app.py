from flask import Flask, render_template, request, redirect, url_for

#status: deslogado, logado
LOGADO = 1
DESLOGADO = 0
status = DESLOGADO

app = Flask(__name__)

@app.route('/')
def principal():
  global status
  if status == DESLOGADO:
    return render_template('loginSER.html')
  if status == LOGADO:
    return redirect(url_for('acessado'))


@app.route('/login', methods = ['POST'])
def recebendo_dados():
  global status
  login = request.form.get('matricula','')
  senha = request.form.get('senha','')

  if login == 'aluno' and senha == '1234':
    status = LOGADO
    return redirect(url_for("acessado"))
  
  return redirect(url_for('principal'))



@app.route("/principal")
def acessado ():
  global status
  if status == DESLOGADO:
    return redirect(url_for('principal'))
  return render_template('principal.html')

@app.route("/sair")
def desacessar():
  global status
  status = DESLOGADO
  return redirect(url_for('principal'))




  

if __name__ == '__main__':
  app.run()
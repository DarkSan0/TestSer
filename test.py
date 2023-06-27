from flask import Flask, render_template, request, redirect, url_for, session, flash
from routes import *

app = Flask (__name__)


#home
app.add_url_rule("/", "home", redirecionador)
#login
app.add_url_rule("/login", "login", login)


#administrador


#aluno


#professor


if __name__ == "__main__":
    app.run(debug=True)
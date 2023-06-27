"""from flask import Flask, render_template, request, redirect, url_for, session, flash
from routes import *



app = Flask (__name__)


#home
app.add_url_rule("/", "home", redirecionador)
#login
app.add_url_rule("/login", "login", login, methods = ["GET", "POST"])


#administrador


#aluno


#professor


if __name__ == "__main__":
    app.run(debug=True)"""
    
dic = {"abc":{}}
(dic["abc"])["1234"] = ""

dic2 = {"abc":{}}
dic2["abc"] = {"1234"}
dic2["abc"] = {'dados': "jdojoej", 'senha': "213876"}

print(dic, f"\n{dic2}")
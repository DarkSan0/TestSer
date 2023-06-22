from flask import Flask, render_template, request, redirect, url_for, session, flash
from routes import *

app = Flask(__name__)

app.add_url_rule("/","login",login)

app.add_url_rule("/menu/adm","home", home_admin)

if __name__ == "__main__":
    app.run(debug=True)
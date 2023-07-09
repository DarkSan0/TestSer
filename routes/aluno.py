from flask import request, render_template, url_for, redirect, session, flash
from .secure import Restrigir_Permissao
from .database import *

def home_aluno ():
    
    return Restrigir_Permissao(ALU, "Menu_F.html", "redirecionador_home", True)

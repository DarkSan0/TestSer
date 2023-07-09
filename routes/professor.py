from flask import request, render_template, url_for, redirect, session, flash
from .secure import Restrigir_Permissao
from .database import *

def home_professor ():
    
    return Restrigir_Permissao(PROF, "Menu_F.html", "redirecionador_home", True)

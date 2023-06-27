from flask import request, render_template, url_for, redirect, session, flash
from .secure import Restrigir_Permissao
from .database import *

def home_adm():
    return  Restrigir_Permissao(ADM, "Menu.html", "home")

def cadastro_aluno ():
    if request.method == "POST":
        fImage = request.form.get("fImage")
        nome_aluno = request.form.get("nome-aluno")
        cpf = request.form.get("cpf")
        numero_aluno = request.form.get("numero-aluno")
        email = request.form.get("email")
        data_nascimento = request.form.get("data-nascimento")
        
        nome_responsavel = request.form.get("nome-responsavel")
        numero_responsavel1 = request.form.get("numero-responsavel1")
        numero_responsavel2 = request.form.get("numero-responsavel2")
        
        cep = request.form.get("cep")
        rua = request.form.get("rua")
        bairro = request.form.get("bairro")
        cidade = request.form.get("cidade")
        estado = request.form.get("uf")
        numero_casa = request.form.get("numero")
        criar_aluno(nome_aluno, data_nascimento, "", email, "1234", nome_responsavel,numero_responsavel1, numero_responsavel2, cep, rua, bairro, cidade, numero_casa, cpf)
    
    
    return  Restrigir_Permissao(ADM, "Cadastro-Aluno.html", "home")

def cadastro_professor ():
    
    if request.method == "POST":
        pass
    
    return  Restrigir_Permissao(ADM, "Cadastro-Professor.html", "home")

def cadastro_adm ():
    if request.method == "POST":
        pass
        
        
    return  Restrigir_Permissao(ADM, "Cadastro-Administrador", "home")


    
    
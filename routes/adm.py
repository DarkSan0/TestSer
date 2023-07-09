from flask import request, render_template, url_for, redirect, session, flash
from .secure import Restrigir_Permissao
from .database import *




def home_administrador():
    return  Restrigir_Permissao(ADM, "Menu.html", "home")





def cadastro_administrador ():
    if request.method == "POST":
        pass
        
        
    return  Restrigir_Permissao(ADM, "Cadastro-Administrador", "home")






def cadastro_professor ():
    
    if request.method == "POST":
        imagem = request.form.get("flImage")
        nome_professor = request.form.get("nome-prof")
        
        cpf = request.form.get("cpf")
        numero_prof = request.form.get("numero-prof")
        """var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")"""
    
        pr = Professor(nome_professor, "1234")
        dados[PROF][pr.get_matricula()]= pr
    
    return  Restrigir_Permissao(ADM, "Cadastro-Professor.html", "home")






def cadastro_aluno ():

    if request.method == "POST":
        imagem = request.form.get("flImage")
        nome_aluno = request.form.get("nome-aluno")
        
        cpf = request.form.get("cpf")
        numero_aluno = request.form.get("numero-aluno")
        """var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")
        var1 = request.form.get("")"""
    
        al = Aluno(nome_aluno, "1234")
        dados[ALU][al.get_matricula()]= al
        
    return Restrigir_Permissao(ADM, "Cadastro-Aluno.html", "home")

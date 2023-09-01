from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from util.security import permission
from util.autenticacao_form import *
from modulos.administrador.adm_dao import alunos, admins, professores, Professor, Administrador, Aluno, criar_adiministrador, criar_aluno, criar_professor

administrador_bp = Blueprint("administrador", __name__, url_prefix="/administradror", )


@administrador_bp.route("/home")
#@permission(["ADMIN"])
def home_adm ():
    
    if not session.get("usuario"):
        flash ("Por favor realize o login")
        return redirect(url_for("login"))
    
    if not len(session.get("usuario")) == 5 :
        flash ("Permissão Negada")
        return redirect(url_for("redirecionador_home"))
        
    
    return render_template ("Menu.html")



@administrador_bp.route("/cadastrar_aluno", methods = ["GET", "POST"])
#@permission(["ADMIN"])
def cadastrar_aluno():
    cdt_aluno = Cadastro_AlunoForm()
    
    if not session.get("usuario"):
        flash ("Por favor realize o login")
        return redirect(url_for("login"))
    
    if not len(session.get("usuario")) == 5 :
        flash ("Permissão Negada")
        return redirect(url_for("redirecionador_home"))

    if request.method == "POST":
        if not cdt_aluno.validate_on_submit():
            flash ("Dados não prenchidos corretamente")
            
            return render_template ("Cadastro-Aluno.html", form = cdt_aluno)
            


        
        #imagem = cdt_aluno.fImage.data
        cpf = cdt_aluno.cpf.data
        numero = cdt_aluno.numero_aluno.data
        data_nasmento = cdt_aluno.data_nascimento.data
        email = cdt_aluno.email.data

        """nome_responsavel = cdt_aluno.nome_responsavel.data
        numero_responsavel1 = cdt_aluno.numero_responsavel1.data
        numero_responsavel2 = cdt_aluno.numero_responsavel2.data
        cep = cdt_aluno.cep.data
        rua = cdt_aluno.rua.data
        bairro = cdt_aluno.bairro.data
        cidade = cdt_aluno.cidade.data
        uf = cdt_aluno.uf.data
        numero = cdt_aluno.numero.data"""
        
        flash ("Dados prenchidos corretamente")
        aluno = Aluno (cdt_aluno.nome_aluno.data, "1234")
        
        criar_aluno(aluno)
        


    return render_template ("Cadastro-Aluno.html", form = cdt_aluno)



@administrador_bp.route("/cadastrar_professor", methods = ["GET", "POST"])
#@permission(["ADMIN"])
def cadastrar_professor():
    cdt_professor = Cadastro_ProfessorForm()
    
    if not session.get("usuario"):
        flash ("Por favor realize o login")
        return redirect(url_for("login"))
    
    if not len(session.get("usuario")) == 5 :
        flash ("Permissão Negada")
        return redirect(url_for("redirecionador_home"))

    if request.method == "POST":
        if not cdt_professor.validate_on_submit():
            flash ("Dados não prenchidos corretamente")
            
            return render_template ("Cadastro-Professor.html", form = cdt_professor)


        #fImage = cdt_professor.fImage.data
        
        nome_prof = cdt_professor.nome_prof.data
        cpf = cdt_professor.cpf.data
        numero_prof = cdt_professor.numero_prof.data
        data_nascimento = cdt_professor.data_nascimento.data
        email = cdt_professor.email.data
        
        """ cep = cdt_professor.cep.data
        rua = cdt_professor.rua.data
        bairro = cdt_professor.bairro.data
        cidade = cdt_professor.cidade.data
        uf = cdt_professor.uf.data
        numero = cdt_professor.numero.data"""
        
        
        professor = Professor(nome_prof, "1234")
        criar_professor (professor)


    return render_template ("Cadastro-Professor.html", form = cdt_professor)


@administrador_bp.route("/alunos_cadastrados", methods = ["GET"])
#@permission(["ADMIN"])
def alunos_cadastrados ():
    
    if not session.get("usuario"):
        flash ("Por favor realize o login")
        return redirect(url_for("login"))
    
    if not len(session.get("usuario")) == 5 :
        flash ("Permissão Negada")
        return redirect(url_for("redirecionador_home"))
    
    return render_template ("CadastradosAlunos.html", alunos = alunos, professores = professores)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField,DateField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    matricula = StringField("Usuário", validators=[DataRequired(), Length(min=5, max=7)])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=4)])

class Cadastro_AlunoForm(FlaskForm):
    #fImage = FileField("Image")
    nome_aluno = StringField ("Nome_aluno", validators=[DataRequired()])
    cpf = StringField ("Cpf_aluno", validators=[DataRequired()]) #, Length(11)
    numero_aluno = StringField ("Numero_aluno", validators=[DataRequired()])
    data_nascimento = DateField("Data_Nasc")
    email = StringField ("Email_aluno", validators=[DataRequired()])

    #nome_responsavel = StringField ("Nome_responsavel", validators=[DataRequired()])
    #numero_responsavel1 = StringField ("numero_responsavel1", validators=[DataRequired()])
    #numero_responsavel2 = StringField ("numero_responsavel2", validators=[DataRequired()])
    #cep = StringField("Cep", validators=[DataRequired()])
    #rua = StringField("Rua", validators=[DataRequired()])
    #bairro = StringField("Bairro", validators=[DataRequired()])
    #cidade = StringField("Cidade", validators=[DataRequired()])
    #uf = StringField("Uf", validators=[DataRequired()])
    #numero = StringField("Numero", validators=[DataRequired()])



class Cadastro_ProfessorForm(FlaskForm):
    #fImage = FileField("Image")
    nome_prof = StringField ("Nome_prof", validators=[DataRequired()])
    cpf = StringField ("Cpf", validators=[DataRequired()])
    numero_prof = StringField ("Numero_prof", validators=[DataRequired()])
    data_nascimento = DateField("Data_Nasc")
    email = StringField ("Email", validators=[DataRequired()])
    #cep = StringField ("Cep", validators=[DataRequired()])
    #rua = StringField ("Rua", validators=[DataRequired()])
    #bairro = StringField ("Bairro", validators=[DataRequired()])
    #cidade = StringField ("Cidade", validators=[DataRequired()])
    #uf = StringField ("Uf", validators=[DataRequired()])
    #numero = StringField("Numero", validators=[DataRequired()])

class Cadastro_AdmForm(FlaskForm):
    pass
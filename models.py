from app import database


class Professores(database.Model):
    matricula = database.Column(database.Integer, nullable=False, primary_key=True)
    email = database.Column(database.String, nullable=False, unique=True)
    nome = database.Column(database.String, nullable=False)
    cpf = database.Column(database.String, nullable=False, unique=True)
    cep = database.Column(database.String, nullable=False) # multivalorado
    idade = database.Column(database.Integer, nullable=False)
    rua = database.Column(database.String, nullable=False)
    cidade = database.Column(database.String, nullable=False)
    numero_casa = database.Column(database.Integer, nullable=False)
    bairro = database.Column(database.String, nullable=False)
    estado = database.Column(database.String(length=2), nullable=False)

class TelefoneProfessores(database.Model):
    telefone = database.Column(database.Integer, nullable=False, primary_key=True)
    matricula_prof = database.Column(database.Integer, database.ForeignKey('professores.matricula'), nullable=False)

class Turma(database.Model):
    codigo = database.Column(database.Integer, primary_key=True)
    dp_geral = database.Column(database.Float) # !

class Possuem(database.Model):
    semestre = database.Column(database.String, nullable=False, primary_key=True) 
    matricula_prof = database.Column(database.Integer, database.ForeignKey('professores.matricula'), nullable=False)
    codigo_turma = database.Column(database.Integer, database.ForeignKey('turma.codigo'), nullable=False)

class Disciplinas(database.Model):
    materia = database.Column(database.String, nullable=False, primary_key=True)
    dp_geral = database.Column(database.Float) 
    qtd_professor = database.Column(database.Integer) # !

class Ensinam(database.Model):
    semestre = database.Column(database.String, nullable=False, primary_key=True)
    materia = database.Column(database.String, database.ForeignKey('disciplinas.materia'), nullable=False)
    matricula_aluno = database.Column(database.Integer, database.ForeignKey('alunos.matricula'), nullable=False)
    matricula_professor = database.Column(database.Integer, database.ForeignKey('professores.matricula'), nullable=False)
    hor_disc = database.Column(database.String, nullable=False)
    recuperacao = database.Column(database.Float)
    avaliacao1 = database.Column(database.Float)
    avaliacao2 = database.Column(database.Float)
    bimestre = database.Column(database.Integer, nullable=False) # !

class Alunos(database.Model):
    matricula = database.Column(database.Integer, nullable=False, primary_key=True)
    cpf_responsavel = database.Column(database.String, database.ForeignKey('responsaveis.cpf'), nullable=False)
    idade = database.Column(database.Integer, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    telefone = database.Column(database.String, nullable=False, unique=True)
    nome = database.Column(database.String, nullable=False)
    cep = database.Column(database.String, nullable=False) # multivalorado
    rua = database.Column(database.String, nullable=False)
    cidade = database.Column(database.String, nullable=False)
    numero_casa = database.Column(database.Integer, nullable=False)
    bairro = database.Column(database.String, nullable=False)
    estado = database.Column(database.String(length=2), nullable=False)

class Responsaveis(database.Model):
    cpf = database.Column(database.String, nullable=False, primary_key=True)
    telefone = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)

class TelefoneResponsaveis(database.Model):
    telefone = database.Column(database.String, nullable=False, primary_key=True)
    cpf_responsavel = database.Column(database.String, database.ForeignKey('responsaveis.cpf'), nullable=False)




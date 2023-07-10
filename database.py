from models import *
from app import app, database

with app.app_context():
    # database.create_all()
    professor1 = Professores(matricula=1219, email='jotazin@gmail.com', nome='Jota', cpf='1281021', cep='213313-222', idade=35, rua='Santana de Azevedo', cidade='Santa Rita', numero_casa=785, bairro='Tibiri 2', estado='PB')
    database.session.add(professor1)
    database.session.commit()
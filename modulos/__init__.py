from modulos.aluno.aluno_routes import aluno_bp
from modulos.professor.profesor_routes import professor_bp
from modulos.administrador.adm_routes import administrador_bp

from modulos.administrador.adm_service import validar_log_administrador
from modulos.professor.profesor_service import validar_log_professor
from modulos.aluno.aluno_service import validar_log_aluno


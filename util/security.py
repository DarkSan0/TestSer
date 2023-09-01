from flask import session, flash, redirect, url_for

translate_role = {
    5: 'ADMIN',
    6: 'PROFESSOR',
    7: 'ALUNO'
}

def permission(roles):
    def decorator(fn):
        def inner(*args, **kwargs):
            matricula = session.get('usuario', '')
            role = translate_role.get(len(matricula), None)

            if role in roles:
                fn(*args, **kwargs)
            else:
                flash('Permissão negada')
                return redirect(url_for('redirecionador_home'))
        return inner
    return decorator

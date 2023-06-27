from flask import  render_template, redirect, url_for, session, flash

def Restrigir_Permissao (tipoUSR_pPermi,arquivo_html,rota_deslogado):
    status = session.get('usuario')
    if status:
        tipo = status[0]
        if tipo == tipoUSR_pPermi:
            return render_template(arquivo_html)
        flash("Permisão negada")
    
    return redirect(url_for(rota_deslogado))
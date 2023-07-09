from flask import  render_template, redirect, url_for, session, flash

def Restrigir_Permissao (tipoUSR_pPermi,arquivo_html,rota_deslogado,
                         enviar_dados = False):
    
    status = session.get('usuario')
    if status:
        tipo = len (status)
        if tipo == tipoUSR_pPermi:
            
            if enviar_dados:
                from ..database import dados
                
                
                info_usuario = dados[tipo][status]
                
                return render_template(arquivo_html,
                                       tipo_usuario = tipo,
                                       dados_usuario = info_usuario.get_matricula()
                                       )
                
            
            
            return render_template(arquivo_html)
        
        
        flash("Permisão negada")
    return redirect(url_for(rota_deslogado))





def Verificar_Tentativa_Log (dados, senha, matricula):
    
    
    tipo_usuario = len(matricula)
    if tipo_usuario in dados:
        
        if matricula in dados[tipo_usuario]:
            dados_matricula = dados[tipo_usuario][matricula]
            if senha == dados_matricula.get_senha():
                return matricula
    return False
        
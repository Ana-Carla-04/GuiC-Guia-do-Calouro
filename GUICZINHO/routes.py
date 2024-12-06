
from flask import Flask, render_template, request, redirect, session, flash, jsonify
import requests
import json
from GUICZINHO import app, banco_dados
from GUICZINHO.models import Usuario




app = Flask(__name__)
app.secret_key = 'napoleao'

# URL da API SUAP
SUAP_TOKEN_URL = 'https://suap.ifrn.edu.br/api/v2/autenticacao/token/'
SUAP_INFO_URL = 'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/'

print(SUAP_INFO_URL)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def suap_login():
    matricula = request.form['matricula']
    senha = request.form['senha']

    # Autenticação no SUAP via API
    payload = json.dumps({'username': matricula, 'password': senha})
    headers = {'Content-Type': 'application/json'}

    # Enviando a requisição de autenticação
    response = requests.post(SUAP_TOKEN_URL, data=payload, headers=headers)
    data = response.json()

    # Se o token de acesso for retornado
    if response.status_code == 200 and 'access' in data:
        token_acesso = data['access']
        
        # Armazenando o token na sessão
        session['token_acesso'] = token_acesso

        # Fazendo uma nova requisição para obter os dados do usuário
        headers = {'Authorization': f'Bearer {token_acesso}'}
        user_response = requests.get(SUAP_INFO_URL, headers=headers)
        user_data = user_response.json()

        if user_response.status_code == 200:
            nome_usuario = user_data['nome_usual']
            matricula_usuario = user_data['matricula']
            tipo_vinculo = user_data['tipo_vinculo']

            # Armazenando as informações do usuário na sessão
            session['nome_usuario'] = nome_usuario
            session['matricula_usuario'] = matricula_usuario
            session['tipo_vinculo'] = tipo_vinculo

            # Verifica se é um aluno, servidor ou prestador de serviço
            if tipo_vinculo in ["Prestador de Serviço", "Aluno", "Servidor"]:
                flash(f'Olá, {nome_usuario}! Seja bem-vindo ao sistema.', 'success')
                return redirect('/homepage')
            else:
                flash('Você não tem permissão para acessar o sistema.', 'error')
                return redirect('/')
        else:
            flash('Erro ao buscar informações do usuário.', 'error')
            return redirect('/')
    else:
        # Credenciais inválidas
        flash('Matrícula ou senha incorretas.', 'error')
        return redirect('/')

@app.route('/homepage')
def homepage():
    # Página protegida, acessível somente para usuários autorizados
    return render_template ('homepage.html')

@app.route('/eventos')
def eventos():
    return render_template ('eventos.html')

@app.route('/setores')
def setores():
    return render_template ('setores.html')

@app.route('/material')
def material():
    return render_template ('material.html')


# setores

@app.route('/auditorio')
def auditorio():
    return render_template ('/setores_templates/auditorio.html')

@app.route('/almoxarifado')
def almoxarifado():
    return render_template ('/setores_templates/almoxarifado.html')

@app.route('/biblioteca')
def biblioteca():
    return render_template ('/setores_templates/biblioteca.html')

@app.route('/coapac')
def coapac():
    return render_template ('/setores_templates/coapac.html')

@app.route('/CED')
def CED():
    return render_template ('/setores_templates/CED.html')

@app.route('/CE')
def CE():
    return render_template ('/setores_templates/CE.html')

@app.route('/ETEP')
def ETEP():
    return render_template ('/setores_templates/ETEP.html')

@app.route('/lab_pesquisa')
def lab_pesquisa():
    return render_template ('/setores_templates/lab_pesquisa.html')

@app.route('/miniauditorio')
def miniauditorio():
    return render_template ('/setores_templates/miniauditorio.html')

@app.route('/NAPNE')
def NAPNE():
    return render_template ('/setores_templates/NAPNE.html')

@app.route('/NEABI')
def NEABI():
    return render_template ('/setores_templates/NEABI.html')

@app.route('/NULIC')
def NULIC():
    return render_template ('/setores_templates/NULIC.html')

@app.route('/psicologia')
def psicologia():
    return render_template ('/setores_templates/psicologia.html')

@app.route('/servico_social')
def servico_social():
    return render_template ('/setores_templates/servico_social.html')

@app.route('/setor_saude')
def setor_saude():
    return render_template ('/setores_templates/setor_saude.html')

@app.route('/TI')
def TI():
    return render_template ('/setores_templates/TI.html')



# eventos

# @app.route('')
# def ():
#     return render_template('')


if __name__ == '__main__':
    app.run(debug=True)



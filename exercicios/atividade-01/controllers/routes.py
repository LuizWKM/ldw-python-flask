from flask import render_template, request, redirect, url_for

def init_app(app):
    enigmas = []
    lendas = []

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/enigmas', methods=['GET', 'POST'])
    def enigmas_page():
        if request.method == 'POST':
            titulo = request.form.get('titulo')
            pergunta = request.form.get('pergunta')
            resposta = request.form.get('resposta')
            if pergunta and resposta:
                enigmas.append({'titulo': titulo,'pergunta': pergunta, 'resposta': resposta})
                return redirect(url_for('enigmas_page'))
        return render_template('enigmas.html', enigmas=enigmas)

    @app.route('/lendas', methods=['GET', 'POST'])
    def lendas_page():
        if request.method == 'POST':
            titulo = request.form.get('titulo')
            origem = request.form.get('origem')
            descricao = request.form.get('descricao')
            if titulo and origem and descricao:
                lendas.append({'Título': titulo, 'Origem': origem, 'Descrição': descricao})
                return redirect(url_for('lendas_page'))
        return render_template('lendas.html', lendas=lendas)
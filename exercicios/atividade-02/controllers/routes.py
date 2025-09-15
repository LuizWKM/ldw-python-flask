from flask import render_template, request, redirect, url_for
import urllib # Envia requisições a uma URL
import json # Faz a conversão de dados json -> dicionário
import random  # Importando a biblioteca random para embaralhar as alternativas

def init_app(app):
    enigmas = []
    lendas = []
    # Lista de enigmas ou perguntas (Exemplo inicial)
    questions = []

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
    import random  # Importando a biblioteca random para embaralhar as alternativas

    @app.route('/trivia', methods=['GET', 'POST'])
    def trivia():
        url = 'https://opentdb.com/api.php?amount=10&category=20&language=pt'  # API da Open Trivia
        response = urllib.request.urlopen(url)
        data = response.read()
        triviaData = json.loads(data)

        # Armazenando as questões obtidas da API
        questions.clear()  # Limpa a lista a cada requisição
        for question in triviaData['results']:
            # Criando uma lista de respostas, incluindo a resposta correta e as incorretas
            all_answers = question['incorrect_answers'] + [question['correct_answer']]

            # Aleatorizando a ordem das alternativas
            random.shuffle(all_answers)

            # Armazenando as questões e as respostas embaralhadas
            question_data = {
                'question': question['question'],
                'correct_answer': question['correct_answer'],
                'incorrect_answers': question['incorrect_answers'],
                'all_answers': all_answers  # Respostas embaralhadas
            }
            questions.append(question_data)

        return render_template('trivia.html', questions=questions)

    @app.route('/trivia/<int:id>', methods=['GET'])
    def trivia_detail(id):
        question_detail = questions[id]
        return render_template('trivia_detail.html', question=question_detail)
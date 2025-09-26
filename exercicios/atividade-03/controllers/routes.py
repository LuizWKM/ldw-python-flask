from flask import render_template, request, redirect, url_for
from models.database import db, Lenda, Enigma
import urllib.request
import json

def init_app(app):
    enigmas = []
    lendas = []
    questions = []

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/enigmas', methods=['GET', 'POST'])
    def enigmas_page():
        enigmas = Enigma.query.all()
        return render_template('enigmas.html', enigmas=enigmas)

    @app.route('/lendas', methods=['GET', 'POST'])
    def lendas_page():
        lendas = Lenda.query.all()
        return render_template('lendas.html', lendas=lendas)

    @app.route('/trivia', methods=['GET', 'POST'])
    def trivia():
        url = 'https://opentdb.com/api.php?amount=10&category=20&language=pt'
        response = urllib.request.urlopen(url)
        data = response.read()
        triviaData = json.loads(data)
        questions.clear()
        for question in triviaData['results']:
            questions.append({
                'question': question['question'],
                'correct_answer': question['correct_answer'],
                'incorrect_answers': question['incorrect_answers']
            })
        return render_template('trivia.html', questions=questions)

    @app.route('/trivia/<int:id>', methods=['GET'])
    def trivia_detail(id):
        question_detail = questions[id]
        return render_template('trivia_detail.html', question=question_detail)

    @app.route('/enigmas/perguntas', methods=['GET', 'POST'])
    @app.route('/enigmas/perguntas/delete/<int:id>')
    def enigmasPerguntas(id=None):
        if id:
            enigma = Enigma.query.get(id)
            db.session.delete(enigma)
            db.session.commit()
            return redirect(url_for('enigmasPerguntas'))
        if request.method == 'POST':
            newenigma = Enigma(
                request.form['tituloE'],
                request.form['enigma'],
                request.form['respostaE'],
                request.form['lenda_id']
            )
            db.session.add(newenigma)
            db.session.commit()
            return redirect(url_for('enigmasPerguntas'))
        page = request.args.get('page', 1, type=int)
        per_page = 3
        enigmas_page = Enigma.query.paginate(page=page, per_page=per_page)
        lendas = Lenda.query.all()
        return render_template('enigmasperguntas.html', enigmasperguntas=enigmas_page, lendas=lendas)

    @app.route('/enigma/edit/<int:id>', methods=['GET', 'POST'])
    def enigmaEdit(id):
        e = Enigma.query.get(id)
        lendas = Lenda.query.all()
        if request.method == 'POST':
            e.tituloE = request.form['tituloE']
            e.enigma = request.form['enigma']
            e.respostaE = request.form['respostaE']
            e.lenda_id = request.form['lenda_id']
            db.session.commit()
            return redirect(url_for('enigmasPerguntas'))
        return render_template('editenigma.html', e=e, lendas=lendas)

    @app.route('/lendas/historias', methods=['GET', 'POST'])
    @app.route('/lendas/historias/delete/<int:id>')
    def lendasHistorias(id=None):
        if id:
            lenda = Lenda.query.get(id)
            db.session.delete(lenda)
            db.session.commit()
            return redirect(url_for('lendasHistorias'))
        if request.method == 'POST':
            newlenda = Lenda(
                request.form['tituloL'],
                request.form['origem'],
                request.form['descricao']
            )
            db.session.add(newlenda)
            db.session.commit()
            return redirect(url_for('lendasHistorias'))
        page = request.args.get('page', 1, type=int)
        per_page = 3
        lendas_page = Lenda.query.paginate(page=page, per_page=per_page)
        return render_template('lendashistorias.html', lendashistorias=lendas_page)

    @app.route('/lendas/edit/<int:id>', methods=['GET', 'POST'])
    def lendaEdit(id):
        lenda = Lenda.query.get(id)
        if request.method == 'POST':
            lenda.tituloL = request.form['tituloL']
            lenda.origem = request.form['origem']
            lenda.descricao = request.form['descricao']
            db.session.commit()
            return redirect(url_for('lendasHistorias'))
        return render_template('editlenda.html', lenda=lenda)
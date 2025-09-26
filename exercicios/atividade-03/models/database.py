from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável por criar a entidade "Lendas" com seus atributos.
class Lenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tituloL = db.Column(db.String(150))
    origem = db.Column(db.String(150))
    descricao = db.Column(db.String(150))

    def __init__(self, tituloL, origem, descricao):
        self.tituloL = tituloL
        self.origem = origem
        self.descricao = descricao

# Classe responsável por criar a entidade "Enigma" com seus atributos.
class Enigma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tituloE = db.Column(db.String(150))
    enigma = db.Column(db.String(150))
    respostaE = db.Column(db.String(150))
    lenda_id = db.Column(db.Integer, db.ForeignKey('lenda.id'))
    
    lenda = db.relationship('Lenda', backref=db.backref('enigma', lazy=True))

    def __init__(self, tituloE, enigma, respostaE, lenda_id): 
        self.tituloE = tituloE
        self.enigma = enigma
        self.respostaE = respostaE
        self.lenda_id = lenda_id
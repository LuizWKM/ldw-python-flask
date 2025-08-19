from flask import Flask, render_template # Importando o Flask
from controllers import routes

# Criando uma instância do Flask
app = Flask(__name__, template_folder='views') # O __name__ representa o nome da aplicação/arquivo que está sendo executado futuramente irá ser __main__

routes.init_app(app)

# Se o arquivo for executado diretamento pelo interpretador ele vira o nome __main__ e inicia o servidor
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) # Iniciando o servidor
from flask import Flask, render_template # Importando o Flask

# Criando uma instância do Flask
app = Flask(__name__, template_folder='views') # O __name__ representa o nome da aplicação/arquivo que está sendo executado futuramente irá ser __main__

# Definindo a rota principal da aplicação '/'


@app.route('/')
def home(): # Função que será executada ao acessar a rota
    return render_template('index.html')


@app.route('/games')
def games():
    title = 'Tarisland'
    year = 2022
    category = 'MMORPG'
    # Lista em Python(array)
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    #Dicionário (Objeto)
    console = {'Nome': 'Playstation 5', 
               'Fabricante': 'Sony',
               'Ano': 2020}
    return render_template('games.html',
                           title=title,
                           year=year,
                           category=category,
                           players=players,
                           console=console)


# Se o arquivo for executado diretamento pelo interpretador ele vira o nome __main__ e inicia o servidor
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) # Iniciando o servidor
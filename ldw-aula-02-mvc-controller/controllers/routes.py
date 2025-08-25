from flask import render_template, request


def init_app(app):
    # Lista em Python(array)
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    @app.route('/')
    # Definindo a rota principal da aplicação '/

    def home(): # Função que será executada ao acessar a rota
        return render_template('index.html')


    @app.route('/games', methods=['GET', 'POST'])
    def games(): #Essa é uma view function
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'
    
        #Dicionário (Objeto)
        console = {'Nome': 'Playstation 5', 
                'Fabricante': 'Sony',
                'Ano': 2020}
        
        # Tratando uma requisição POST com request
        if request.method == 'POST':
            # Coletando o texto da input
            if request.form.get('player'):
                players.append(request.form.get('player'))
        
        
        return render_template('games.html',
                            title=title,
                            year=year,
                            category=category,
                            players=players,
                            console=console)
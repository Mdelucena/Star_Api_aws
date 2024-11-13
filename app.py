from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Função para pegar todos os dados de uma URL com paginação
def get_all_data(url):
    results = []
    while url:
        response = requests.get(url)
        data = response.json()
        results.extend(data['results'])
        url = data.get('next')
    return results

# Função para pegar um único dado (um item específico) da URL
def get_single_data(url):
    response = requests.get(url)
    return response.json()

# Endpoint para filmes com filtros, paginação e ordenação
@app.route('/filmes', methods=['GET'])
def get_filmes():
    ordenar = request.args.get('ordenar', default='titulo')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    
    url = "https://swapi.dev/api/films/"
    filmes = get_all_data(url)

    if ordenar == 'ano_lancamento':
        filmes = sorted(filmes, key=lambda x: x['release_date'])
    elif ordenar == 'titulo':
        filmes = sorted(filmes, key=lambda x: x['title'])

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "total_filmes": len(filmes),
        "filmes": filmes[start:end]
    })

# Endpoint para um filme específico
@app.route('/filmes/<int:film_id>', methods=['GET'])
def get_film(film_id):
    url = f"https://swapi.dev/api/films/{film_id}/"
    film = get_single_data(url)
    return jsonify(film)

# Endpoint para personagens com filtros, paginação e ordenação
@app.route('/personagens', methods=['GET'])
def get_personagens():
    nome = request.args.get('nome')
    ordenar = request.args.get('ordenar', default='nome')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    url = "https://swapi.dev/api/people/"
    personagens = get_all_data(url)

    if nome:
        personagens = [p for p in personagens if nome.lower() in p['name'].lower()]
    
    if ordenar == 'nome':
        personagens = sorted(personagens, key=lambda x: x['name'])

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "total_personagens": len(personagens),
        "personagens": personagens[start:end]
    })

# Endpoint para um personagem específico
@app.route('/personagens/<int:personagem_id>', methods=['GET'])
def get_personagem(personagem_id):
    url = f"https://swapi.dev/api/people/{personagem_id}/"
    personagem = get_single_data(url)
    return jsonify(personagem)

# Endpoint para planetas com filtros, paginação e ordenação
@app.route('/planetas', methods=['GET'])
def get_planetas():
    nome = request.args.get('nome')
    ordenar = request.args.get('ordenar', default='nome')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    url = "https://swapi.dev/api/planets/"
    planetas = get_all_data(url)

    if nome:
        planetas = [p for p in planetas if nome.lower() in p['name'].lower()]
    
    if ordenar == 'nome':
        planetas = sorted(planetas, key=lambda x: x['name'])

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "total_planetas": len(planetas),
        "planetas": planetas[start:end]
    })

# Endpoint para um planeta específico
@app.route('/planetas/<int:planeta_id>', methods=['GET'])
def get_planeta(planeta_id):
    url = f"https://swapi.dev/api/planets/{planeta_id}/"
    planeta = get_single_data(url)
    return jsonify(planeta)

# Endpoint para naves com filtros, paginação e ordenação
@app.route('/naves', methods=['GET'])
def get_naves():
    nome = request.args.get('nome')
    ordenar = request.args.get('ordenar', default='nome')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    url = "https://swapi.dev/api/starships/"
    naves = get_all_data(url)

    if nome:
        naves = [n for n in naves if nome.lower() in n['name'].lower()]
    
    if ordenar == 'nome':
        naves = sorted(naves, key=lambda x: x['name'])

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "total_naves": len(naves),
        "naves": naves[start:end]
    })

# Endpoint para uma nave específica
@app.route('/naves/<int:ship_id>', methods=['GET'])
def get_nave(ship_id):
    url = f"https://swapi.dev/api/starships/{ship_id}/"
    nave = get_single_data(url)
    return jsonify(nave)

# Endpoint para veículos com filtros, paginação e ordenação
@app.route('/veiculos', methods=['GET'])
def get_veiculos():
    nome = request.args.get('nome')
    ordenar = request.args.get('ordenar', default='nome')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    url = "https://swapi.dev/api/vehicles/"
    veiculos = get_all_data(url)

    if nome:
        veiculos = [v for v in veiculos if nome.lower() in v['name'].lower()]
    
    if ordenar == 'nome':
        veiculos = sorted(veiculos, key=lambda x: x['name'])

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "total_veiculos": len(veiculos),
        "veiculos": veiculos[start:end]
    })

# Endpoint para um veículo específico
@app.route('/veiculos/<int:vehicle_id>', methods=['GET'])
def get_veiculo(vehicle_id):
    url = f"https://swapi.dev/api/vehicles/{vehicle_id}/"
    veiculo = get_single_data(url)
    return jsonify(veiculo)

if __name__ == '__main__':
    app.run(debug=True)

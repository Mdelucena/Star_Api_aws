import pytest
from app import app  # Importe o seu objeto Flask da sua aplicação

@pytest.fixture
def client():
    # Cria uma instância do aplicativo para os testes
    with app.test_client() as client:
        yield client  # Vai liberar o client para ser usado nos testes

def test_get_filmes(client):
    # Testando o endpoint de filmes
    response = client.get('/filmes')
    assert response.status_code == 200  # Verifique se a resposta foi 200 (OK)
    json_data = response.get_json()
    assert 'filmes' in json_data  # Verifique se a chave 'filmes' está presente no JSON

def test_get_film(client):
    # Testando o endpoint de um filme específico (substitua com um ID válido)
    response = client.get('/filmes/1')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'title' in json_data  # Verifique se o título do filme está presente

def test_get_personagens(client):
    # Testando o endpoint de personagens
    response = client.get('/personagens?nome=Leia')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'personagens' in json_data  # Verifique se a chave 'personagens' está presente
    assert len(json_data['personagens']) > 0  # Verifique se há resultados para "Leia"

def test_get_planetas(client):
    # Testando o endpoint de planetas
    response = client.get('/planetas')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'planetas' in json_data  # Verifique se a chave 'planetas' está presente

def test_get_naves(client):
    # Testando o endpoint de naves
    response = client.get('/naves?nome=Falcon')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'naves' in json_data  # Verifique se a chave 'naves' está presente
    assert len(json_data['naves']) > 0  # Verifique se há resultados para "Falcon"

def test_get_veiculos(client):
    # Testando o endpoint de veículos
    response = client.get('/veiculos')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'veiculos' in json_data  # Verifique se a chave 'veiculos' está presente

# Star Wars API - RESTful API

Esta é uma API RESTful que utiliza a [API pública do Star Wars (swapi.dev)](https://swapi.dev/) para fornecer informações sobre a saga Star Wars. A API permite consultar dados sobre filmes, personagens, planetas, naves e veículos.

## Funcionalidades

A API permite realizar as seguintes consultas:

- **Filmes**: Obtenha informações sobre os filmes da saga Star Wars.
- **Personagens**: Consulte detalhes dos personagens principais.
- **Planetas**: Informações sobre os planetas no universo Star Wars.
- **Naves**: Dados sobre as naves espaciais usadas pelos personagens.
- **Veículos**: Detalhes sobre os veículos usados nas aventuras.

Cada recurso pode ser consultado de duas formas:

1. **Listando todos os itens** (por exemplo, todos os filmes, personagens, etc.).
2. **Consultando um item específico** pelo ID (por exemplo, o filme com ID 1 ou o personagem com ID 4).

## Endpoints da API

### Filmes

- **GET `/filmes`**: Retorna todos os filmes da saga Star Wars.
- **GET `/filmes/{id}`**: Retorna um filme específico pelo ID.

### Personagens

- **GET `/personagens`**: Retorna todos os personagens.
- **GET `/personagens/{id}`**: Retorna um personagem específico pelo ID.

### Planetas

- **GET `/planetas`**: Retorna todos os planetas.
- **GET `/planetas/{id}`**: Retorna um planeta específico pelo ID.

### Naves

- **GET `/naves`**: Retorna todas as naves.
- **GET `/naves/{id}`**: Retorna uma nave específica pelo ID.

### Veículos

- **GET `/veiculos`**: Retorna todos os veículos.
- **GET `/veiculos/{id}`**: Retorna um veículo específico pelo ID.

## Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/star-wars-api.git

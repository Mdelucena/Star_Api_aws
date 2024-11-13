import json
import requests

BASE_URL = "https://swapi.dev/api"

def lambda_handler(event, context):
    # Extrai o caminho e os parâmetros da requisição
    resource = event['pathParameters']['resource']  # Identifica o recurso como 'films', 'people', etc.
    resource_id = event.get('queryStringParameters', {}).get('id', None)
    
    # Extrai filtros adicionais dos parâmetros de consulta, se houver
    filters = event.get('queryStringParameters', {}).get('filters', None)
    
    # Constrói a URL da API de acordo com o recurso e o ID
    url = f"{BASE_URL}/{resource}/"
    if resource_id:
        url += f"{resource_id}/"
    
    # Se filtros forem passados, adiciona-os à URL
    if filters:
        # Assumindo que os filtros sejam passados como uma string com formato chave=valor
        filters = filters.split(',')  # Supondo que os filtros sejam separados por vírgulas
        for filter in filters:
            key, value = filter.split('=')
            url += f"?{key}={value}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
        
    except requests.exceptions.HTTPError as http_err:
        return {
            'statusCode': response.status_code,
            'body': json.dumps({"error": f"HTTP error occurred: {http_err}"}),  # Erro HTTP
        }
    except Exception as err:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": f"An error occurred: {err}"}),  # Erro genérico
        }

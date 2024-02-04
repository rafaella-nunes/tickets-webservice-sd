import requests
from requests.exceptions import HTTPError, RequestException

base_url = "http://127.0.0.1:5000"

def make_request(method, url, data=None):
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url)
        else:
            print("Método não suportado")
            return None

        response.raise_for_status()
        return response.json()

    except HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
    except RequestException as req_err:
        print(f"Erro na requisição: {req_err}")
    except Exception as e:
        print(f"Erro desconhecido: {e}")

if __name__ == "__main__":
    # Listar todos os ingressos
    response = make_request('GET', f"{base_url}/ingressos")
    if response:
        print(response)

    # Obter detalhes de um ingresso específico
    response = make_request('GET', f"{base_url}/ingressos/1")
    if response:
        print(response)

    # Adicionar um novo ingresso
    novo_ingresso = {"nome": "Ingresso Família", "preco": 100}
    response = make_request('POST', f"{base_url}/ingressos", data=novo_ingresso)
    if response:
        print(response)

    # Atualizar um ingresso existente
    ingresso_atualizado = {"nome": "Ingresso VIP Atualizado", "preco": 60}
    response = make_request('PUT', f"{base_url}/ingressos/2", data=ingresso_atualizado)
    if response:
        print(response)

    # Excluir um ingresso
    response = make_request('DELETE', f"{base_url}/ingressos/3")
    if response:
        print(response)

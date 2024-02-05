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
    op = 0
    while(op != 6):
        print("1 - Ver Ingressos disponíveis")
        print("2 - Adicionar Ingressos")
        print("3 - Editar Ingresso")
        print("4 - Comprar Ingresso")
        print("5 - Deletar Ingresso")
        print("6 - Sair")
        op = int(input("Escolha uma opção: "))
        if op == 1:
            response = make_request('GET', f"{base_url}/ingressos")
            if response:
                print(response)
        elif op == 2:
            ingresso_id = int(input("digite o id do ingresso: "))
            ingresso_name = input("digite o nome do ingresso: ")
            ingresso_preco = int(input("digite o preço do ingresso: "))
            ingresso_quant = int(input("digite a quantidade do ingresso: "))
            novo_ingresso = {"id": ingresso_id, "nome": ingresso_name, "preco": ingresso_preco, "quantidade": ingresso_quant}
            response = make_request('POST', f"{base_url}/ingressos", data=novo_ingresso)
            if response:
                print(response)

        elif op == 3:
            response = make_request('GET', f"{base_url}/ingressos")
            if response:
                print(response)
                ingresso_id = int(input("digite o id do ingresso que deseja editar: "))
                ingresso_name = input("digite o nome do ingresso: ")
                ingresso_preco = int(input("digite o preço do ingresso: "))
                ingresso_quant = int(input("digite a quantidade do ingresso: "))
                ingresso_atualizado = {"id": ingresso_id, "nome": ingresso_name, "preco": ingresso_preco, "quantidade": ingresso_quant}
                response = make_request('PUT', f"{base_url}/ingressos/{ingresso_id}", data=ingresso_atualizado)
                if response:
                    print(response)
        elif op == 4:
            ingresso_id = int(input("digite o id do ingresso que deseja comprar: "))
            ingresso_quant = int(input("digite a quantidade que deseja comprar: "))
            response = make_request('GET', f"{base_url}/ingressos/{ingresso_id}")
            if response:
                quant_restante = int(response["quantidade"]) - ingresso_quant
                preco = int(response["preco"])
                if(quant_restante >= 0):
                    ingresso_atualizado = {"id": ingresso_id, "nome": ingresso_name, "preco": ingresso_preco, "quantidade": quant_restante}
                    response = make_request('PUT', f"{base_url}/ingressos/{ingresso_id}", data=ingresso_atualizado)
                    if response:
                        print(response)
                        if response["mensagem"] == "Sucesso":
                            print("Valor pago: ", preco * ingresso_quant)
                else:
                    print("quantidade de ingressos não disponível")
                
        elif op == 5:
            ingresso_id = int(input("digite o id do ingresso que deseja excluir: "))
            response = make_request('DELETE', f"{base_url}/ingressos/{ingresso_id}")
            if response:
                print(response)

import requests

base_url = "http://127.0.0.1:5000"

# Listar todos os ingressos
response = requests.get(f"{base_url}/ingressos")
print(response.json())

# Obter detalhes de um ingresso específico
response = requests.get(f"{base_url}/ingressos/1")
print(response.json())

# Adicionar um novo ingresso
novo_ingresso = {"nome": "Ingresso Família", "preco": 100}
response = requests.post(f"{base_url}/ingressos", json=novo_ingresso)
print(response.json())

# Atualizar um ingresso existente
ingresso_atualizado = {"nome": "Ingresso VIP Atualizado", "preco": 60}
response = requests.put(f"{base_url}/ingressos/2", json=ingresso_atualizado)
print(response.json())

# Excluir um ingresso
response = requests.delete(f"{base_url}/ingressos/3")
print(response.json())

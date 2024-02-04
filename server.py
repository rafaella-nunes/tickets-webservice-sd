from flask import Flask, request, jsonify

app = Flask(__name__)

# Banco de dados
ingressos = [
    {"id": 1, "nome": "Ingresso Padrão", "preco": 20},
    {"id": 2, "nome": "Ingresso VIP", "preco": 50},
    {"id": 3, "nome": "Ingresso Familia", "preco": 100},
]

# Endpoint para listar todos os ingressos
@app.route('/ingressos', methods=['GET'])
def listar_ingressos():
    return jsonify({"ingressos": ingressos})

# Endpoint para obter um ingresso específico
@app.route('/ingressos/<int:ingresso_id>', methods=['GET'])
def obter_ingresso(ingresso_id):
    ingresso = next((i for i in ingressos if i['id'] == ingresso_id), None)
    if ingresso:
        return jsonify({"ingresso": ingresso})
    else:
        return jsonify({"mensagem": "Ingresso não encontrado"}), 404

# Endpoint para adicionar um novo ingresso
@app.route('/ingressos', methods=['POST'])
def adicionar_ingresso():
    novo_ingresso = request.json
    ingressos.append(novo_ingresso)
    return jsonify({"mensagem": "Ingresso adicionado com sucesso"})

# Endpoint para atualizar um ingresso existente
@app.route('/ingressos/<int:ingresso_id>', methods=['PUT'])
def atualizar_ingresso(ingresso_id):
    ingresso_atualizado = request.json
    for i, ingresso in enumerate(ingressos):
        if ingresso['id'] == ingresso_id:
            ingressos[i] = ingresso_atualizado
            return jsonify({"mensagem": "Ingresso atualizado com sucesso"})
    return jsonify({"mensagem": "Ingresso não encontrado"}), 404

# Endpoint para excluir um ingresso
@app.route('/ingressos/<int:ingresso_id>', methods=['DELETE'])
def excluir_ingresso(ingresso_id):
    global ingressos
    try:
        ingresso_existente = next((i for i in ingressos if i['id'] == ingresso_id), None)
        if ingresso_existente:
            ingressos = [i for i in ingressos if i['id'] != ingresso_id]
            return jsonify({"mensagem": "Ingresso excluído com sucesso"})
        else:
            return jsonify({"mensagem": "Ingresso não encontrado"}), 404
    except Exception as e:
        return jsonify({"mensagem": f"Erro interno: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

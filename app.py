from flask import Flask, jsonify #Criando aplicação web Flask
import json #Importando json para ler o arquivo de dados
import random #Importando random para escolher uma pergunta aleatória

app = Flask(__name__) 

with open('dados.json', 'r', encoding='utf-8') as f: #Guardando o arquivo json em uma variável Python
    dados = json.load(f)

@app.route('/pergunta') #Retornando uma pergunta aleatória
def pergunta_aleatoria():
    return jsonify(random.choice(dados))

@app.route('/todas') #Retornando todas as perguntas
def todas_perguntas():
    return jsonify(dados)

@app.route('/resposta/<int:id>') #Retornando a resposta de uma pergunta específica, usando o id como parâmetro
def resposta(id):
    for item in dados:
        if item["id"] == id:
            return jsonify({"resposta": item["resposta"]})
    return jsonify({"erro": "Pergunta não encontrada"})

app.run(debug=True) #Iniciando o servidor Flask em modo de depuração para facilitar o desenvolvimento e testes

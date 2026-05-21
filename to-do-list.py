from flask import Flask, request

app = Flask(__name__)

tarefas = []

@app.route("/tareas", methods =["GET"])
def listar():
    return {"tarefas": tarefas}

@app.route("/tarefas", methods =["POST"])
def adicionar():
    dados = request.json
    tarefas.append(dados["tarefas"])
    return{"mensagem": "Tarefa adicionada" }

app.run(debug=True)

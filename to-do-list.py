from flask import Flask, request

app = Flask(__name__)

tarefas = []

@app.route("/tarefas", methods=["GET"])
def listar():
    return {"tarefas": tarefas}

@app.route("/")
def home():
    return {"mensagem": "API funcionando!"}

@app.route("/tarefas", methods=["POST"])
def adicionar():
    dados = request.json
    tarefas.append(dados["tarefa"])
    return {"mensagem": "Tarefa adicionada"}

app.run(debug=True)
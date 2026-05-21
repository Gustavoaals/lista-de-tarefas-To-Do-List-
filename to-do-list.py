from flask import flask, request

app = flask(__name__)

tarefas = []

@app.route("/tareas", methods =["GET"])
def listar():
    return {"tarefas": tarefas}

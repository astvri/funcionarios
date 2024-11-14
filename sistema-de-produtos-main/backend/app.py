from flask import Flask, request, jsonify
from flask_cors import CORS
from src.controller.funcionario_controller import (
    cadastrar_funcionario, listar_funcionarios,
    buscar_funcionario, atualizar_funcionario, deletar_funcionario
)

app = Flask(__name__)

CORS(app)

# Rota para cadastrar um novo funcionário
@app.route('/funcionarios', methods=['POST'])
def cadastrar_funcionario_route():
    data = request.get_json()
    return cadastrar_funcionario(
        data['nomeFuncionario'], data['codigo'], data['setor'], data['salario'], data['cargaHoraria']
    )

# Rota para listar todos os funcionários
@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios_route():
    return listar_funcionarios()

# Rota para buscar um funcionário específico pelo código
@app.route('/funcionarios/<int:codigo>', methods=['GET'])
def buscar_funcionario_route(codigo):
    return buscar_funcionario(codigo)

# Rota para atualizar as informações de um funcionário
@app.route('/funcionarios/<int:codigo>', methods=['PUT'])
def atualizar_funcionario_route(codigo):
    data = request.get_json()
    return atualizar_funcionario(codigo, data.get('nomeFuncionario'), data.get('setor'), data.get('salario'), data.get('cargaHoraria'))

# Rota para deletar um funcionário
@app.route('/funcionarios/<int:codigo>', methods=['DELETE'])
def deletar_funcionario_route(codigo):
    return deletar_funcionario(codigo)


if __name__ == '__main__':
    app.run(debug=True)

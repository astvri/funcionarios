from flask import request, jsonify
from src.model.funcionario_modal import (
    criar_funcionario, listar_funcionarios, buscar_funcionario, atualizar_funcionario, deletar_funcionario
)

def cadastrar_funcionario(nomeFuncionario, codigo, setor, salario, cargaHoraria):
    message, status_code = criar_funcionario(nomeFuncionario, codigo, setor, salario, cargaHoraria)
    return jsonify(message), status_code

def listar_funcionarios_controller():
    funcionarios_list, status_code = listar_funcionarios()
    return jsonify(funcionarios_list), status_code

def buscar_funcionario_controller(codigo):
    funcionario, status_code = buscar_funcionario(codigo)
    return jsonify(funcionario), status_code

def atualizar_funcionario_controller(codigo, nomeFuncionario, setor, salario, cargaHoraria):
    message, status_code = atualizar_funcionario(codigo, nomeFuncionario, setor, salario, cargaHoraria)
    return jsonify(message), status_code

def deletar_funcionario_controller(codigo):
    message, status_code = deletar_funcionario(codigo)
    return jsonify(message), status_code

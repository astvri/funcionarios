import mysql.connector
from src.database.conexao import criar_conexao
from flask import jsonify

# Função para criar um novo funcionário
def criar_funcionario(nomeFuncionario, codigo, setor, salario, cargaHoraria):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO funcionarios (nomeFuncionario, codigo, setor, salario, cargaHoraria)
            VALUES (%s, %s, %s, %s, %s)
        """, (nomeFuncionario, codigo, setor, salario, cargaHoraria))
        conexao.commit()
        return jsonify({"message": "Funcionário cadastrado com sucesso"}), 201
    except Exception as erro:
        conexao.rollback()
        return jsonify({"error": str(erro)}), 500
    finally:
        cursor.close()
        conexao.close()

# Função para listar todos os funcionários
def listar_funcionarios():
    try:
        conexao = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="sua_senha", 
            database="loja"
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()
        return funcionarios
    except mysql.connector.Error as erro:
        print(f"Erro ao acessar o banco de dados: {erro}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()


# Função para buscar um funcionário específico
def buscar_funcionario(codigo):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM funcionarios WHERE codigo = %s", (codigo,))
        funcionario = cursor.fetchone()
        if funcionario:
            funcionario_dict = {"codigo": funcionario[0], "nomeFuncionario": funcionario[1], "setor": funcionario[2], "salario": funcionario[3], "cargaHoraria": funcionario[4]}
            return jsonify(funcionario_dict), 200
        else:
            return jsonify({"error": "Funcionário não encontrado"}), 404
    except Exception as erro:
        return jsonify({"error": str(erro)}), 500
    finally:
        cursor.close()
        conexao.close()

# Função para atualizar as informações de um funcionário
def atualizar_funcionario(codigo, nomeFuncionario, setor, salario, cargaHoraria):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        # Recupera os valores atuais do funcionário se não forem fornecidos
        cursor.execute("SELECT nomeFuncionario, setor, salario, cargaHoraria FROM funcionarios WHERE codigo = %s", (codigo,))
        funcionario_atual = cursor.fetchone()

        if not funcionario_atual:
            return jsonify({"error": "Funcionário não encontrado"}), 404

        nomeFuncionario = nomeFuncionario if nomeFuncionario else funcionario_atual[0]
        setor = setor if setor else funcionario_atual[1]
        salario = salario if salario else funcionario_atual[2]
        cargaHoraria = cargaHoraria if cargaHoraria else funcionario_atual[3]

        cursor.execute(""" 
            UPDATE funcionarios
            SET nomeFuncionario = %s, setor = %s, salario = %s, cargaHoraria = %s
            WHERE codigo = %s
        """, (nomeFuncionario, setor, salario, cargaHoraria, codigo))

        conexao.commit()
        if cursor.rowcount > 0:
            return jsonify({"message": "Funcionário atualizado com sucesso"}), 200
        else:
            return jsonify({"error": "Funcionário não encontrado"}), 404
    except Exception as erro:
        conexao.rollback()
        return jsonify({"error": str(erro)}), 500
    finally:
        cursor.close()
        conexao.close()

# Função para deletar um funcionário
def deletar_funcionario(codigo):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE codigo = %s", (codigo,))
        conexao.commit()
        if cursor.rowcount > 0:
            return {"message": "Funcionário deletado com sucesso"}, 200
        else:
            return {"error": "Funcionário não encontrado"}, 404
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

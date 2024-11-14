def criar_tabelas(cursor):
    cursor.execute("""
        CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomeFuncionario VARCHAR(255) NOT NULL,
    codigo INT NOT NULL,
    setor VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    cargaHoraria INT NOT NULL
);
""")
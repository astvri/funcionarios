const apiUrl = 'http://127.0.0.1:5000/funcionarios';

// Função para listar funcionários
async function listarFuncionarios() {
    try {
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
            throw new Error("Erro ao buscar funcionários");
        }
        
        const funcionarios = await response.json();

        const tabela = document.querySelector('#funcionarios-tabela tbody');
        tabela.innerHTML = '';

        funcionarios.forEach(funcionario => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${funcionario.codigo}</td>
                <td>${funcionario.nomeFuncionario}</td>
                <td>${funcionario.setor}</td>
                <td>R$ ${funcionario.salario}</td>
                <td>${funcionario.cargaHoraria}h</td>
                <td>
                    <button class="editar btn btn-warning btn-sm" onclick="editarFuncionario(${funcionario.codigo})">Editar</button>
                    <button class="deletar btn btn-danger btn-sm" onclick="deletarFuncionario(${funcionario.codigo})">Deletar</button>
                </td>
            `;
            tabela.appendChild(row);
        });
    } catch (error) {
        console.error("Erro ao carregar funcionários:", error);
        alert("Erro ao carregar funcionários.");
    }
}

// Função para cadastrar um funcionário
document.querySelector('#form-funcionario').addEventListener('submit', async (event) => {
    event.preventDefault();

    const nomeFuncionario = document.querySelector('#nomeFuncionario').value;
    const codigo = document.querySelector('#codigoFuncionario').value;
    const setor = document.querySelector('#setorFuncionario').value;
    const salario = document.querySelector('#salarioFuncionario').value;
    const cargaHoraria = document.querySelector('#cargaHorariaFuncionario').value;

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nomeFuncionario, codigo, setor, salario, cargaHoraria })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || "Erro ao cadastrar funcionário");
        }

        const result = await response.json();
        alert(result.message || "Funcionário cadastrado com sucesso.");
        listarFuncionarios();
        document.querySelector('#form-funcionario').reset();
    } catch (error) {
        console.error("Erro ao cadastrar funcionário:", error);
        alert("Erro ao cadastrar funcionário.");
    }
});

// Função para deletar um funcionário
async function deletarFuncionario(codigo) {
    if (!confirm("Tem certeza de que deseja deletar este funcionário?")) return;

    try {
        const response = await fetch(`${apiUrl}/${codigo}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || "Erro ao deletar funcionário");
        }

        const result = await response.json();
        alert(result.message || "Funcionário deletado com sucesso.");
        listarFuncionarios();
    } catch (error) {
        console.error("Erro ao deletar funcionário:", error);
        alert("Erro ao deletar funcionário.");
    }
}

// Função para editar um funcionário
async function editarFuncionario(codigo) {
    const nomeFuncionario = prompt('Novo nome do funcionário:');
    const setor = prompt('Novo setor:');
    const salario = prompt('Novo salário:');
    const cargaHoraria = prompt('Nova carga horária:');

    if (nomeFuncionario && setor && salario && cargaHoraria) {
        try {
            const response = await fetch(`${apiUrl}/${codigo}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ nomeFuncionario, setor, salario, cargaHoraria })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "Erro ao editar funcionário");
            }

            const result = await response.json();
            alert(result.message || "Funcionário editado com sucesso.");
            listarFuncionarios();
        } catch (error) {
            console.error("Erro ao editar funcionário:", error);
            alert("Erro ao editar funcionário.");
        }
    } else {
        alert("Todos os campos são obrigatórios para editar o funcionário.");
    }
}

// Carregar a lista de funcionários ao carregar a página
document.addEventListener('DOMContentLoaded', listarFuncionarios);

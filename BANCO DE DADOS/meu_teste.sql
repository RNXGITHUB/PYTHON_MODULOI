-- Criar uma tabela de teste para alunos
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    curso TEXT
);

-- Inserir dados de teste
INSERT INTO alunos (nome, curso) VALUES ('Carlos Silva', 'Informática');
INSERT INTO alunos (nome, curso) VALUES ('Ana Maria', 'Administração');

-- Consultar os dados inseridos
SELECT * FROM alunos;*
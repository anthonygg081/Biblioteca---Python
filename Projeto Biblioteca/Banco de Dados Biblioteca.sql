-- 1. Criando o Banco de Dados
CREATE DATABASE biblioteca;
USE biblioteca;

-- 2. Tabela de Usuários
-- O nome do usuário será nossa Chave Primária (PK)
CREATE TABLE usuarios (
    nome_usuario VARCHAR(50) PRIMARY KEY,
    senha VARCHAR(100) NOT NULL
);

-- 3. Tabela de Livros Disponíveis
-- Apenas os livros que estão na estante
CREATE TABLE livros_disponiveis (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL
);

-- 4. Tabela de Livros Alugados
-- Esta tabela conecta o livro ao usuário
CREATE TABLE livros_alugados (
    id_aluguel INT AUTO_INCREMENT PRIMARY KEY,
    titulo_livro VARCHAR(100) NOT NULL,
    nome_usuario VARCHAR(50),
    data_aluguel TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    taxa_paga DECIMAL(5,2) DEFAULT 5.00,
    -- Chave Estrangeira: garante que o usuário exista na tabela 'usuarios'
    FOREIGN KEY (nome_usuario) REFERENCES usuarios(nome_usuario)
);
CREATE DATABASE PAPELARIA;

-----------------------------------------------------------
--              ENTIDADES E RELACIONAMENTOS              --
-----------------------------------------------------------
DROP TABLE IF EXISTS CLIENTES;              -- entidade [X]
DROP TABLE IF EXISTS CLIENTE_ADDRESS;       -- entidade [/]
DROP TABLE IF EXISTS FUNCIONARIO;           -- entidade [X]
DROP TABLE IF EXISTS ATENDENTE;             -- entidade [/]
DROP TABLE IF EXISTS ENTREGADOR;            -- entidade [/]
DROP TABLE IF EXISTS FUNCIONARIO_ADDRESS;   -- entidade [/]
DROP TABLE IF EXISTS FORNECEDORES;          -- entidade [/]
DROP TABLE IF EXISTS FORNECEDORES_ADDRESS;  -- entidade [/]
DROP TABLE IF EXISTS PRODUTOS;              -- entidade [X]
DROP TABLE IF EXISTS CATEGORIA;             -- entidade [X]
DROP TABLE IF EXISTS COMPRAS;               -- entidade [X]
DROP TABLE IF EXISTS ENTREGA;        -- relacionamentos [/]
DROP TABLE IF EXISTS CARRINHO;       -- relacionamentos [/]
DROP TABLE IF EXISTS GET_CATEGORIA;  -- relacionamentos [/]
DROP TABLE IF EXISTS GET_PRODUTO;    -- relacionamentos [/]
-----------------------------------------------------------
--                        TABELAS                        --
-----------------------------------------------------------
CREATE TABLE CLIENTES(
    id INTEGER PRIMARY KEY,
    cpf CHAR(11),
    nome VARCHAR(50),
    telefone1 CHAR(11),
    telefone2 CHAR(11)
);

CREATE TABLE CLIENTE_ADDRESS(
    CEP CHAR(8),
    logradouro VARCHAR(50),
    nro INTEGER,
    UF CHAR(2),
    cidade VARCHAR(50),
    bairro VARCHAR(50),
    pais VARCHAR(50),
    complemento VARCHAR(50),
    PRIMARY KEY(CEP, logradouro, nro)
);

CREATE TABLE FUNCIONARIO(
    id INTEGER PRIMARY KEY,
    cpf CHAR(11),
    nome VARCHAR(50),
    telefone1 CHAR(11),
    telefone2 CHAR(11)
);

CREATE TABLE ATENDENTE(
    id_atendimento INTEGER
);

CREATE TABLE ENTREGADOR(
    telefonePRO CHAR(11)
);

CREATE TABLE FUNCIONARIO_ADDRESS(
    CEP CHAR(8),
    logradouro VARCHAR(50),
    nro INTEGER,
    UF CHAR(2),
    cidade VARCHAR(50),
    bairro VARCHAR(50),
    pais VARCHAR(50),
    complemento VARCHAR(50),
    PRIMARY KEY(CEP, logradouro, nro)
);

CREATE TABLE FORNECEDORES(
    id INTEGER PRIMARY KEY,
    cnpj CHAR(0), -- verificar
    nome VARCHAR(50),
    telefone1 CHAR(10),
    telefone2 char(11)
);

CREATE TABLE FORNECEDORES_ADDRESS(
    CEP CHAR(8),
    logradouro VARCHAR(50),
    nro INTEGER,
    UF CHAR(2),
    cidade VARCHAR(50),
    bairro VARCHAR(50),
    pais VARCHAR(50),
    complemento VARCHAR(50),
    PRIMARY KEY(CEP, logradouro, nro)
);

CREATE TABLE PRODUTOS(
    codigo INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    descricao VARCHAR(500),
    qtde INTEGER,
    secao VARCHAR(50)
);

CREATE TABLE CATEGORIA(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    descricao VARCHAR(500)
);

CREATE TABLE COMPRAS(
    id_compra INTEGER PRIMARY KEY,
    data_de_compra DATE,
    preco FLOAT
);
-----------------------------------------------------------
CREATE TABLE CARRINHO(
    id_carrinho INTEGER PRIMARY KEY,
    item VARCHAR(50),
    qtde INTEGER,
    preco FLOAT
    data_de_compra DATE,
);

CREATE TABLE ENTREGA(
    id_entrega INTEGER,
    data_de_entrega DATE
);

CREATE TABLE GET_PRODUTO(

);

CREATE TABLE GET_CATEGORIA(

);

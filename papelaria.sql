CREATE DATABASE PAPELARIA;

-----------------------------------------------------------
--              ENTIDADES E RELACIONAMENTOS              --
-----------------------------------------------------------
DROP TABLE IF EXISTS CLIENTES;                 --  entidade
DROP TABLE IF EXISTS ENDERECO;                 --  entidade
DROP TABLE IF EXISTS PRODUTOS;                 --  entidade
DROP TABLE IF EXISTS CATEGORIA;                --  entidade
DROP TABLE IF EXISTS FORNECEDORES;             --  entidade
DROP TABLE IF EXISTS FUNCIONARIO;              --  entidade
DROP TABLE IF EXISTS ATENDENTE;                --  entidade
DROP TABLE IF EXISTS ENTREGADOR;               --  entidade
DROP TABLE IF EXISTS CARRINHO;           -- relacionamentos
DROP TABLE IF EXISTS PEDIDO;             -- relacionamentos
DROP TABLE IF EXISTS ENTREGA;            -- relacionamentos
DROP TABLE IF EXISTS GET_ENDERECO;       -- relacionamentos
DROP TABLE IF EXISTS GET_CATEGORIA;      -- relacionamentos

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

CREATE TABLE ENDERECO_CLIENTE(
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

CREATE TABLE CARRINHO( -- cliente compra produto(s)
    id_compra INTEGER PRIMARY KEY,
    data_de_compra DATE,
    preco FLOAT
);

CREATE TABLE FORNECEDORES(
    id INTEGER PRIMARY KEY,
    cnpj CHAR(0), -- verificar
    nome VARCHAR(50),
    telefone1 CHAR(10),
    telefone2 char(11)
);

CREATE TABLE PEDIDO( -- compra produtos do fornecedor
    id_pedido INTEGER PRIMARY KEY,
    item VARCHAR(50),
    qtde INTEGER,
    data_de_compra DATE,
    preco FLOAT
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

CREATE TABLE ENTREGA( -- entrega pedido ao cliente
    id_entrega INTEGER,
    data_de_entrega DATE
);

CREATE TABLE CATEGORIA(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    descricao VARCHAR(500)
);

CREATE TABLE GET_ENDERECO(

);

CREATE TABLE GET_CATEGORIA(

);
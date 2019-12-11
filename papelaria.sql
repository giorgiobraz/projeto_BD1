DROP DATABASE IF EXISTS PAPELARIA;
CREATE DATABASE PAPELARIA;
USE PAPELARIA;


-----------------------------------------------------------
--              ENTIDADES E RELACIONAMENTOS              --
-----------------------------------------------------------
DROP TABLE IF EXISTS CARRINHO;           -- relacionamentos
DROP TABLE IF EXISTS COMPRAS;                   -- entidade
DROP TABLE IF EXISTS CLIENTE_ADDRESS;           -- entidade
DROP TABLE IF EXISTS CLIENTES;                  -- entidade
DROP TABLE IF EXISTS ATENDENTE;                 -- entidade
DROP TABLE IF EXISTS ENTREGADOR;                -- entidade
DROP TABLE IF EXISTS FUNCIONARIO_ADDRESS;       -- entidade
DROP TABLE IF EXISTS FUNCIONARIO;               -- entidade
DROP TABLE IF EXISTS FORNECEDORES_ADDRESS;      -- entidade
DROP TABLE IF EXISTS FORNECEDORES;              -- entidade
DROP TABLE IF EXISTS PRODUTOS;                  -- entidade
DROP TABLE IF EXISTS CATEGORIA;                 -- entidade
DROP TABLE IF EXISTS ENTREGA;            -- relacionamentos
DROP TABLE IF EXISTS GET_PRODUTO;        -- relacionamentos
-----------------------------------------------------------
--                        TABELAS                        --
-----------------------------------------------------------
CREATE TABLE FUNCIONARIO(
    id INTEGER PRIMARY KEY,
    cpf CHAR(11),
    nome VARCHAR(50),
    telefone1 CHAR(11),
    telefone2 CHAR(11)
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
    id_funcionario INTEGER,
    FOREIGN KEY(id_funcionario) REFERENCES FUNCIONARIO(id) ON DELETE CASCADE,
    PRIMARY KEY(CEP, logradouro, nro, id_funcionario)
);

CREATE TABLE ATENDENTE(
    id_funcionario INTEGER,
    FOREIGN KEY(id_funcionario) REFERENCES FUNCIONARIO(id),
    PRIMARY KEY(id_funcionario)
);

CREATE TABLE ENTREGADOR(
    id_funcionario INTEGER,
    FOREIGN KEY(id_funcionario) REFERENCES FUNCIONARIO(id),
    PRIMARY KEY(id_funcionario)
);

CREATE TABLE CLIENTES(
    id INTEGER PRIMARY KEY,
    cpf CHAR(11),
    nome VARCHAR(50),
    telefone1 CHAR(11),
    telefone2 CHAR(11),
    id_atendente INTEGER,
    FOREIGN KEY(id_atendente) REFERENCES ATENDENTE(id_funcionario)
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
    id_cliente INTEGER,
    FOREIGN KEY(id_cliente) REFERENCES CLIENTES(id) ON DELETE CASCADE,
    PRIMARY KEY(CEP, logradouro, nro, id_cliente)
);

CREATE TABLE CATEGORIA(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50),
    descricao VARCHAR(500),
    CONSTRAINT PRIMARY KEY(id)
);

CREATE TABLE PRODUTOS(
    codigo INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    descricao VARCHAR(500),
    qtde INTEGER,
    secao VARCHAR(50),
    id_categoria INTEGER NOT NULL,
    CONSTRAINT FOREIGN KEY(id_categoria) REFERENCES CATEGORIA(id)
);

CREATE TABLE COMPRAS(
    id_compra INTEGER PRIMARY KEY,
    data_de_compra DATE,
    modalidade VARCHAR(20),
    preco FLOAT,
    id_cliente INTEGER,
    FOREIGN KEY(id_cliente) REFERENCES CLIENTES(id)
);

CREATE TABLE CARRINHO( -- compras N..N produtos
    id_compra INTEGER,
    id_produto INTEGER,
    item VARCHAR(50),
    qtde INTEGER,
    preco FLOAT,
    data_de_compra DATE,
    FOREIGN KEY(id_compra) REFERENCES COMPRAS(id_compra),
    FOREIGN KEY(id_produto) REFERENCES PRODUTOS(codigo),
    PRIMARY KEY(id_compra, id_produto)
);

CREATE TABLE FORNECEDORES(
    id INTEGER PRIMARY KEY,
    cnpj CHAR(14),
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
    id_fornecedores INTEGER,
    FOREIGN KEY(id_fornecedores) REFERENCES FORNECEDORES(id) ON DELETE CASCADE,
    PRIMARY KEY(CEP, logradouro, nro, id_fornecedores)
);

CREATE TABLE ENTREGA( -- cliente N..N entregador
    id_cliente INTEGER,
    id_funcionario INTEGER,
    data_de_entrega DATE,
    FOREIGN KEY(id_cliente) REFERENCES CLIENTES(id),
    FOREIGN KEY(id_funcionario) REFERENCES ENTREGADOR(id_funcionario),
    PRIMARY KEY(id_cliente, id_funcionario)
);

CREATE TABLE GET_PRODUTO( -- produtos N..N fornecedores
    id_fornecedores INTEGER,
    id_produto INTEGER,
    FOREIGN KEY(id_fornecedores) REFERENCES FORNECEDORES(id),
    FOREIGN KEY(id_produto) REFERENCES PRODUTOS(codigo),
    PRIMARY KEY(id_fornecedores, id_produto)
);

insert into CATEGORIA(nome, descricao) values('Livros', 'novo 1'), ('Escritório', 'novo 2'), ('Papelaria', 'novo 3');
insert into PRODUTOS(nome, descricao, qtde, secao, id_categoria) values('Livros', 'bla bla bla', '3', 'qualquer', 1);
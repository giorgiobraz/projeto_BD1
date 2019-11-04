# Projeto BD1

Implementação de um sistema de papelaria para o projeto final da disciplina de Banco de Dados 1 do curso Bacharelado em Ciência da Computação em 2019/2 (UTFPR-CM).

## Conteúdo do projeto

- Modelo relacional utilizando o MySQL Workbench
- Frameworks: Flask e Bootstrap 4
- `pip3 install pymysql`
- `pip3 install Flask==0.12.2`

## Criação do ambiente virtual com Virtualenv

### Instalação

`sudo pip3 install virtualenv`

### Inicializando um ambiente virtual

`mkdir <nome_do_diretório> && cd <nome_do_diretório>/`  
`virtualenv -p python3 .`

### Script de Ativação do ambiente virtual

`source bin/activate`

### Criação de arquivo com as dependências do sistema

`pip3 freeze >> requirements.txt`

### Instalação das dependências com o ambiente virtual ativo

`pip3 install -r requiremennts.txt`

### Como Desativar seu ambiente virtual

`deactivate`

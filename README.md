# Projeto BD1

Implementação de um sistema de papelaria para o projeto final da disciplina de Banco de Dados 1 do curso Bacharelado em Ciência da Computação em 2019/2 (UTFPR-CM).

## Principais tecnologias utilizadas

- Flask
- PyMySQL
- Bootstrap

---

## Crie um ambiente virtual

Primeiro, é preciso instalar uma ferramenta que permite isolar, do sistema operacional, um ambiente Python que contenha apenas os componentes necessários à aplicação. Para isso, vamos prosseguir com a instalação do _virtualenv_[^1]:  

`sudo pip3 install virtualenv`

Após a instalação, dentro do diretório criado para o projeto, a fim de inicializar o ambiente virtual, execute as instruções abaixo:  
`mkdir venv && cd venv/`  
`virtualenv -p python3 .`  
`cd ..`  

Agora basta ativar o ambiente virtual com o comando abaixo:  
`source venv/bin/activate`

Com o ambiente virtual ativo, instale as dependências:  
`pip3 install -r requiremennts.txt`

Para desativar o ambiente virtual, apenas use o comando:  
`deactivate`

---

## Execute a aplicação






[^1]: https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais
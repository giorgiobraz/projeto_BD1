import pymysql

###################################################################################
# 								    CRUD CATEGORIAS
###################################################################################
class Categorias:
	def __init__(self, nome, descricao):
		self.nome = nome
		self.descricao = descricao


# Estabelece conexao Categoria

	def estabelece_conexao(self, database="papelaria"):
		return pymysql.connect(host="localhost", user='novousuario', password='password', db=database)

# Create Categoria
	def nova_categoria(self, nome, descricao):
		connection = self.estabelece_conexao()

		if not connection.open:
			return False
		try:
			query = "insert into CATEGORIA(nome, descricao) values(%s, %s);"

			with connection.cursor() as cursor:
					cursor.execute(query, (nome, descricao))
					connection.commit()
					return True
		except Exception as e:
			print('Não foi possível estabelecer conexao',e)
			return False
		finally:
			connection.close()

# Select Categoria
	def get_all_categoria(self):
		connection = self.estabelece_conexao()
		
		if not connection.open:
			print('conexao !open')
		
		try:
			with connection.cursor() as cursor:
				query = "select * from CATEGORIA"
				cursor.execute(query)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()


# Update Categoria
	def edit_nome_categoria(self, id, nome, descricao):
		connection = self.estabelece_conexao()
		try:
			query = "update CATEGORIA set nome=%s, descricao=%s WHERE id=%s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, descricao, id))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()


# Delete Categoria 

	def rm_categoria(self, id):
		connection = self.estabelece_conexao()
		try:
			query = "delete from CATEGORIA where id = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, id)
				connection.commit()
				return True
		except Exception as e:
			return False
		finally:
			connection.close()


###################################################################################
# 								 	 CRUD PRODUTOS
###################################################################################
class Produtos:
	def __init__(self, nome, descricao, qtde, secao, id_categoria):
		self.nome = nome
		self.descricao = descricao
		self.qtde = qtde
		self.secao = secao
		self.id_categoria = id_categoria

# Estabelece conexao Produtos
	def estabelece_conexao(self, database="papelaria"):
		return pymysql.connect(host="localhost", user='novousuario', password='password', db=database)


# Create Produtos
	def novo_produto(self, nome, descricao, qtde, secao, id_categoria):
		connection = self.estabelece_conexao()

		if not connection.open:
			return False
		try:
			query = "insert into PRODUTOS(nome, descricao, qtde, secao, id_categoria) values(%s, %s, %s, %s, %s);"

			with connection.cursor() as cursor:
					cursor.execute(query, (nome, descricao, qtde, secao, id_categoria))
					connection.commit()
					return True
		except Exception as e:
			print('Não foi possível estabelecer conexao',e)
			return False
		finally:
			connection.close()


# Select Produtos
	def get_all_produtos(self):
		connection = self.estabelece_conexao()
		
		if not connection.open:
			print('conexao !open')
		
		try:
			with connection.cursor() as cursor:
				query = "select * from PRODUTOS"
				cursor.execute(query)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

# # Select nome categorias
# 	def get_nome_categorias(self, id_categoria):
# 		connection = self.estabelece_conexao()
		
# 		if not connection.open:
# 			print('conexao !open')
		
# 		try:
# 			with connection.cursor() as cursor:
# 				query = "select nome from CATEGORIA where id=%s;"
# 				cursor.execute(query)
# 				return cursor.fetchall()
# 		except Exception as e:
# 			print(e)
# 		finally:
# 			connection.close()


# Update Produtos
	def edit_nome_produto(self, id, nome, descricao, qtde, secao, id_categoria):
		connection = self.estabelece_conexao()
		try:
			query = "update PRODUTOS set nome=%s, descricao=%s, qtde=%s, secao=%s, id_categoria=%s WHERE codigo=%s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, descricao, qtde, secao, id_categoria, id))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()


# Delete Produtos 

	def rm_produto(self, id):
		connection = self.estabelece_conexao()
		try:
			query = "delete from PRODUTOS where id = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, id)
				connection.commit()
				return True
		except Exception as e:
			return False
		finally:
			connection.close()
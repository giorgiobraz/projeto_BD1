import pymysql

# ------------------------ Entidades ----------------------- #
class Categorias:
	def __init__(self, nome, descricao):
		self.nome = nome
		self.descricao = descricao

# ------------------- Estabelece Conexao ------------------- #
	def estabelece_conexao(self, database="papelaria"):
		return pymysql.connect(host="localhost", user='novousuario', password='password', db=database)

# ------------------------- Create ------------------------- #
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
	# Sua exceção tá generica.. pode ocorrer erros na hr de inserir e a mensagem será sobre a conexão #################################333
			print('Não foi possível estabelecer conexao',e)
			return False
		finally:
			connection.close()

# ------------------------- Select ------------------------- #
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
	# vc podia retornar alguma coisa pra indicar que a query foi falha... ou dar um raise em exceção ##########################################
			print(e)
		finally:
			connection.close()

# ------------------------- Update ------------------------- #
	def edit_nome_categoria(self, id, nome, descricao):
		connection = self.estabelece_conexao()
		try:
			query = "update CATEGORIA set nome = %s where id = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, id))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

# ------------------------- Delete ------------------------- #
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

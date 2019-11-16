import pymysql

# ------------------------ Entidades ----------------------- #
class Categorias:
    def __init__(self, id, nome, descricao):
        self.id = id # automatizar !!!
        self.nome = None
        self.descricao = None

# class Produtos:
#     def __init__(self, codigo, nome, descricao, qtde, secao, id_categoria):
#         self.codigo = # automatizar !!!
#         self.nome = None
#         self.descricao = None
#         self.qtde = qtde
#         self.secao = None
#         self.id_categoria = None # FK

# ------------------- Estabelece Conexao ------------------- #
	def estabelece_conexao(self, database="papelaria"):
		return pymysql.connect(host="localhost", user="UserName",           passwd="Password", db=database)

# ------------------------- Create ------------------------- #
	def nova_categoria(self, nome, descricao):
		connection = self.estabelece_conexao()
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

# ------------------------- Select ------------------------- #
	def get_all_categoria(self):
			connection = self.estabelece_conexao()
			try:
				with connection.cursor() as cursor:
					query = "select * from CATEGORIA"
					cursor.execute(query)
					return cursor.fetchall()
			except Exception as e:
				print(e)
			finally:
				connection.close()

# ------------------------- Update ------------------------- #
	def edit_nome_categoria(self, idCli=None, nome = None):
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

# ------------------------- Update ------------------------- #
	def edit_descricao_categoria(self, idCli=None, nome = None):
		connection = self.estabelece_conexao()
		try:
			query = "update CATEGORIA set descricao = %s where id = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (descricao, id))
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

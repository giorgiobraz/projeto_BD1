import pymysql

# ------------------------ Entidades ----------------------- #
class Categorias:
    def __init__(self, id, nome, descricao):
        self.id = id # Remover IDs (implementar auto_increments no SQL)
        self.nome = None # None aqui mesmo?? ############################### 
        self.descricao = None # None aqui mesmo?? ############################### 

# class Produtos:
#     def __init__(self, codigo, nome, descricao, qtde, secao, id_categoria):
#         self.codigo = # automatizar !!!
#         self.nome = None
#         self.descricao = None
#         self.qtde = qtde
#         self.secao = None
#         self.id_categoria = None # FK

# ------------------- Estabelece Conexao ------------------- #
	def estabelece_conexao(self, database="papelaria"): # essa linha tu vai ter que refazer ela em todas as proximas classes... se quiser melhorar isso crie uma classe pai que faz essa operação... e todas as demais vão herdar dela ################################################
		return pymysql.connect(host="localhost", user="UserName",           passwd="Password", db=database)

# ------------------------- Create ------------------------- #
	def nova_categoria(self, nome, descricao):
		connection = self.estabelece_conexao()
		# a connection não necessariamente pode funcionar sempre... vc poderia verificar antes de tentar fazer a query
		# if not connection.open():
			# return False
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
	def edit_nome_categoria(self, idCli=None, nome = None): # eu acho que nenhum desses parametros é opcional... entao tirar o " = None", vc nao trata isso no codigo... ###########################################
		connection = self.estabelece_conexao()
		try:
			query = "update CATEGORIA set nome = %s where id = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, id)) # Aqui tinha que ser idCli.. não? ################################################
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
				cursor.execute(query, (descricao, id)) # Aqui tinha que ser idCli.. não? ################################################
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

# ------------------------- Delete ------------------------- #
	def rm_categoria(self, id): # Matenha um padrao nos parametros.. aqui tá id, em outros lugares idCli ################################################
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

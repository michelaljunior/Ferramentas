# -*- coding: utf-8 -*-

from Modulos import *

banco = sqlite3.connect('base.db')
cursor = banco.cursor()

class PyCrud():
	def __init__(self):
		while True:
			os.system('cls')
			menu = int(input("""
		
		[ PYCRUD V0.1 ]
		
	[1] - Cadastrar Registros
	[2] - Consultar Registros
	[3] - Alterar Registros
	[4] - Deletar Registros
	
	[5] - Sair
		
> """))
			if menu == 1:
				self.Cadastrar()
			elif menu == 2:
				self.Consultar()
			elif menu == 3:
				self.Alterar()
			elif menu == 4:
				self.Deletar()
			elif menu == 5:
				break
		
	def Cadastrar(self):
		os.system('cls')
		print('\t[\tCadastrar Cliente\t]')
		
		nome = input('Nome: ')
		cpfcnpj = input('CPF ou CNPJ: ')
		email = input('E-mail: ')
		produto = input('Produto: ')
		telefone = input('Telefone: ')
		cadastro = str(datetime.now())[:19]
		modificacao = str(datetime.now())[:19]
		
		
		cursor.execute(f"""
		INSERT INTO clientes (
			'nome', 
			'CPF/CNPJ', 
			'email', 
			'produto', 
			'telefone',
			'cadastro', 
			'modificacao') VALUES ('{nome}','{cpfcnpj}','{email}','{produto}','{telefone}','{cadastro}','{modificacao}')
		""")
		banco.commit()
		
	def Consultar(self):
		os.system('cls')
		menu = int(input("""
			\t[\t Consulta de registros\t]
			
			[1] - Consulta sem filtro
			[2] - Consulta por nome Cadastrado
			[3] - Consulta por cpf ou cnpj
		
			[4] - Sair
> """))
		if menu == 1:
			cursor.execute('SELECT * FROM clientes')
			for registros in cursor.fetchall():
				print(registros)
			input()
		elif menu == 2:
			print('Em dev!')
		elif menu == 3:
			print('Em dev!')
		else:
			pass
		
	def Alterar(self):
		pass
	def Deletar(self):
		pass
		
if __name__ == '__main__':
	PyCrud()
	banco.close()
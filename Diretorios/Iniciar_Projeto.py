# -*- coding: utf-8 -*-

from Modulos import *

class Programa_Principal():
	def __init__(self, Janela):
		def Sair():
			self.Janela.destroy()
			
		self.Janela = Janela
		
		self.menubar = Menu(self.Janela)
		self.Janela.config(menu=self.menubar)
		
		
		self.Menu_1 = Menu(self.menubar)
		self.Menu_2 = Menu(self.menubar)
		self.Menu_3 = Menu(self.menubar)
		
		self.menubar.add_cascade(label='Janela', menu=self.Menu_1)	
		self.menubar.add_cascade(label='Arquivo', menu=self.Menu_2)
		self.menubar.add_cascade(label='Sobre', menu=self.Menu_3)
		
		self.Menu_1.add_command(label='Sair', command=Sair)
		self.Menu_2.add_command(label='Selecionar diretório', command=self.ProcurarDiretorio)
		self.Menu_3.add_command(label='Ajuda')
		self.Menu_3.add_command(label='Sobre Nós')
		# Bloco 1
		
		self.Label_Campo_Nome = Label(self.Janela, text='Nome do projeto:', font=fonttext)
		self.Campo_Nome = Entry(self.Janela, bd=1, relief=SOLID, highlightbackground='#000', font=fontlight)
		
		# SubBloco 1
		self.Label_Adicionais = Label(self.Janela, text='Adicionais:',font=fonttext)
		self.Frame_Adicionais = Frame(self.Janela, bd=1, relief=SOLID, highlightbackground='#000')
		self.Crud = IntVar()
		self.Campo_Crud = Checkbutton(self.Janela, text='CRUD', variable=self.Crud, font=fonttext)
		
		# Bloco 2
		
		self.Label_Campo_Local = Label(self.Janela, text='Local para criar diretório do projeto:', font=fonttext)
		self.Campo_Local = Entry(self.Janela, bd=1, relief=SOLID, highlightbackground='#000', font=fontlight)
		self.Botao_Pesquisar = Button(self.Janela, bd=1, text='Selecionar diretório', relief=SOLID, bg='#FFFF00', highlightbackground='#000', font=fontlight, command=self.ProcurarDiretorio)
		
		# Rodape
		self.Label_Rodape = Label(self.Janela, text='Erno Soluções (C) 2020', font=fonttext)
		
		# Posicionamento dos widghts
		
		self.Label_Campo_Nome.place(x=10, y=11)
		self.Campo_Nome.place(x=10, y=35, width=200, height=35)
		
		self.Label_Adicionais.place(x=220, y=11)
		self.Frame_Adicionais.place(x=220, y=35, width=300, height=35)
		self.Campo_Crud.place(x=230, y=38)
		
		self.Label_Campo_Local.place(x=10, y=100)
		self.Campo_Local.place(x=10, y=125, width=420, height=40)
		self.Botao_Pesquisar.place(x=440, y=125, width=150, height=40)
		
		self.Label_Rodape.place(x=425, y=555)
		self.Janela.mainloop()
		
	def CriarDiretorios(self, Diretorio, NomeProjeto):
		if str(self.CampoLocal.get()) == '':
			print('Preencha todos os campos')
		else:
			Rodar_shell(f'mkdir {Diretorio}/{NomeProjeto}')
	def ProcurarDiretorio(self):
		self.Campo_Local.delete('0', END)
		LocalDiretorio = filedialog.askdirectory(title = 'Informe o local para iniciar o projeto')
		self.Campo_Local.insert(END, LocalDiretorio)
		
Janela = Tk()
Janela.geometry('600x600')
Janela.title('Erno Soluções - Criar diretorios')
Janela.iconphoto(False, PhotoImage(file = 'Modulos/Icones/logo.png') )
Janela.resizable(0,0)

fonttext = 'Raleway 11'
fontlight = 'Raleway 10'

if __name__ == '__main__':
	Programa_Principal(Janela)

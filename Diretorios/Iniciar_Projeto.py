# -*- coding: utf-8 -*-
# Versao: 1
# Desenvolvido por Michel Anderson
# Data Ultima alteração 05/02/2020
# Erno Soluções © 2020

from Modulos import *

class Programa_Principal():
	def __init__(self, Janela):
		def Sair():
			self.Janela.destroy()
			
		self.Janela = Janela
		self.Janela.configure(bg='#fff')
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
		
		self.Label_Campo_Nome = Label(self.Janela, bg='#fff', text='Nome do projeto:', font=fonttext)
		self.Campo_Nome = Entry(self.Janela, bd=1, relief=SOLID, highlightbackground='#000', font=fontlight)
		
		# SubBloco 1
		self.Label_Adicionais = Label(self.Janela, bg='#fff', text='Adicionais:',font=fonttext)
		self.Frame_Adicionais = Frame(self.Janela, bg='#fff', bd=1, relief=SOLID, highlightbackground='#000')
		self.Crud = IntVar()
		self.Campo_Crud = Checkbutton(self.Janela, bg='#fff', text='CRUD', variable=self.Crud, font=fonttext)
		self.Node = IntVar()
		self.Campo_Node = Checkbutton(self.Janela, bg='#fff', text='NodeJs', variable=self.Node, font=fonttext)
		
		# Bloco 2
		
		self.Label_Campo_Local = Label(self.Janela, bg='#fff', text='Local para criar diretório do projeto:', font=fonttext)
		self.Campo_Local = Entry(self.Janela, bd=1, relief=SOLID, highlightbackground='#000', font=fontlight)
		self.Botao_Pesquisar = Button(self.Janela, bd=1, text='Selecionar diretório', relief=SOLID, bg='#FFFF00', highlightbackground='#000', font=fontlight, command=self.ProcurarDiretorio)
		
		# Bloco 3
		self.Botao_Processar = Button(self.Janela, bd=1, text='Criar Projeto', relief=SOLID, bg='#32CD32', highlightbackground='#000', font=fontlight, command=self.CriarDiretorios)
		
		# Rodape
		self.Label_Rodape = Label(self.Janela, bg='#fff', text='Erno Soluções (C) 2020', font=fonttext)
		self.Label_Progresso = Label(self.Janela, bg='#fff', text='Insira as informações', font=fonttext)
		
		# Posicionamento dos widghts
		
		self.Label_Campo_Nome.place(x=10, y=11)
		self.Campo_Nome.place(x=10, y=35, width=200, height=35)
		
		self.Label_Adicionais.place(x=220, y=11)
		self.Frame_Adicionais.place(x=220, y=35, width=300, height=35)
		self.Campo_Crud.place(x=230, y=38)
		self.Campo_Node.place(x=300, y=38)
		
		self.Label_Campo_Local.place(x=10, y=100)
		self.Campo_Local.place(x=10, y=125, width=420, height=40)
		self.Botao_Pesquisar.place(x=440, y=125, width=150, height=40)
		
		self.Botao_Processar.place(x=10, y=500, width=150, height=40)
		
		self.Label_Progresso.place(x=10, y=555)
		self.Label_Rodape.place(x=425, y=555)
		
		self.Janela.mainloop()
		
	def CriarDiretorios(self):
		Diretorio = Substituir('/','\\\\', str(self.Campo_Local.get()))
		NomeProjeto = str(self.Campo_Nome.get())
		print(NomeProjeto)
		if Diretorio == '' or NomeProjeto == '':
			print('Preencha todos os campos')
		else:
			try:
				os.mkdir(f'{Diretorio}\\{NomeProjeto}')
				
				self.Label_Progresso.configure(text="Criando Diretorios...")
				
				os.mkdir(f'{Diretorio}\\{NomeProjeto}\\Js')
				os.mkdir(f'{Diretorio}\\{NomeProjeto}\\Html')
				os.mkdir(f'{Diretorio}\\{NomeProjeto}\\Estilo')
				os.mkdir(f'{Diretorio}\\{NomeProjeto}\\Estilo\\Imagens')
				os.mkdir(f'{Diretorio}\\{NomeProjeto}\\Estilo\\Imagens\\Icones')
				os.mkdir(f'{Diretorio}\\{NomeProjeto}\\Estilo\\Fontes')
				
				self.Label_Progresso.configure(text="Criando Arquivos...")
				
				if self.Node.get() == 1:
					padraopackge = {
						"name": f"{NomeProjeto}",
						"version": "0.1",
						"description": "",
						"Create by": "Erno Solucoes",
						"main": "Js/Controlador.js",
						"scripts": {
							"start": "electron ."
						},
						"devDependencies": {
							"electron": "^7.1.9"
						}
					}
					
					Arquivo = open(f'{Diretorio}/{NomeProjeto}/package.json', 'a')
					Arquivo.write(str(padraopackge))
					self.Label_Progresso.configure(text="Escrevendo package.json...")
					Arquivo.close()
					js = '''// Todos os direitos a Erno Soluções 
const {app, BrowserWindow} = require('electron');

let Janela

function CriarJanela () {
	Janela = new BrowserWindow(
		{
			width: 1000,
			height: 600,
			webPreferences: {nodeIntegration: true},
			//frame: false,
		});

	Janela.loadFile('Html/Login/index.html');
	//Janela.setMenu(null);
};

app.on('ready', CriarJanela);
'''
					arquivo = open(f'{Diretorio}\\{NomeProjeto}\\Js\\Controlador.js', 'w')
					arquivo.write(js)
					arquivo.close()
				
				self.Label_Progresso.configure(text="Fim!")
			except Exception as erro:
				self.Label_Progresso.configure(text="Algo errado aconteceu!")
				print(erro)
			
			
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
	os.system('rmdir Modulos/__pycache__/')
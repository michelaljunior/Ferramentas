# -*- coding: utf-8 -*-
# Versao: Testing
# Desenvolvido por Michel Anderson
# Data da ultima alteração 06/02/2020
# Erno Soluções © 2020

import json
import os
import requests

Descobrir = 'https://prod-s0-webapp-proxy.nubank.com.br/api/discovery'
DescobrirApp = 'https://prod-s0-webapp-proxy.nubank.com.br/api/app/discovery'

Cabecalho = {
	'Content-Type': 'application/json;charset=UTF-8',
	'X-Correlation-Id': 'WEB-APP.pewW9',
	'User-Agent': 'Erno Nubpyapi',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
	'Connection': 'keep-alive',
	'DNT': '1',
	'Host': 'prod-s0-webapp-proxy.nubank.com.br',
	'Origin': 'https://app.nubank.com.br',
	'Referer': 'https://app.nubank.com.br/'
}

# Pega o json com sessao

request = requests.get(Descobrir, headers=Cabecalho)
proxy = json.loads(request.content.decode('utf-8'))
request = requests.get(DescobrirApp, headers=Cabecalho)
proxyApp = json.loads(request.content.decode('utf-8'))

# Pega o link junto com a sessao para o usuario poder logar
LinkLogar = proxy['login']

class NuConta():
	def Logar(usuario, senha):
	
		# Passa as informações necessarias para o nubank realizar o login
		# Precisa alterar o "client_secret" para logar,

		Informacoes = { "grant_type": "password", "login": usuario, "password": senha, "client_id": "other.conta", "client_secret": "yQPeLzoHuJzlMMSAjC-LgNUJdUecx8XO" }
		Resposta = requests.post(LinkLogar, json=Informacoes, headers=Cabecalho)

		if Resposta.status_code != 200:
			Dados = f'Erro de execução HTTP!\nCODE: {Resposta.status_code}\nURL: {Resposta.url}\nResposta: {Resposta.json()}'
		else:
			Dados = Resposta.json()

		return Dados
		
if __name__ == '__main__':
	print(NuConta.Logar('usuario', 'senha'))
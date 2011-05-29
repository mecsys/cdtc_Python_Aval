#-*- coding: UTF-8 -*-
import sys

def imprimeValores(foo, boo):
	"""
	Função de apoio, imprime o resultado do processamento.
	"""
	print("%d nota(s) de %d reais" % (foo, boo))

def calculaNotas(valor):
	"""
	Função para processamento de saque.
	
	OBS.: Como hoje é domingo, preparei esta versão bem simples, 
	para não perder o prazo de entrega."

	IMPORTANTE: 
	 Utilizei Python 2.x.x, pois o resultado
	 de divisão são números inteiros. Já em Python 3.x.x o resultado de
	 divisão são números floats.
	 Isto poderia interferir nos resultados, se não convertidos os 
	 resultados das divisãoes em inteiros.
	"""
	valor = int(valor)
	
	if (valor <= 0):
		print("Saldo negativo: %d" % valor)
		sys.exit()

	if (int(valor / 100) > 0):
		spam = int(valor / 100)
		imprimeValores(spam, 100)
		valor = valor - (spam * 100)

	if (int(valor / 50) > 0):
		spam = int(valor / 50)
		imprimeValores(spam, 50)
		valor = valor - (spam * 50)
	
	if (int(valor / 10) > 0):
		spam = int(valor / 10)
		imprimeValores(spam, 10)
		valor = valor - (spam * 10)

	if (int(valor / 5) > 0):
		spam = int(valor / 5)
		imprimeValores(spam, 5)
		valor = valor - (spam * 5)

	if (int(valor / 1) > 0):
		spam = int(valor / 1)
		imprimeValores(spam, 1)
		valor = valor - (spam * 1)

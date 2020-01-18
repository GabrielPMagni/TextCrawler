#try:
nome_arquivo = input('Digite o nome do arquivo a ser analizado com sua extensão: \n\n\t>')
arquivo = open(nome_arquivo, 'r')
try:
	num_palavras = int(input('Quantas palavras-chave deseja procurar no arquivo: '))
except ValueError:
	print('Valor inválido, por favor digite número inteiros.')
palavras = []
palavras_fim = []
for i in range(num_palavras):
	if i <= 0:
		item1 = input(f'{i+1}ª palavra-chave a ser buscada:\n\n\t>')
		palavras.append(item1)
		item2 = input(f'Final da {i+1}ª palavra-chave a ser buscada OU \"-1-\" para até o próximo espaço:\n\n\t>')
		palavras_fim.append(item2)
	else:
		item1 = input(f'{i+1}ª palavra-chave a ser buscada:\n\n\t>')
		palavras.append(item1)
		item2 = input(f'Final da {i+1}ª palavra-chave a ser buscada OU \"-1-\" para até o próximo espaço:\n\n\t>')
		palavras_fim.append(item2)
for linha in arquivo:
	counter = 0
	for palavra in linha.split():
		try:
			palavra_index = []
			palavra_fim_index = []
			item1 = palavra.find(palavras[counter])
			palavra_index.append(item1)
			#--------------------
			item2 = palavra.rfind(palavras_fim[counter])
			palavra_fim_index.append(item2)

		except Exception as erro:
			print('\n\nErro #00000001: ' + str(erro))
		finally:
			counter = -1
			if palavra_index[counter] == -1:
				pass
			else:
				#try:
				for palavra in linha.split():
					arquivo_res = open('resultado.txt', 'a')
					if palavras_fim[counter] != '-1-':
						counter+=1
						if counter >= len(palavra_index):
							pass
						else:
							if counter >= len(palavra_fim_index):
								pass
							else:
								string = (palavra[palavra_index[counter] + len(palavras[counter]): palavra_fim_index[counter]] + '	')
								arquivo_res.write(string)
					else:
						if counter >= len(palavra_index):
							pass
						else:
							if counter >= len(palavra_fim_index):
								pass
							else:
								string = (palavra[palavra_index[counter] + len(palavras[counter]): -1] + '	')
								arquivo_res.write(string)
					arquivo_res.write('\n')
			'''
			except Exception as erro:
				print('\n\nErro #00000002: ' + str(erro))
			'''
		"""if palavra2_index == -1:
			pass
		else:
			try:
				arquivo_res = open('resultado.txt', 'a')
				if palavra_fim2 == '-1-':
					arquivo_res.write(palavra[palavra2_index + len(palavra2): -1] + '\n')
				else:
					arquivo_res.write(palavra[palavra2_index + len(palavra2):palavra_fim2] + '\n')
			except Exception as erro:
				print('\n\nErro #00000003: ' + str(erro))
		"""
print('Processo ocorreu com sucesso, confira o arquivo \"resultado.txt\" para verificar resultados.\n\nPara colocar em uma planilha, apenas abra o arquivo no Excel ou LibreOffice Calc e escolha separações por \"Tabulação\"\n\n')
'''			
except Exception as erro:
	print('\n\nErro #00000000: ' + str(erro))
finally:
	print('\n\nFinalizando aplicação e fechando arquivos relacionados')
	arquivo.close()
	arquivo_res.close()
	print('\n\nOk')
'''
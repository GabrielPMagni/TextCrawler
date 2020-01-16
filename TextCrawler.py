try:
	nome_arquivo = input('Digite o nome do arquivo a ser analizado com sua extensão: \n\n\t>')
	arquivo = open(nome_arquivo, 'r')
	palavra1 = input('1ª palavra-chave a encontrar: \n\n\t>')
	palavra_fim1 = input('Palavra-chave final da 1ª busca \nOU (\"-1-\" para final da palavra): \n\n\t>')
	palavra2 = input('2ª palavra-chave a encontrar: \n\n\t>')
	palavra_fim2 = input('Palavra-chave final da 2ª busca \nOU (\"-1-\" para final da palavra): \n\n\t>')
	for linha in arquivo:
		for palavra in linha.split():
			try:
				palavra1_index = palavra.find(palavra1)
				palavra1_fim_index = palavra.rfind(palavra_fim1)
				palavra2_index = palavra.find(palavra2)
			except Exception as erro:
				print('\n\nErro #00000001: ' + str(erro))

			if palavra1_index == -1:
				pass
			else:
				try:
					arquivo_res = open('resultado.txt', 'a')
					if palavra_fim1 == '-1-':
						arquivo_res.write(palavra[palavra1_index + len(palavra1): palavra1_fim_index] + '	')
					else:
						arquivo_res.write(palavra[palavra1_index + len(palavra1): -1] + '	')


				except Exception as erro:
					print('\n\nErro #00000002: ' + str(erro))

			if palavra2_index == -1:
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

	print('Processo ocorreu com sucesso, confira o arquivo \"resultado.txt\" para verificar resultados.\n\nPara colocar em uma planilha, apenas abra o arquivo no Excel ou LibreOffice Calc e escolha separações por \"Tabulação\"\n\n')
			
except Exception as erro:
	print('\n\nErro #00000000: ' + str(erro))
finally:
	print('\n\nFinalizando aplicação e fechando arquivos relacionados')
	arquivo.close()
	arquivo_res.close()
	print('\n\nOk')

import sys

# Variável para contar a qtdade de linhas
total = 0

for arquivo in sys.argv[1:]: # [1:] para pegar apenas os parâmetros
	# Abre o arquivo
	with open(arquivo, newline='') as arquivo_txt:
		linha = 0
		# Varre linha a linha
		for row in arquivo_txt:
			linha += 1
			print(f"Arquivo '{arquivo}' - Linha {linha}: {row}")

		# Incrementa o contador, depois que as linhas são lidas
		total += linha

print(f"Total lidos: {str(total)}")
print("FIM!")
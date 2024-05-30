# dados de criação de matriz 
matriz_entrada = input().split(" x ")
linhas, colunas = int(matriz_entrada[0]), int(matriz_entrada[1])
# inicializando a matriz
matriz =  [[0] * colunas for _ in range(linhas)]

# verficando a quantidade de elementos na matriz 
quantidade_elementos = int(input())

# colocando dados nela
for _ in range(quantidade_elementos):
    entrada = input().split()
    nivel_atratividade = int(entrada[0])
    posicao = entrada[1][1:-1].split(",")
    i, j = int(posicao[0]), int(posicao[1])
    matriz[i][j] = nivel_atratividade

operacao = input()
while operacao != "Fim":
    # Vamos Permutar
    if operacao == "Permutar":
            entrada = input().split()
            posicao1 = entrada[0][1:-1].split(",")
            posicao2 = entrada[1][1:-1].split(",")
            i1, j1 = int(posicao1[0]), int(posicao1[1])
            i2, j2 = int(posicao2[0]), int(posicao2[1])
            matriz[i1][j1], matriz[i2][j2] = matriz[i2][j2], matriz[i1][j1]
            
    # transpoe mais q tudo esse menino
    elif operacao == "Transposição":
        matriz = [[matriz[j][i] for j in range(linhas)] for i in range(colunas)]
        
    # eita como remove 
    elif operacao == "Remover":
        min_valor = 100000
        min_i, min_j = 0,0
        for i in range(linhas):
            for j in range(colunas):
                if matriz[i][j] != 0 and matriz[i][j] < min_valor:
                    min_valor = matriz[i][j]
                    min_i, min_j = (i, j)

        if min_valor:
          matriz[min_i][min_j] = 0
    
    operacao = input()

# printa printa printa printa
print("Atual Arranjo:")
for linha in matriz:
    print(" ".join(str(elemento) for elemento in linha))

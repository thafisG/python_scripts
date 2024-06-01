# lista auxiliar para guiar
lista_caracteres = ['B', 'C', 'L', 'M', 'T', 'P', 't']

# recebendo
casa_original = input()
casa_depois = input()

# tem nd mas é so pra iniciar
matriz_casa_original = []
matriz_casa_depois = []

# eita como gosta de iniciar com nada
moveis_original = []
moveis_depois = []

# agora sim iniciando de verdade
for i in range(0, 60, 10):
    linha_matriz = casa_original[i:i+10]
    matriz_casa_original.append(linha_matriz)

for i in range(0, 60, 10):
    linha_matriz = casa_depois[i:i+10]
    matriz_casa_depois.append(linha_matriz)

# as 10 mil opções de moveis, pq a diva é mt rica
cama_antes = []
cadeira_antes = []
lareira_antes = []
mesa_antes = []
tv_antes = []
planta_antes = []
tapete_antes = []

cama_depois = []
cadeira_depois = []
lareira_depois = []
mesa_depois = []
tv_depois = []
planta_depois = []
tapete_depois = []

# verificando cada movel e sua quantidade 
for caracter in casa_original:
    if caracter == "B":
        cama_antes.append(caracter)
    elif caracter == "C":
        cadeira_antes.append(caracter)
    elif caracter == "L":
        lareira_antes.append(caracter)
    elif caracter == "M":
        mesa_antes.append(caracter)
    elif caracter == "T":
        tv_antes.append(caracter)
    elif caracter == "P":
        planta_antes.append(caracter)
    elif caracter == "t":
        tapete_antes.append(caracter)

# verificando novamente depois que a bagunça aconteceu 
for caracter in casa_depois:
    if caracter == "B":
        cama_depois.append(caracter)
    elif caracter == "C":
        cadeira_depois.append(caracter)
    elif caracter == "L":
        lareira_depois.append(caracter)
    elif caracter == "M":
        mesa_depois.append(caracter)
    elif caracter == "T":
        tv_depois.append(caracter)
    elif caracter == "P":
        planta_depois.append(caracter)
    elif caracter == "t":
        tapete_depois.append(caracter)

# contabilizando todos os moveis antes x depois 
quantidade_original = len(cama_antes) + len(planta_antes) + len(tapete_antes) + len(lareira_antes) + len(tv_antes) + len(mesa_antes) + len(cadeira_antes)
quantidade_depois = len(cama_depois) + len(planta_depois) + len(tapete_depois) + len(lareira_depois) + len(tv_depois) + len(mesa_depois) + len(cadeira_depois)

# forzinho para analise dos moveis dentro da casinha
for linha in range(6):
    for coluna in range(10):
        caracter = matriz_casa_original[linha][coluna]
        if caracter in lista_caracteres:
            moveis_original.append([caracter, [linha, coluna]])
    
for linha in range(6):
    for coluna in range(10):
        caracter = matriz_casa_depois[linha][coluna]
        if caracter in lista_caracteres:
            moveis_depois.append([caracter, [linha, coluna]])

# iniciando variaveis para contabilizar 
mudado = 0 
removido = 0 
adicionado = 0

# variaveis especificar para os cases
planta_remo = 0 
tapete_remo = 0 

# verificar como ta as coisas nesta casita
# Verificando moveis adicionados 
if quantidade_original < quantidade_depois:
    for lista in range(quantidade_original+1):
        if len(cama_antes) < len(cama_depois):
            adicionado += 1
        elif len(cadeira_antes) < len(cadeira_depois):
            adicionado += 1
        elif len(lareira_antes) < len(lareira_depois):
            adicionado += 1
        elif len(mesa_antes) < len(mesa_depois):
            adicionado += 1
        elif len(tv_antes) < len(tv_depois):
            adicionado += 1
        elif len(planta_antes) < len(planta_depois):
            adicionado += 1
        elif len(tapete_antes) < len(tapete_depois):
            adicionado += 1

# Verificando remoção 
for movel in moveis_original:
    if movel not in moveis_depois:
        removido += 1
        if len(planta_antes) != len(planta_depois):
            planta_remo += 1
        if len(tapete_antes) != len(tapete_depois):
            tapete_remo += 1

mudou_b = 0
# Verificar mudanças de lugar
for i in range(6):
    for j in range(10):
        if matriz_casa_original[i][j] != matriz_casa_depois[i][j]:
            mudado += 1
            if matriz_casa_original[i][j] == "B":
                if matriz_casa_original[i][j] != matriz_casa_depois[i][j]:
                    mudou_b += 1

# vamos analisar se alguém mexeu nessa bagaça 
if adicionado >= 1 and mudado >= 2 and planta_remo == 1 and tapete_remo == 1:
    print("Caramba, a casa tá uma bagunça! Não sei quem foi o responsável.")
elif adicionado >= 3:
    print("Thomaz bagunçou a casa. Ele sempre enche a casa de bugiganga!!.")
elif planta_remo >= 1:
    print("Poxa, Pedro Elias! Não basta vender toda a plantação de melões, ainda quer vender minha planta??")
elif len(cama_depois) != 0 and len(cadeira_depois) == 0 and len(mesa_depois) == 0 and len(planta_depois) == 0 and len(lareira_depois) == 0 and len(tv_depois) == 0 and len(tapete_depois) == 0:
    print("CADÊ MEUS MÓVEIS?!?! SÓ FICOU A CAMA! Só pode ter sido Welton.")
elif mudado >= 5:
    print("João bagunçou a casa. Não aguento mais tudo fora do lugar! Toda vez isso.")
elif quantidade_original != quantidade_depois:
    print("Hum, tem algo diferente aqui... Deve ter sido só impressão minha.")
elif removido == 0 and adicionado == 0 and mudado == 0:
    print("Ufa! A casa tá do jeitinho que eu deixei.")

especies_eevee = ["Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon", "Glaceon", "Leafeon", "Sylveon"]

agua = ["Misty", "Gary", "Ivy", "Blanche"]
eletrico = ["Ash", "Ritchie", "Surge", "Spark"]
fogo = ["May", "Blaine", "Candela"]
psiquico = ["Agatha", "Sabrina", "Fantina"]
sombrio = ["Jessie", "James", "Giovanni"]
gelo = ["Lorelei", "Dawn"]
planta = ["Max", "Erika", "Tracey", "Mallow"]
fada = ["Whitney"]

# calculo para vê qual pokemon consegue evoluir 
def calculo_evolutivo_eevee(nome_tratado, idade):
    total = 0
    for caracter in nome_tratado:
        total += ord(caracter) - ord('a') + 1
    return (total * idade) % 8

# função para analise dos indices e decidir
def registro_treinador(nome_tratado, idade):
        
    if (nome_tratado in agua):
        return especies_eevee[0]
    elif (nome_tratado in eletrico):
        return especies_eevee[1]
    elif (nome_tratado in fogo):
        return especies_eevee [2]
    elif (nome_tratado in psiquico):
        return especies_eevee [3]
    elif (nome_tratado in sombrio):
        return especies_eevee[4]
    elif (nome_tratado in gelo): 
        return especies_eevee[5]
    elif (nome_tratado in planta):
        return especies_eevee[6]
    elif (nome_tratado in fada):
        return especies_eevee[7]
    else:
        eevee_index = calculo_evolutivo_eevee(nome_tratado, idade)
        return especies_eevee[eevee_index]


# quantidade de treinadores
qtd_treinadores = int(input())

# verificando cada nome e fazendo o tratamento para dar inicio a saida
for treinador in range(qtd_treinadores):
    entrada = input()
    # {NOME} - {IDADE} 
    nome, idade = entrada.split(" - ")
    nome_tratado = nome.capitalize()
    idade = int(idade)

    # chamando função
    evolution = registro_treinador(nome_tratado, idade)

    # saida desta belezura 
    if evolution == "Vaporeon":
        print(f"A evolução do Eevee de {nome_tratado} é para Vaporeon, o mestre das águas!")
    elif evolution == "Jolteon":
        print(f"O Eevee de {nome_tratado} evoluiu para Jolteon, cheio de energia elétrica!")
    elif evolution == "Flareon":
        print(f"O Eevee de {nome_tratado} se transformou em Flareon, dominando o calor do fogo!")
    elif evolution == "Espeon":
        print(f"Espeon é a evolução do Eevee de {nome_tratado}, mostrando sua mente brilhante!")
    elif evolution == "Umbreon":
        print(f"A evolução sombria do Eevee de {nome_tratado} é Umbreon, deslizando pelas sombras!")
    elif evolution == "Glaceon":
        print(f"Glaceon é o novo estágio do Eevee de {nome_tratado}, tão frio quanto o gelo!")
    elif evolution == "Leafeon":
        print(f"O Eevee de {nome_tratado} se transformou em Leafeon, um espírito da floresta!")
    elif evolution == "Sylveon":
        print(f"Sylveon é a evolução mágica do Eevee de {nome_tratado}, irradiando bondade e misticismo!")

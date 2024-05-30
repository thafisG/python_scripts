# lista auxiliares
locais_fechados = []
locais_abertos = []
suspeitos = []

# lista estilo matriz mt bacana e chique e conceitual 
locais_possiveis = [
    ["Torre do Mago", 700, [6.00, 23.99]],
    ["Rancho da Marnie", 260, [9.00, 16.00]],
    ["Saloon", 1200, [12.00, 23.99]],
    ["Armazém do Pierre", 1100, [9.00, 17.00]],
    ["Casa do Prefeito", 1500, [8.00, 22.00]],
    ["Peixaria", 1900, [9.00, 17.00]],
    ["Museu", 1870, [8.00, 18.00]],
    ["Ferreiro", 1700, [9.00, 16.00]],
    ["Mercado Joja", 1800, [9.00, 23.00]],
    ["Carpintaria", 1500, [9.00, 17.00]],
    ["Minas", 1850, [0.00, 23.99]],
    ["Centro Comunitário", 1300, [0.00, 23.99]]
]

for pessoa in range(6):
    # dados principais
    dados_pessoa = input()
    nome_pessoa, horario_pessoa, nome_local = dados_pessoa.split(" - ")
    # calculando o horario desse cidadão de bem em horas
    horario_pessoa = float(horario_pessoa.replace(":", "."))
    suspeitos.append({"nome": nome_pessoa, "horario": horario_pessoa, "local": nome_local})

# analise dos locais dos meliantes 
locais_pessoas = [suspeito["local"] for suspeito in suspeitos]

# Verificação de locais invi (invisivel)
locais_invalidos = []

for local in locais_pessoas:
    local_existente = False
    for possivel in locais_possiveis:
        if possivel[0] == local:
            local_existente = True

    if not local_existente:
        locais_invalidos.append(local)

if len(locais_invalidos) == 1:
    nome_suspeito = ""
    for suspeito in suspeitos:
        if suspeito["local"] == locais_invalidos[0]:
            nome_suspeito = suspeito["nome"]  
    print(f"Esse lugar {locais_invalidos[0]} nem existe! {nome_suspeito} foi quem roubou os melões!")
elif len(locais_invalidos) > 1:
    nomes_invalidos = ([suspeito["nome"] for suspeito in suspeitos if suspeito["local"] in locais_invalidos])

    locais_invalidos.sort()
    nomes_invalidos.sort()
    print(f"{', '.join(locais_invalidos)} nem existem! {', '.join(nomes_invalidos)} roubaram os melões!")
else:
    # Análise de horario dos cara
    locais_abertos = []
    locais_fechados = []
    for suspeito in suspeitos:
        local = [possivel for possivel in locais_possiveis if possivel[0] == suspeito["local"]]
        if local:
            local = local[0]
            if local[2][0] <= suspeito["horario"] <= local[2][1]:
                locais_abertos.append(suspeito)
            else:
                locais_fechados.append(suspeito)

    # locais invalidos, o cara nem pra mentir serve
    if locais_fechados:
        if len(locais_fechados) == 1:
            suspeito = locais_fechados[0]
            nome = suspeito["nome"]
            nome_local = suspeito["local"]
            horario_fechamento = [possivel[2][1] for possivel in locais_possiveis if possivel[0] == nome_local][0]
            horario_fechamento = "{:.2f}".format(horario_fechamento).replace(".", ":")
            print(f"{nome_local} nem estava aberto nessa hora, esse lugar foi fechado às {horario_fechamento}! {nome} roubou os melões!")
        else:
            nomes = ([suspeito["nome"] for suspeito in locais_fechados])
            locais = ([suspeito["local"] for suspeito in locais_fechados])
            nomes.sort()
            locais.sort()
            print(f"{', '.join(locais)} nem estavam abertos nessa hora, esses lugares foram fechados beeem antes! {', '.join(nomes)} se uniram e roubaram os melões!")
    else:
            # Análise da distância de cada suspeito até a plantação
            distancias = []
            for suspeito in suspeitos:
                for possivel in locais_possiveis:
                    if possivel[0] == suspeito["local"]:
                        distancias.append((possivel[1], suspeito["nome"]))
            
            # Encontrar a menor distância
            menor_distancia = distancias[0][0]
            for distancia, _ in distancias:
                if distancia < menor_distancia:
                    menor_distancia = distancia
            
            # Encontrar todos os suspeitos que andaram devagar pois antes tiveram pressa (menor distancia)
            suspeitos_proximos = []
            for distancia, nome in distancias:
                if distancia == menor_distancia:
                    suspeitos_proximos.append(nome)
            
            if len(suspeitos_proximos) == 1:
                print(f"{suspeitos_proximos[0]} estava a {menor_distancia} metros da plantação! Agora é nosso suspeito número um. Fiquem de olho!")
            elif len(suspeitos_proximos) > 1:
                print(f"{', '.join((suspeitos_proximos))} estavam a {menor_distancia} metros da plantação! Eles podiam estar cometendo o roubo juntos... Fiquem de olho!")

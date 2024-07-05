# dicionário com os dados dos artistas
discos_vendidos_semana_1 = {
    "Priscila Senna": {"discos": 40, "fortuna": 10000},
    "Eduarda": {"discos": 60, "fortuna": 9990},
    "Academia da Berlinda": {"discos": 30, "fortuna": 9995},
    "Martins": {"discos": 25, "fortuna": 9970},
    "Igor de Carvalho": {"discos": 25, "fortuna": 9965}
}

# dicionario com os dados da semana 2
discos_vendidos_semana_2 = {}

# função para calcular o faturamento dos discos
def faturamento_semana_2(dicionario, artista, qtd_discos, dicionario_primario):
    valor_total = 0
    # caso esse mini divo(a) nao exista
    if artista not in dicionario:
        dicionario[artista] = {"discos": qtd_discos, "fortuna": 0}
    
    if qtd_discos == 1:
        valor_total += (qtd_discos * 20)
    elif qtd_discos == 2 or qtd_discos == 3:
        valor_total += ((qtd_discos * 20) * 0.98)
    elif qtd_discos == 4 or qtd_discos == 5:
        valor_total += ((qtd_discos * 20) * 0.95)
    else:
        valor_total += ((qtd_discos * 20) * 0.93)
    
    dicionario[artista]["discos"] += qtd_discos
    dicionario[artista]["fortuna"] += valor_total

# tratando a entrada
def entrada_dados():
    numero_de_artistas = int(input())
    for artista in range(numero_de_artistas):
        nome_artista, numero_discos = input().split(" - ")
        numero_discos = int(numero_discos)
        faturamento_semana_2(discos_vendidos_semana_2, nome_artista, numero_discos, discos_vendidos_semana_1)

# eita como essa glr é rica
def lucro_do_artista():
    artistas_aumento_lucro = []
    novos_artistas = []
    # for mt bacana para analisar dinheiro e o aumento comparado a 1 semana
    for artista, dados in discos_vendidos_semana_2.items():
        if artista in discos_vendidos_semana_1:
            fortuna_semana_1 = discos_vendidos_semana_1[artista]['fortuna']
            aumento_percentual = ((dados['fortuna'] + fortuna_semana_1) / fortuna_semana_1 - 1) * 100
            if aumento_percentual > 0:
                artistas_aumento_lucro.append((artista, aumento_percentual))
            discos_vendidos_semana_1[artista]['discos'] += dados['discos']
            discos_vendidos_semana_1[artista]['fortuna'] += dados['fortuna']
        else:
            novos_artistas.append((artista, dados['discos']))
    # vendo se tem aumento legal ou nao
    if artistas_aumento_lucro:
        print("Estes artistas obtiveram aumento do lucro em relação à primeira semana:")
        for artista, aumento in artistas_aumento_lucro:
            print(f"{artista} - Lucro em relação à primeira semana: {aumento:.2f}%")
    else:
        print("Os artistas da primeira semana não tiveram aumento do lucro na segunda semana!")
    # vendo se sao afortunados na semana 1 e dps na semana 2, para o caso de pessoas novas
    print("\nEsta é a fortuna atual dos artistas considerados:")
    for artista, dados in discos_vendidos_semana_1.items():
        print(f"{artista}: R$ {dados['fortuna']:.2f}")
        
    for artista, dados in discos_vendidos_semana_2.items():
        if artista not in discos_vendidos_semana_1:
            print(f"{artista}: R$ {dados['fortuna']:.2f}")
    # mostrando os discos dos artistas novos
    if novos_artistas:
        print("\nNa semana 2 tivemos vendas de novos artistas no mercado:")
        for artista, discos_vendidos in novos_artistas:
            print(f"{artista} - Discos vendidos: {round(discos_vendidos/2)}")
    else:
        print("\nNa semana 2 não tivemos vendas de novos artistas no mercado!")

# chamada função
entrada_dados()
lucro_do_artista()

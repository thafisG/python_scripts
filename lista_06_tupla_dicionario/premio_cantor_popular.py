# calculo da idade das cidades
def calculo_idade_cidade(fundacao):
    return 2024 - fundacao

# pontuando as musicas: o melhor, o pior dos melhoress e o melhor dos piores
def pontuacao_vencedor(maior_visualizacao, segundo_maior_visualizacao, menor_visualizacao, idades_das_cidades, dados_premiacao):
    if maior_visualizacao:
        pontuacao = idades_das_cidades['idade'] + maior_visualizacao['visualizacao']
        print(f"O fenômeno é {maior_visualizacao['artista']}, que canta a música {maior_visualizacao['musica']}, já contando com mais de {maior_visualizacao['visualizacao']} milhões de visualizações na internet.")
    if segundo_maior_visualizacao:
        pontuacao = (idades_das_cidades['idade'] // 2) + segundo_maior_visualizacao['visualizacao']
        print(f"A música com segunda maior visualização é '{segundo_maior_visualizacao['musica']}' com {segundo_maior_visualizacao['visualizacao']} visualizações. Pontuação: {pontuacao}")
    if menor_visualizacao:
        pontuacao = (idades_das_cidades['idade'] // 3) + menor_visualizacao['visualizacao']
        print(f"A música com menor visualização é '{menor_visualizacao['musica']}' com {menor_visualizacao['visualizacao']} visualizações. Pontuação: {pontuacao}")

# tratando a entrada dos dados
def entrada_dados():
    dados_premiacao = []
    qtd_cidades = int(input())
    for _ in range(qtd_cidades):
        cidade = input()
        data_fundacao_cidade = int(input())
        idade_da_cidade = calculo_idade_cidade(data_fundacao_cidade)

        for _ in range(3):
            artista, musica, visualizacao = input().split(" - ")
            visualizacao = int(visualizacao)
            premiacao = {
                'cidade': cidade,
                'data_fundacao': data_fundacao_cidade,
                'artista': artista,
                'musica': musica,
                'visualizacao': visualizacao
            }

            dados_premiacao.append(premiacao)

    return dados_premiacao

# função principal para verificar a premiação 
def competicao_premiada():
    dados_premiacao = entrada_dados()
    candidatos = ["João Gomes", "Zé Vaqueiro", "Raphaela Santos", "Alceu Valença", "Priscila Senna"]
    pontuacao_candidatos = {candidato: 0 for candidato in candidatos}
    melhor_musica = {candidato: {'musica': '', 'visualizacao': 0} for candidato in candidatos}
    # booleanos separadamentes para cada cidade
    cidade_impressa_recife = False
    cidade_impressa_olinda = False
    cidade_impressa_petrolina = False
    
    for entrada in dados_premiacao:
        artista = entrada['artista']
        cidade = entrada['cidade']
        if artista in candidatos:
            cidade_idade = calculo_idade_cidade(entrada['data_fundacao'])
            # verificando cada cidade e seu respectivo booleano
            if cidade == 'Recife' and not cidade_impressa_recife:
                print("A veneza brasileira foi consultada nesta pesquisa!")
                cidade_impressa_recife = True
            elif cidade == 'Olinda' and not cidade_impressa_olinda:
                print("Uma honra ver que a primeira capital pernambucana foi consultada!")
                cidade_impressa_olinda = True
            elif cidade == 'Petrolina' and not cidade_impressa_petrolina:
                print("Ansioso para descobrir a opinião dos petrolinenses!")
                cidade_impressa_petrolina = True
            
            # verificando pontuacao para a premiacao
            if entrada == dados_premiacao[0]:
                pontuacao_candidatos[artista] += cidade_idade
            elif entrada == dados_premiacao[1]:
                pontuacao_candidatos[artista] += cidade_idade // 2
            elif entrada == dados_premiacao[2]:
                pontuacao_candidatos[artista] += cidade_idade // 3

            pontuacao_candidatos[artista] += entrada['visualizacao']

            if entrada['visualizacao'] > melhor_musica[artista]['visualizacao']:
                melhor_musica[artista] = {
                    'musica': entrada['musica'],
                    'visualizacao': entrada['visualizacao']
                }

    vencedor = max(pontuacao_candidatos, key=pontuacao_candidatos.get)
    # nepotismo com os fav
    if vencedor == "João Gomes":
        print("Parabéns, João Gomes, o novo fenômeno da música pernambucana!")
    elif vencedor == "Zé Vaqueiro":
        print("Zé Vaqueiro, o astro do forró, agora brilha como o rei da música pernambucana!")
    elif vencedor == "Raphaela Santos":
        print("Raphaela Santos, a voz marcante, agora é a rainha da música pernambucana!")
    elif vencedor == "Alceu Valença":
        print("Alceu Valença, o ícone da MPB, agora é o gigante da música pernambucana!")
    elif vencedor == "Priscila Senna":
        print("Priscila Senna, a rainha da sofrência, é a mais nova estrela da música pernambucana!")
    # CHEGOU A HORA QUE TODOS ESPERAVAM
    print(f"O fenômeno é {vencedor}, que canta a música {melhor_musica[vencedor]['musica']}, já contando com mais de {melhor_musica[vencedor]['visualizacao']} milhões de visualizações na internet.")

# chamando a função 
competicao_premiada()

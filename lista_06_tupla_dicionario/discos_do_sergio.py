# que começe os jogos
def entrada_artistas():
    print("Bem-vindo(a) à 'Sergio Bieber's Disco Shop'!")
    artista1 = input()
    artista2 = input()
    print(f"E os artistas de hoje são {artista1} e {artista2}!")
    return artista1, artista2

# Função para adicionar álbuns para um artista
def adicionar_albuns(artista_nome):
    albuns = {}
    nome_album = input()
    while nome_album != "acabou":
        preco_album = float(input())
        albuns[nome_album] = preco_album
        nome_album = input()
    return albuns

# Função para processar vendas
def processar_vendas(artista1_albuns, artista2_albuns, artista1_nome, artista2_nome):
    receita_total = 0.0
    vendas_artista1 = 0
    vendas_artista2 = 0
    receita_artista1_individual = 0
    receita_artista2_individual = 0
    
    print("-----COMEÇO DO EXPEDIENTE!-----")
    venda = input()
    # while para verificar cada artista e chamada para ajustar preço
    while venda != "FIM":
        if venda in artista1_albuns:
            print(f"{venda} vendido")
            vendas_artista1 += 1
            receita_total += artista1_albuns[venda]
            receita_artista1_individual += artista1_albuns[venda]
            if (vendas_artista1 - vendas_artista2) >= 3 and (vendas_artista1 - vendas_artista2) % 3 == 0:
                print(f"A diferença está ficando muito grande! AUMENTA R$4 DE {artista1_nome.upper()} E ABAIXA R$4 DE {artista2_nome.upper()}!")
                ajustar_precos(artista1_nome, artista2_nome, artista1_albuns, artista2_albuns)
            
        elif venda in artista2_albuns:
            print(f"{venda} vendido")
            vendas_artista2 += 1
            receita_total += artista2_albuns[venda]
            receita_artista2_individual += artista2_albuns[venda]
            if (vendas_artista2 - vendas_artista1) >= 3 and (vendas_artista2 - vendas_artista1) % 3 == 0:
                print(f"A diferença está ficando muito grande! AUMENTA R$4 DE {artista2_nome.upper()} E ABAIXA R$4 DE {artista1_nome.upper()}!")
                ajustar_precos(artista2_nome, artista1_nome, artista2_albuns, artista1_albuns)
        # iii esse tem nao    
        else:
            print("Parece que não temos esse disco...")
        
        venda = input()
    
    print("-----FIM DO EXPEDIENTE!-----")
    return receita_total, vendas_artista1, vendas_artista2, receita_artista1_individual, receita_artista2_individual

# função para ajustar o preço
def ajustar_precos(artista_mais_vendido, artista_menos_vendido, mais_vendido_albuns, menos_vendido_albuns):
        
    # Ajustar preços para o artista mais vendido
    for album, preco in mais_vendido_albuns.items():
        novo_preco = preco + 4.0
        mais_vendido_albuns[album] = max(1.0, novo_preco)  # Garantir preço mínimo de R$1.00
        
    for album, preco in menos_vendido_albuns.items():
        novo_preco = preco - 4.0
        menos_vendido_albuns[album] = max(1.0, novo_preco)  # Garantir preço mínimo de R$1.00
    
    return mais_vendido_albuns, menos_vendido_albuns

# Função para determinar o artista com mais vendas e imprimir resultados finais
def imprimir_resultados(artista1_nome, artista2_nome, receita_total, vendas_artista1, vendas_artista2, receita_artista1_individual, receita_artista2_individual):
    total_vendas = vendas_artista1 + vendas_artista2
    # caso for gero, se nao faz o restante
    if total_vendas == 0:
        print(f"O total de receita gerado foi de {int(receita_total)} e foram vendidos {total_vendas} discos.")
        print("Que tristeza! Só artista péssimo...")
    else:
        print(f"O total de receita gerado foi de {receita_total:.1f} e foram vendidos {total_vendas} discos.")
        if vendas_artista1 == vendas_artista2:
            print("Difícil de escolher o melhor!")
        else:
            artista_mais_vendido = artista1_nome if vendas_artista1 > vendas_artista2 else artista2_nome
            total_vendidos = vendas_artista1 if vendas_artista1 > vendas_artista2 else vendas_artista2
            if receita_artista1_individual > receita_artista2_individual:
                print(f"O artista que mais gerou dinheiro para a loja foi {artista_mais_vendido}, acumulando uma receita de {receita_artista1_individual:.1f} e vendendo {total_vendidos} discos.")
            else:
                print(f"O artista que mais gerou dinheiro para a loja foi {artista_mais_vendido}, acumulando uma receita de {receita_artista2_individual:.1f} e vendendo {total_vendidos} discos.")

# chamando as funções
artista1, artista2 = entrada_artistas()
artista1_albuns = adicionar_albuns(artista1)
artista2_albuns = adicionar_albuns(artista2)
receita_total, vendas_artista1, vendas_artista2, receita_artista1_individual, receita_artista2_individual = processar_vendas(artista1_albuns, artista2_albuns, artista1, artista2)
imprimir_resultados(artista1, artista2, receita_total, vendas_artista1, vendas_artista2, receita_artista1_individual, receita_artista2_individual)
artista1_albuns, artista2_albuns = ajustar_precos(artista1, artista2, artista1_albuns, artista2_albuns)

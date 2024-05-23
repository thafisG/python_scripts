# lista para armazenar os suspeitos - trabalhamos com nome SIM!!
nomes_suspeitos = []
# para perguntar os nomes dos possiveis criminosos
nome = ""
# sinal para ajudar a separar os nomes
separador = ", "
# variavel auxiliar para chamada das frases
indagacao_crime = input()
# inicio das avaliações
while indagacao_crime != "Já temos nossa lista de suspeitos":
    if indagacao_crime == "Novo suspeito - altíssima periculosidade":
        nome = input()
        nomes_suspeitos.insert(0, nome)
    elif indagacao_crime == "Novo suspeito - pouco perigoso":
        nome = input()
        nomes_suspeitos.append(nome)
    elif indagacao_crime == "Livre de suspeita, pode remover":
        nome = input()
        if nome in nomes_suspeitos:
            nomes_suspeitos.remove(nome)
    elif indagacao_crime == "Sujeito mais perigoso do que pensávamos":
        indice_atual = int(input())
        indice_novo = int(input())
        nomes_suspeitos[indice_atual], nomes_suspeitos[indice_novo] = nomes_suspeitos[indice_novo], nomes_suspeitos[indice_atual]
    elif indagacao_crime == "Que estranho, esses dois meliantes… troque-os de lugar":
        nome1 = input()
        nome2 = input()
        if nome1 in nomes_suspeitos and nome2 in nomes_suspeitos:
            idx1, idx2 = nomes_suspeitos.index(nome1), nomes_suspeitos.index(nome2)
            nomes_suspeitos[idx1], nomes_suspeitos[idx2] = nomes_suspeitos[idx2], nomes_suspeitos[idx1]
    elif indagacao_crime == "Essa posição não esta de acordo, ele não e tão perigoso assim":
        nome = input()
        if nome in nomes_suspeitos:
            nomes_suspeitos.remove(nome)
            nomes_suspeitos.append(nome)
    elif indagacao_crime == "Como a lista esta ficando?":
        print(separador.join(nomes_suspeitos))
    # pedindo dnv pra o while rodar
    indagacao_crime = input()
# função para quando acabar tudo
if indagacao_crime == "Já temos nossa lista de suspeitos":
    print("O resultado final ficou assim:")
    print(separador.join(nomes_suspeitos))

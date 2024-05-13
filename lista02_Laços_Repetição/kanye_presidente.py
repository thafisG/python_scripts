pontuacao_kanye = 0
pontuacao_candidato = 0
N = input()
votos = 0
# primeiro turno
while N != "FIM":
    N = int(N)
    votos += pontuacao_kanye + pontuacao_candidato
    if N % 7 == 0 and N % 2 != 0:
        pontuacao_kanye += 20000000
    elif N % 2 == 0 and N % 7 != 0:
        pontuacao_kanye += 10000000
    elif N % 7 != 0 and N % 2 != 0:
        pontuacao_candidato += 14000000

    if (pontuacao_kanye + pontuacao_candidato) >= 300000000:
        N = "FIM"
    else:
        N = input()

# validação de votos
if pontuacao_kanye > 170000000:
    print("O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
    print(f"Kanye conseguiu ao final da campanha um total de {pontuacao_kanye} votos.")
if pontuacao_kanye < 130000000:
    print("Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")
    print(f"Kanye conseguiu ao final da campanha um total de {pontuacao_kanye} votos.")
if 130000000 <= pontuacao_kanye and pontuacao_kanye <= 170000000:
    print("A eleição está disputada, vamos ter um segundo turno!")
    print(f"Kanye conseguiu ao final da campanha um total de {pontuacao_kanye} votos.")
# zerando para iniciar o 2 turno
    pontuacao_kanye = 0
    pontuacao_candidato = 0
    votos = 0
    N = input()
    # 2 turno
    while N != "FIM":
        N = int(N)
        votos += pontuacao_kanye + pontuacao_candidato
        if N % 7 == 0 and N % 2 != 0:
            pontuacao_kanye += 20000000
        elif N % 2 == 0 and N % 7 != 0:
            pontuacao_kanye += 10000000
        elif N % 7 != 0 and N % 2 != 0:
            pontuacao_candidato += 14000000

        if (pontuacao_kanye + pontuacao_candidato) >= 300000000:
            N = "FIM"
        else:
            N = input()
    # validando 2 turno
    if pontuacao_kanye > 170000000:
        print("Depois de um pleito muito acirrado, O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
    else:
        print("Caramba, foi uma disputa muito acirrada, mas não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")
    print(f"Kanye conseguiu ao final da campanha um total de {pontuacao_kanye} votos.")

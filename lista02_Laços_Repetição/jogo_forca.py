print("Bem vindo ao jogo da forca do ye!")
# quantidade de musiquinhas :)
N = int(input())
total_de_pontos = 0
contador = 0

# analisando a musica para começar os jogos hehe
for posicao in range(N):
        letras_acertadas = ""
        letras_erradas = ""
        parar = False
        musica = input()
        # calculando as tentativas pra que essa criatura ganhe, ne possivel
        tentativas = 0
        for c in musica:
            if c != " ":
                tentativas += 2
        # para guardar as respostas, vai q ele acerta alguma
        resposta = ""
        # essa musica ai oh, vamo vê qual é
        if posicao == N - 1:
            print("Última música!")

        else:
            print(f"Esta é a música {posicao + 1} de {N}.")

        # analise dos tracinhos pra vê se ta sendo um cara de sorte ou nao...
        for espaco in musica:
            if espaco == " ":
                resposta += " "
            elif espaco != " ":
                resposta += "_"

        letras_acertadas = ""
        letras_erradas = ""
        while tentativas > 0 and total_de_pontos != N and parar == False:
            chute = input()

            if chute in letras_acertadas or chute in letras_erradas:
                print("Já tinha colocado essa letra antes, preciso de mais atenção.")
                tentativas -= 1
            else:
                if chute in musica:
                    print("Uhuuuuu! Consegui adivinhar uma letra!")
                    letras_acertadas += chute
                    tentativas -= 1
                    for i in range(len(musica)):
                        if musica[i] == chute:
                            resposta = resposta[:i] + chute + resposta[i + 1:]
                else:
                    print(f"Eita! Parece que a letra {chute} não está na música secreta!")
                    letras_erradas += chute
                    tentativas -= 1

            # exibindo a resposta ne chefe, pra esse cara nao se perder
            print("Resposta atual:", resposta)

            if resposta == musica:
                print("Isso! Consegui acertar uma música!")
                total_de_pontos += 1
                parar = True
            elif tentativas == 0:
                print(f"Vish, essa tava difícil, a música era {musica}. Espero acertar a próxima!")

# chegando no final para o querido saber os pontos dps de tanto esforço
print(f"Consegui acertar {total_de_pontos} músicas de {N}!")
taxa_acerto = (total_de_pontos / N) * 100

# analise dos calculos legais em porcentagem pra vê se esse cara é bom em acertar letra
if taxa_acerto <= 50:
    print("Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!")
elif taxa_acerto > 50 and taxa_acerto <= 75:
    print("Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.")
elif taxa_acerto > 75 and taxa_acerto < 100:
    print("Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.")
elif taxa_acerto == 100:
    print("Eu sou o próprio Kanye West.")

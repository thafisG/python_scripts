# finalmente a utimaaaa
# recebendo os numeros de rodadas
num_rodadas = int(input())
# variaveis auxiliares
pontuacao_kanye = 0
pontuacao_taylor = 0
# bora ver quem tem fã ruim
pontuacao_desordem_kanye = 0
pontuacao_desordem_taylor = 0
# variavel para ver quem vai vencer ou nao
pontuacao_kanye_vitoria = 0
pontuacao_taylor_vitoria = 0

# começando a rodar as rodadas muito bacanas :)
for rodada in range(1, num_rodadas + 1):
    if pontuacao_desordem_kanye < 5 and pontuacao_desordem_taylor < 5:
        if pontuacao_kanye_vitoria < 3 and pontuacao_taylor_vitoria < 3:
            print(f"{rodada}° RODADA:")
            pontuacao_kanye = 0
            pontuacao_taylor = 0

            if pontuacao_desordem_kanye < 5 and pontuacao_desordem_taylor < 5:
                # avaliando o querido
                musica_kanye = input()
                for _ in range(3):
                    avaliacao_kanye = input()
                    if avaliacao_kanye == "boa":
                        pontuacao_kanye += 2
                    elif avaliacao_kanye == "média":
                        pontuacao_kanye += 1
                    elif avaliacao_kanye == "ruim":
                        pontuacao_kanye -= 3
                    elif avaliacao_kanye == "péssima":
                        palavra = input()
                        while palavra != "ORDEM":
                            pontuacao_desordem_kanye += 1
                            palavra = input()
            if pontuacao_desordem_taylor < 5 and pontuacao_desordem_kanye < 5:
                # avaliando a querida
                musica_taylor = input()
                for _ in range(3):
                    avaliacao_taylor = input()
                    # analise taylor
                    if avaliacao_taylor == "boa":
                        pontuacao_taylor += 2
                    elif avaliacao_taylor == "média":
                        pontuacao_taylor += 1
                    elif avaliacao_taylor == "ruim":
                        pontuacao_taylor -= 3
                    elif avaliacao_taylor == "péssima":
                        palavra = input()
                        while palavra != "ORDEM":
                            pontuacao_desordem_taylor += 1
                            palavra = input()

            # avaliando os fãs bagunceiro
            if pontuacao_desordem_kanye >= 5:
                print("Os fãs do(a) Kanye West causaram tanta desordem que ele(a) perdeu o prêmio!")
                print("O(a) vencedor(a) do Cin Awards é Taylor Swift, parabéns!")
                pontuacao_taylor_vitoria += 1
                continue
            elif pontuacao_desordem_taylor >= 5:
                print("Os fãs do(a) Taylor Swift causaram tanta desordem que ele(a) perdeu o prêmio!")
                print("O(a) vencedor(a) do Cin Awards é Kanye West, parabéns!")
                pontuacao_kanye_vitoria += 1
                continue

            # verificando quem venceu na rodada ou perdeu ne
            if pontuacao_kanye > pontuacao_taylor:
                print(f"O(a) vencedor(a) da {rodada}° rodada foi Kanye West")
                pontuacao_kanye_vitoria += 1
            elif pontuacao_taylor > pontuacao_kanye:
                print(f"O(a) vencedor(a) da {rodada}° rodada foi Taylor Swift")
                pontuacao_taylor_vitoria += 1
            elif pontuacao_taylor == pontuacao_kanye:
                print(f"Não houve vencedor na {rodada}° rodada")

# validando quem ganhou mais
if pontuacao_desordem_taylor < 5 and pontuacao_desordem_kanye < 5:
    if pontuacao_kanye_vitoria > pontuacao_taylor_vitoria:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {pontuacao_kanye_vitoria} vitórias, é Kanye West, parabéns!")
    elif pontuacao_taylor_vitoria > pontuacao_kanye_vitoria:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {pontuacao_taylor_vitoria} vitórias, é Taylor Swift, parabéns!")
    elif pontuacao_taylor_vitoria == pontuacao_kanye_vitoria:
        print("Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!")

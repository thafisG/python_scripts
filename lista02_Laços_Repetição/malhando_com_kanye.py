quantidade_exercicios = int(input())
tipo_treino = input()
nome_musica = ""
nota_musica = 0
contagem_musicas = 0

while tipo_treino == "TREINO DE PERNA DEUS DAI ME FORCAS" or tipo_treino == "TREINO DE COSTAS FE EM DEUS QUE VAI" or tipo_treino == "TREINO DE PEITO AMEM SENHOR":
    print(f"{tipo_treino}")
    musica_aprovada = 0
    for _ in range(quantidade_exercicios):
        nome_musica = input()
        nota_musica = int(input())
        contagem_musicas += 1
        print(f"{contagem_musicas}° música {nome_musica} tocando agora")

        if nota_musica >= 7:
            print("O padre Marcelo está inspirado, conseguiu finalizar suas séries!")
            musica_aprovada += 1
        else:
            print("O padre Marcelo está desanimado, não conseguiu finalizar suas séries")

    if musica_aprovada >= (quantidade_exercicios // 2 + quantidade_exercicios % 2):
        print("ME DEI BEM COM ESSA PLAYLIST, APROVADO")
    else:
        print("NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL")

    tipo_treino = input()
    contagem_musicas = 0

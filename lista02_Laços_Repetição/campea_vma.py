quantidade_alunos = int(input())
contagem_votos_tay = 0
contagem_votos_bey = 0
voto_decisivo = ""
# variavel para ordem
X = 0
# vamos analisar quem sabe mais
for aluno in range(quantidade_alunos):
    X += 1
    # voto de cada aluno - 1 sessão
    voto_aluno = input()
    if voto_aluno == "taylor swift":
        contagem_votos_tay += 1
        print(f"Aluno {X} votou na Taylor Swift.")
    elif voto_aluno == "beyonce":
        contagem_votos_bey += 1
        print(f"Aluno {X} votou na Beyoncé.")

# primeiro turnooo - vamos analisar os votos
print("Contagem de votos:")
print(f"Taylor Swift: {contagem_votos_tay} votos")
print(f"Beyoncé: {contagem_votos_bey} votos")

# caso alguém ganhe no 1 turno
if contagem_votos_tay > contagem_votos_bey:
    print(f"Taylor Swift venceu com {contagem_votos_tay} votos! Kanye West tá irritado com isso.")
elif contagem_votos_bey > contagem_votos_tay:
    print(f"Beyoncé venceu com {contagem_votos_bey} votos! Será que Kanye West estava certo?")
# iniciando 2 turno - quem será q vai ganhar?
if contagem_votos_tay == contagem_votos_bey:
    print("Empate! Iniciando rodada de debate.")
    print("Alunos, agora é a sua chance de convencer os outros a mudar de voto!")
    # for do 2 turno
    i = 0
    for i in range(quantidade_alunos):
        i += 1
        novo_voto = input()
        if novo_voto == "sim":
            voto_aluno = input()
            if voto_aluno == "taylor swift":
                contagem_votos_tay += 1
                print(f"Aluno {i} mudou seu voto para Taylor Swift.")
            elif voto_aluno == "beyonce":
                contagem_votos_bey += 1
                print(f"Aluno {i} mudou seu voto para Beyoncé.")
        else:
            print(f"Aluno {i} não mudou seu voto.")

    # nova contageeemm - momento mais esperado
    print("Nova contagem de votos após o debate:")
    print(f"Taylor Swift: {contagem_votos_tay} votos")
    print(f"Beyoncé: {contagem_votos_bey} votos")
    # será que alguém vai ganhar?
    if contagem_votos_tay > contagem_votos_bey:
        print(f"Taylor Swift venceu com {contagem_votos_tay} votos! Kanye West tá irritado com isso.")
    elif contagem_votos_bey > contagem_votos_tay:
        print(f"Beyoncé venceu com {contagem_votos_bey} votos! Será que Kanye West estava certo?")
    elif contagem_votos_tay == contagem_votos_bey:
        print("Aldo, como presidente do evento, tem o voto decisivo.")
        voto_decisivo = input()
        if voto_decisivo == "taylor swift":
            print("Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.")
        else:
            print("Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?")

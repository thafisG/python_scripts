musicas = {
    'Samba': ["Preciso Me Encontrar", "O Mundo É Um Moinho", "Trem Das Onze", "O Que É O Que É?", "Disritmia", "Timoneiro"],
    'Rock Nacional': ["Epitáfio", "Meu Novo Mundo", "À Sua Maneira", "Que País É Este", "Um Minuto Para O Fim Do Mundo", "Infinita Highway"],
    'Rock': ["Smells Like Teen Spirit", "In The End", "Californication", "Welcome To The Jungle", "Another Brick In The Wall", "Bohemian Rapsody", "Bring Me To Life", "Paint It, Black", "Stairway To Heaven"],
    'Pop': ["As It Was", "Viva La Vida", "Someone Like You", "Blinding Lights", "Maps", "Talking To The Moon", "Believer", "Ghost", "Wake Me Up", "Rude", "Perfect"],
    'MPB': ["O Descobridor Dos Sete Mares", "Anunciação", "Exagerado", "João E Maria", "Sujeito De Sorte", "Naquela Mesa", "Eduardo E Mônica", "Lanterna Dos Afogados", "Metamorfose Ambulante"],
    'Manguebeat': ["Da Lama Ao Caos", "A Praieira", "Maracatu Atômico", "Manguetown", "Um Sonho", "A Cidade"],
    'Indie Folk': ["Ends Of The Earth", "Welcome Home, Son", "Riptide", "Father And Son", "Ho Hey", "The Night We Met", "Budapest", "Atlantis"],
    'Forró': ["Xote Das Meninas", "Xote Da Alegria", "Deus Me Proteja", "Numa Sala De Reboco", "Meu Cenário", "Colo De Menina", "Riacho Do Navio"]
}

def pontuacao(musicas_usuario_genero):
    pontuacoes = {}
    for genero in musicas:
        pontuacoes[genero] = len(musicas_usuario_genero.get(genero, []))
    return pontuacoes

def verificacao_musica(musicas_usuario):
    musicas_usuario_genero = {}
    for genero in musicas:
        musicas_usuario_genero[genero] = []
        for musica in musicas_usuario:
            if musica in musicas[genero]:
                musicas_usuario_genero[genero].append(musica)
    return musicas_usuario_genero

def recomendacao(nome_usuario, quantidade_musicas, musicas_usuario_genero):
    pontuacoes = pontuacao(musicas_usuario_genero)
    
    generos_ordenados = list(musicas.keys())
    generos_ordenados.sort(key=lambda genero: (-pontuacoes[genero], list(musicas.keys()).index(genero)))

    recomendadas = []
    generos_sem_musicas = []
    recomendadas_diferente = {}

    for i, genero in enumerate(generos_ordenados):
        if pontuacoes[genero] == 0:
            continue
        
        if pontuacoes[genero] not in recomendadas_diferente:
            if len(recomendadas_diferente) == 0:
                recomendadas_diferente[pontuacoes[genero]] = 3
            elif len(recomendadas_diferente) == 1:
                recomendadas_diferente[pontuacoes[genero]] = 2
            else:
                recomendadas_diferente[pontuacoes[genero]] = 1

        num_recomendadas = recomendadas_diferente[pontuacoes[genero]]

        genero_recomendadas = []
        for musica in musicas[genero]:
            if musica not in musicas_usuario_genero[genero] and len(genero_recomendadas) < num_recomendadas:
                genero_recomendadas.append(musica)
        if genero_recomendadas:
            recomendadas.extend(genero_recomendadas)
        else:
            generos_sem_musicas.append(genero)

    if quantidade_musicas == 0:
        print(f"Parece que {nome_usuario} não escutou nenhuma música. Vamos recomendar algumas músicas de gêneros diferentes:\n")
        for i in range(len(musicas)):
            genero = list(musicas.keys())[i]
            print(f"{i + 1}. {musicas[genero][0]}")
    elif recomendadas:
        print(f"{nome_usuario} escutou {quantidade_musicas} música(s) e estas são as próximas recomendações:\n")
        for i in range(len(recomendadas)):
            print(f"{i + 1}. {recomendadas[i]}")
    else:
        if len(generos_sem_musicas) == 1:
            print(f"{nome_usuario} já escutou todas as músicas disponíveis no(s) gênero(s): {generos_sem_musicas[0]}. Infelizmente não sobrou nenhuma música disponível para recomendação.")
        else:
            generos_formatados = ', '.join(generos_sem_musicas[:-1]) + f" e {generos_sem_musicas[-1]}"
            generos_ordem_correta = []
            for genero in musicas:
                if genero in generos_sem_musicas:
                    generos_ordem_correta.append(genero)
            generos_formatados = ', '.join(generos_ordem_correta[:-1]) + f" e {generos_ordem_correta[-1]}"
            print(f"{nome_usuario} já escutou todas as músicas disponíveis no(s) gênero(s): {generos_formatados}. Infelizmente não sobrou nenhuma música disponível para recomendação.")

# Entrada do usuário
nome_usuario = input()
qtnd_musicas = int(input())
musicas_usuario = []
for i in range(qtnd_musicas):
    musica = input()
    musicas_usuario.append(musica)

musicas_usuario_genero = verificacao_musica(musicas_usuario)
recomendacao(nome_usuario, qtnd_musicas, musicas_usuario_genero)

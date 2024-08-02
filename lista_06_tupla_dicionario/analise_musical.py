# VOLTOU A MAIS TEMIDA: CIFRA CESAR
def decodificar_cifra_cesar(texto_codificado, chave):
    texto_decifrado = ''
    for caractere in texto_codificado:
        if caractere.isalpha():
            codigo = ord(caractere)
            if caractere.islower():
                codigo = ((codigo - ord('a') - chave) % 26) + ord('a')
            else:
                codigo = ((codigo - ord('A') - chave) % 26) + ord('A')
            texto_decifrado += chr(codigo)
        else:
            texto_decifrado += caractere
    return texto_decifrado

# Entrada para a pontuação maxima
pontuacao_limite = int(input())

# Dicionário para os álbuns e suas músicas com pontuação inicial zero
albuns_de_musica = {
    'sweetener': {
        'no tears left to cry': 0,
        'the light is coming': 0,
        'better off': 0,
        'everytime': 0
    },
    'thank u, next': {
        'NASA': 0,
        'thank u, next': 0,
        'break up with your girlfriend, i\'m bored': 0,
        'bad idea': 0
    },
    'Positions': {
        'motive': 0,
        'safety net': 0,
        'nasty': 0,
        'pov': 0
    },
    'eternal sunshine': {
        'yes, and?': 0,
        'eternal sunshine': 0,
        'the boy is mine': 0,
        'we can\'t be friends': 0
    }
}

# Dicionário para armazenar a pontuação acumulada de cada álbum
albuns_pontuacao = {album: 0 for album in albuns_de_musica}

# Recebendo entrada inicial
try:
    entrada = input()
except EOFError:
    entrada = "FIM"

# Variável para controlar se o limite foi atingido
nivel = False

# loop que recebe a variavel de entrada e roda ate fim ou ate o nivel max
while entrada != "FIM" and not nivel:
    musica_codificada, nivel_yeahs_str = entrada.split(' - ')
    nivel_yeahs = int(nivel_yeahs_str)
    musica_decifrada = decodificar_cifra_cesar(musica_codificada, 3)
    print(f'O nome da música decifrada é: {musica_decifrada}')
    # variavel auxiliar para saber se a msc foi encontrada
    encontrada = False
    for album, musicas in albuns_de_musica.items():
        if musica_decifrada in musicas:
            encontrada = True
            musicas[musica_decifrada] += nivel_yeahs
            albuns_pontuacao[album] += nivel_yeahs

            print('Ótimo! A música está na discografia da nossa base de dados!')
            print(f'O album da música decifrada é {album}')

            if nivel_yeahs < 5:
                print('A diva do pop não se empolgou nessa e decepcionou os arianators.')
            elif 5 <= nivel_yeahs < 10:
                print('Ariana fez o dever de casa e entregou uma música na média para os seus fãs.')
            else:
                print('AVISA QUE ESSA JÁ É HIT NOS CHARTS!')
            # verificando a pontuacao q nem so de rodadas de while vive o ser humano
            if albuns_pontuacao[album] >= pontuacao_limite:
                print(f'Atenção! O limite de pontuação foi atingido pelo álbum {album}!')
                nivel = True

    if not encontrada:
        print('Poxa, essa música não está na discografia da base do nosso estúdio!')

    # Tentando receber a próxima entrada no final de cada loop para saber se vai rodar ou nao
    try:
        entrada = input()
    except EOFError:
        entrada = "FIM"

# Finalizando a análise
print('Fim da análise!\n')

# Encontrando o álbum com maior pontuação
album_max_pontuacao = max(albuns_pontuacao, key=albuns_pontuacao.get)
max_pontuacao = albuns_pontuacao[album_max_pontuacao]

# Encontrar a música com maior pontuação nesse álbum
musicas_do_album_max = albuns_de_musica[album_max_pontuacao]
musica_max_pontuacao = max(musicas_do_album_max, key=musicas_do_album_max.get)
max_pontuacao_musica = musicas_do_album_max[musica_max_pontuacao]

# para a gravação, printa printa printa
print(f'O álbum da estrela Ariana Grande com a maior pontuação foi {album_max_pontuacao}, com um total de {max_pontuacao} pontos!')
print(f'Entre todas as faixas desse álbum, a melhor pontuada foi {musica_max_pontuacao}, que obteve {max_pontuacao_musica} pontos')

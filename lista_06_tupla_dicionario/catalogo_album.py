# Catálogo inicial de álbuns (tuplas)
catalogo_albuns = [
    ("Abbey Road", "The Beatles", 1969, "Rock"),
    ("The Dark Side of the Moon", "Pink Floyd", 1973, "Rock"),
    ("Riot!", "Paramore", 2007, "Rock"),
    ("Fearless", "Taylor Swift", 2008, "Pop"),
    ("Da Lama ao Caos", "Chico Science e Nação Zumbi", 1994, "Manguebeat"),
    ("Gal Costa", "Gal Costa", 1969, "MPB"),
    ("Sim", "Vanessa da Mata", 2007, "MPB"),
    ("As 20 Melhores", "Luiz Gonzaga", 2004, "Forró"),
    ("O Melhor de Dominguinhos", "Dominguinhos", 2013, "Forró"),
    ("Alucinação", "Belchior", 1976, "MPB"),
    ("Samba Esquema Novo", "Jorge Ben Jor", 1963, "Samba")
]

# Dicionário para armazenar os álbuns por gênero musical
generos_musicais = {"Rock": True, "Pop": True, "Manguebeat": True, "MPB": True, "Forró": True, "Samba": True}

# Função para adicionar um novo álbum ao catálogo
def adicionar_album(nome_album, nome_artista, ano_lancamento, genero_musical):
    album_novo = (nome_album, nome_artista, int(ano_lancamento), genero_musical)
    # adicionando album novo no catalogo
    catalogo_albuns.append(album_novo)
    print("Este foi o novo álbum adicionado:")
    print(f"- {nome_album} do/da artista/banda {nome_artista} lançado em {ano_lancamento}")

# Função para consultar álbuns por gênero musical
def consultar_por_genero(genero_musical):
    # eita como cria lista
    albuns_encontrados = []
    # percorrendo a tupla mt bacana e legal pra fazer verificação
    for album in catalogo_albuns:
        if album[3] == genero_musical:
            albuns_encontrados.append(album)
    # seu divertidamente de dora aventureira está em dia (você achou)
    if albuns_encontrados:
        print(f"Nessa galeria há {len(albuns_encontrados)} albuns de {genero_musical}. Os albuns encontrados foram:")
        for album in albuns_encontrados:
            print(f"- {album[0]} do/da artista/banda {album[1]} lançado em {album[2]}")
    # iiiii ta fraco (nao tem aqui)
    else:
        print("Você vai precisar adicionar um novo álbum ao catálogo! Não encontramos nenhum álbum desse estilo musical!")

# Loop principal para tratar as entradas
continuar = True
while continuar:
    entrada = input()
    
    if entrada == "FIM":
        continuar = False
    # ta curioso demais
    elif entrada == "CONSULTAR":
        genero = input()
        consultar_por_genero(genero)
    # adiciona adiciona adiciona
    else:
        nome_album = entrada
        nome_artista = input()
        ano_lancamento = input()
        genero_musical = input()
        adicionar_album(nome_album, nome_artista, ano_lancamento, genero_musical)
        # eita, estilo novo é, tapoxa tapoxa
        if genero_musical not in generos_musicais:
            generos_musicais[genero_musical] = True
            print("Oba, você adicionou um novo estilo musical ao catálogo!")

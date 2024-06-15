resultado = []
# conta do cifra de cesar
def cifra_cesar(texto, deslocamento):
    resultado = []
    for letra in texto.lower():
        if 'a' <= letra <= 'z':  # Verifica se a letra está no intervalo das letras minúsculas
            indice = (ord(letra) - ord('a') + deslocamento) % 26
            resultado.append(chr(ord('a') + indice))
        else:
            resultado.append(letra)
    return ''.join(resultado)

# calculando id 
def calcular_id(nome, deslocamento, multiplicador_tempo=1):
    nome_codificado = cifra_cesar(nome, deslocamento)
    soma_ascii = sum(ord(char) for char in nome_codificado)
    return soma_ascii * multiplicador_tempo

# processando as coisas (aqui terá de tudo)
def processar_eventos(numero_participantes, entrada_apresentacao, eventos):
    nomes_participantes = []
    favoritos = []
    pokebolas = []

    # criando uma lista shiny
    shiny = [[] for _ in range(numero_participantes)]
    
    # tratando as apresentacao para analisar os dados
    for apresentacao in entrada_apresentacao:
        apresentacao_tratada = apresentacao.split(", ")
        nome = apresentacao_tratada[1].split("é ")[1]
        favorito = apresentacao_tratada[2].split("é ")[1]
        qtd_pokebolas = apresentacao_tratada[2].split(" ")[7]
        favorito = favorito.replace(f" e tenho {qtd_pokebolas} pokébolas", "")
        nomes_participantes.append(nome)
        favoritos.append(favorito)
        pokebolas.append(int(qtd_pokebolas))
    
    contador_shiny = 0
    shiny_verdadeiro = False
    while (not shiny_verdadeiro):
        # fazendo o tratamento da entrada
        evento = input()
        eventos.append(evento)
        eventos_tratados = evento.split("! ")
        pokemon = eventos_tratados[0].split("Um ")[1]
        pokemon = pokemon.replace(" selvagem apareceu", "")
        participante = eventos_tratados[1].split(" de ")[1]
        passos = eventos_tratados[1].split(" e ")[1]
        passos = passos.replace(f" passos desde o último encontro de {participante}", "")
        passos = int(passos)
        tempo = eventos_tratados[1].split("Foram ")[1]
        tempo = tempo.replace(f" segundos e {passos} passos desde o último encontro de {participante}", "")
        tempo = int(tempo)
        cifra_cesar(pokemon, 3)
            
        indice_participante = nomes_participantes.index(participante)
        id_participante = calcular_id(participante, 3, 1)
        id_pokemon = calcular_id(pokemon, passos, tempo)

        shiny_verdadeiro = str(id_participante)[-1] == str(id_pokemon)[-1]
        pokemon_favorito = favoritos[indice_participante]
        pokebolas_restantes = pokebolas[indice_participante]
                
        # verificando se pegou um especial ou nao 
        if pokebolas_restantes > 0:
            if shiny_verdadeiro:
                if pokemon not in shiny[indice_participante]:
                    shiny[indice_participante].append(pokemon)
                    pokebolas[indice_participante] -= 1
                    if pokemon == pokemon_favorito:
                        if pokebolas[indice_participante] == 0:
                            print(f"{participante}: Que sorte! Não apenas achei meu shiny favorito, como também o capturei em minha última pokébola!!!")
                            contador_shiny += 1
                        else:
                            print(f"{participante}: Consegui capturar um {pokemon_favorito} shiny!")
                            contador_shiny += 1
                    else:
                        print(f"{participante}: Mais um shiny para a coleção, mas ainda não é um {pokemon_favorito}")
                        shiny_verdadeiro = False

                elif pokemon in shiny[indice_participante]:
                    print(f"{participante}: Achei um {pokemon} shiny, mas não posso desperdiçar pokébolas em um shiny que já tenho...")
                    shiny_verdadeiro = False
            else:
                if pokemon == pokemon_favorito:
                    pokebolas[indice_participante] -= 1
                    print(f"{participante}: Uau, um {pokemon_favorito}! Pena que não é um shiny...")
                    shiny_verdadeiro = False
                else:
                    print(f"{participante}: Ainda não é um {pokemon_favorito} shiny, tenho que continuar procurando...")
                    shiny_verdadeiro = False
        else:
            if shiny_verdadeiro:
                if pokemon == pokemon_favorito:
                    print(f"{participante}: Só pode ser brincadeira, um {pokemon_favorito} shiny logo agora?!")
                    shiny_verdadeiro = False
                else:
                    print(f"{participante}: Péssimo momento, encontrei um {pokemon} shiny, mas não tenho mais pokébolas!")
                    shiny_verdadeiro = False
            else:
                if pokemon == pokemon_favorito:
                    print(f"{participante}: Desculpa, meu querido {pokemon_favorito}, mas não poderei lhe capturar hoje")
                else:
                    print(f"{participante}: Só um {pokemon} normal?Bom, não é como se eu tivesse pokébolas para capturar algo raro mesmo...")

        if contador_shiny >= numero_participantes:
            shiny_verdadeiro = True 
           
    # eita como verifica
    print("\n---Vamos verificar o que todos encontraram!---")

    for idx in range(numero_participantes):
        nome_pessoa = nomes_participantes[idx]
        shinies_list = shiny[idx]  # Lista de shinies do participante atual
        if shinies_list:
            if len(shinies_list) == 1:
                print(f"{nome_pessoa} capturou os seguintes shinies: {shinies_list[0]}")
            else:
                print(f"{nome_pessoa} capturou os seguintes shinies: {', '.join(shinies_list)}")
        else:
            print(f"Coitado, {nome_pessoa} não conseguiu capturar um único shiny hoje")


# Leitura dos inputs
numero_participantes = int(input())
entrada_apresentacao = []
# pedindo as apresentacoes para tratar dentro da função 
for participante in range(numero_participantes):
    entrada = input() 
    entrada_apresentacao.append(entrada)

# criando eventos em lista apenas para poder chamar a função globalmente
eventos = []
processar_eventos(numero_participantes, entrada_apresentacao, eventos)

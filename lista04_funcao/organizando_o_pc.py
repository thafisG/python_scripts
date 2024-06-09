# função para criar matriz, a cada chamada ela cria matriz nova e etc (5x6)
def criar_matriz(pokemons_armazenados):
    num_matrizes = pokemons_armazenados // (5 * 6)
    elementos_restantes = pokemons_armazenados % (5 * 6)

    for _ in range(num_matrizes):
        box_pokemon.append([[1 for _ in range(6)] for _ in range(5)])

    if elementos_restantes > 0:
        box_parcial = [[0 for _ in range(6)] for _ in range(5)]
        indice = 0
        for linha in range(5):
            for coluna in range(6):
                if indice < elementos_restantes:
                    box_parcial[linha][coluna] = 1
                    indice += 1

        box_pokemon.append(box_parcial)

# função para capturar os monstrinhos, ele adicona 1 onde tem coisa e 0 onde nao tem nadica 
def capturar_pokemon(quantidade_pokemon):
    for box in box_pokemon:
        for linha in range(5):
            for coluna in range(6):
                if quantidade_pokemon > 0 and box[linha][coluna] == 0:
                    box[linha][coluna] = 1
                    quantidade_pokemon -= 1
    if quantidade_pokemon > 0:
        while quantidade_pokemon > 0:
            nova_box = [[0 for _ in range(6)] for _ in range(5)]
            for linha in range(5):
                for coluna in range(6):
                    if quantidade_pokemon > 0:
                        nova_box[linha][coluna] = 1
                        quantidade_pokemon -= 1
            box_pokemon.append(nova_box)

# função para remover um determinado número de pokemons do seu PC
def transferir_pokemon(quantidade_pokemon):
    while quantidade_pokemon > 0 and len(box_pokemon) > 0:
        ultima_box = box_pokemon[-1]
        for linha in range(4, -1, -1):
            for coluna in range(5, -1, -1):
                if quantidade_pokemon > 0 and ultima_box[linha][coluna] == 1:
                    ultima_box[linha][coluna] = 0
                    quantidade_pokemon -= 1
        if all(ultima_box[linha][coluna] == 0 for linha in range(5) for coluna in range(6)):
            box_pokemon.pop()

# função auxiliar para impressão a cada comando deste moço querido
def impressao_das_boxes(box_pokemon):
    for numero_box in range(1, len(box_pokemon) + 1):
        box = box_pokemon[numero_box - 1]
        print(f"BOX {numero_box}:")
        for linha in box:
            print(' '.join(str(num) for num in linha))
        print()
    if len(box_pokemon) <= 0:
        print(f"BOX 1:")   
        matriz_vazia = [[0 for _ in range(6)] for _ in range(5)]
        for linha in matriz_vazia:
            print(' '.join(str(elemento) for elemento in linha))
        print()

# inicializando os coisinhos :)
pokemons_armazenados = int(input())
box_pokemon = []
criar_matriz(pokemons_armazenados)

# while para ler os comandos e depois puxar as funções de origem 
comando = input()
# while para rodar infinitamente ate a pessoa digitar "finalizar"
while comando != "Finalizar":

    if comando == "Capturar":
        quantidade_pokemon = int(input())
        capturar_pokemon(quantidade_pokemon)
        impressao_das_boxes(box_pokemon)
        
    elif comando == "Transferir":
        quantidade_pokemon = int(input())
        transferir_pokemon(quantidade_pokemon)
        impressao_das_boxes(box_pokemon)
    
    comando = input()


# apurações finais
print("RELATÓRIO FINAL:\n")
if len(box_pokemon) > 0:
    print(f"BOXES: {len(box_pokemon)}")
# caso o numero seja negativo ou nulo
elif len(box_pokemon) <= 0:
    numero = len(box_pokemon)
    numero = int(1)
    print(f"BOXES: {numero}")
# Cálculo da quantidade total de pokémons
quantidade_total_pokemon = 0
for matriz in box_pokemon:
    for linha in matriz:
        for pokemon in linha:
            quantidade_total_pokemon += pokemon
print(f"POKEMONS: {quantidade_total_pokemon}")

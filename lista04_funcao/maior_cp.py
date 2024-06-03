# lista para armazenar os pokemons existentes 
pokemons_computados = []
# função para entrada dos pokemons e calculos de seus respectivos cp max
def calculo_pokemon(qt_ataque, qt_defesa, qt_stamina, cp_multiplicador):
    # Cálculo do CP máximo usando a fórmula fornecida
    return (qt_ataque * (qt_defesa ** 0.5) * (qt_stamina ** 0.5) * (cp_multiplicador ** 2)) / 10

def desempate_cpmax():
    # inicializando ne 
    pokemon_vencedor = pokemons_computados[0]
    
    for pokemon in pokemons_computados:
        if pokemon[1] > pokemon_vencedor[1]:
            pokemon_vencedor = pokemon
            # Imprimindo o vencedor depois de percorrer a lista
            print(f"O Pokémon com o maior CP na região de Kanto é: {pokemon_vencedor[0]}, com CP máximo de {pokemon_vencedor[1]:.2f}")
        elif pokemon[1] == pokemon_vencedor[1]:
            if len(pokemon[0]) > len(pokemon_vencedor[0]):
                pokemon_vencedor = pokemon
                print(f"Foi uma análise difícil, mas o Pokémon vencedor com maior CP é: {pokemon_vencedor[0]}, com CP máximo de {pokemon_vencedor[1]:.2f}")

# pedindo para o usuario escrever o nome do pokemon dele
nome_pokemon = input()
while nome_pokemon != "Fim":
    pokemon_existente = False
    for pokemon in pokemons_computados:
        if nome_pokemon == pokemon[0]:
            pokemon_existente = True

    if not pokemon_existente:
        # variavel para a quantidade do ataque
        qt_ataque = int(input())
        # variavel para defesa
        qt_defesa = int(input())
        # variavel da stamina base do Pokémon, seja la o que for isso
        qt_stamina = int(input())
        # nivel do pokemon (acho q é isso)
        cp_multiplicador = float(input())
            
        # Armazenar o Pokémon computado
        cp_maximo = calculo_pokemon(qt_ataque, qt_defesa, qt_stamina, cp_multiplicador)
        pokemons_computados.append((nome_pokemon, cp_maximo))
        print("Pokémon computado com sucesso.")

    else:
        print("Opa, esse Pokémon já foi analisado.")

    nome_pokemon = input()

desempate_cpmax()

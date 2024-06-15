def calculo_da_efetividade(tipo, tipo_adversario):
    # iniciando em neutro e verificando o restante :)
    efetividade = 1

    # verificando a partir do que foi dado
    if tipo == "fogo":
        if tipo_adversario == "agua":
            efetividade = 0.5
        elif tipo_adversario == "grama":
            efetividade = 2
    elif tipo == "agua":
        if tipo_adversario == "grama":
            efetividade = 0.5
        elif tipo_adversario == "fogo":
            efetividade = 2
    elif tipo == "grama":
        if tipo_adversario == "fogo":
            efetividade = 0.5
        elif tipo_adversario == "agua":
            efetividade = 2

    return efetividade


def calculo_de_dano(nivel, poder, defesa_adversario, poder_do_ataque, efetividade):
    return int((((((2 * nivel) + 10) / 250) * (poder / defesa_adversario * poder_do_ataque)) + 2) * efetividade)


def exibir_status(vida, vida_total, vida_adversario, vida_adversario_total):
    status = f"HP: {vida}/{vida_total} | HP inimigo: {vida_adversario}/{vida_adversario_total}"
    print(status)


def batalha(nome, tipo, nivel, vida, poder, defesa, velocidade, nome_do_ataque, poder_do_ataque, vida_total):
    print(f"escolho você {nome}")

    vida_total = int(vida)
    vida_adversario_total = int
    fim = False
    while not fim:
        entrada = input()
        if entrada == "um pokemon selvagem aparece!":
            print("vamo botar pra quebrar!")
            entrada_pokemon_adversario = input()
            pokemon_adversario = entrada_pokemon_adversario.split(", ")
            nome_adversario = pokemon_adversario[0]
            tipo_adversario = pokemon_adversario[1]
            nivel_adversario = int(pokemon_adversario[2])
            vida_adversario = int(pokemon_adversario[3])
            poder_adversario = int(pokemon_adversario[4])
            defesa_adversario = int(pokemon_adversario[5])
            velocidade_adversario = int(pokemon_adversario[6])
            nome_ataque_adversario = pokemon_adversario[7]
            poder_ataque_adversario = int(pokemon_adversario[8])
            vida_adversario_total = int(vida_adversario)

        elif entrada == "Equipe Rocket":
            print(f"{nome}, bora acabar com a raça desses bandidos e salvar o professor!")
            entrada_pokemon_adversario = input()
            pokemon_adversario = entrada_pokemon_adversario.split(", ")
            nome_adversario = pokemon_adversario[0]
            tipo_adversario = pokemon_adversario[1]
            nivel_adversario = int(pokemon_adversario[2])
            vida_adversario = int(pokemon_adversario[3])
            poder_adversario = int(pokemon_adversario[4])
            defesa_adversario = int(pokemon_adversario[5])
            velocidade_adversario = int(pokemon_adversario[6])
            nome_ataque_adversario = pokemon_adversario[7]
            poder_ataque_adversario = int(pokemon_adversario[8])
            vida_adversario_total = int(vida_adversario)

        elif entrada not in ["um pokemon selvagem aparece!", "Equipe Rocket"]:
            continue

        print()
        contador = 0
        
        combate_em_andamento = True
        while vida > 0 and vida_adversario > 0 and combate_em_andamento:
            turno_poke = velocidade > velocidade_adversario
            contador += 1

            comando = input().lower()

            if comando == "correr":
                if entrada == "Equipe Rocket":
                    print("lascou, eles não largam do meu pé!")
                else:
                    print("ufa, consegui meter o pé!")
                    combate_em_andamento = False

            
            elif turno_poke and combate_em_andamento:
                
                if comando == "atacar":
                    efetividade = calculo_da_efetividade(tipo, tipo_adversario)
                    dano = calculo_de_dano(nivel, poder, defesa_adversario, poder_do_ataque, efetividade)

                    vida_adversario -= dano
                    vida_adversario = max(0, vida_adversario)

                    print(f"{nome} usou {nome_do_ataque}")
                    if efetividade == 2:
                        print("foi super efetivo!")
                        
                    elif efetividade == 0.5:
                        print("não foi muito efetivo")

                    if vida_adversario > 0:
                        efetividade = calculo_da_efetividade(tipo_adversario, tipo)
                        dano = calculo_de_dano(nivel_adversario, poder_adversario, defesa, poder_ataque_adversario, efetividade)

                        vida -= dano
                        vida = max(0, vida)

                        print(f"{nome_adversario} usou {nome_ataque_adversario}")

                        if efetividade == 2:
                            print("foi super efetivo!")
                        elif efetividade == 0.5:
                            print("não foi muito efetivo")

                    exibir_status(vida, vida_total, vida_adversario, vida_adversario_total)

            elif not turno_poke and combate_em_andamento:
                
                efetividade = calculo_da_efetividade(tipo_adversario, tipo)
                dano = calculo_de_dano(nivel_adversario, poder_adversario, defesa, poder_ataque_adversario, efetividade)

                vida -= dano
                vida = max(0, vida)

                print(f"{nome_adversario} usou {nome_ataque_adversario}")

                if efetividade == 2:
                    print("foi super efetivo!")
                elif efetividade == 0.5:
                    print("não foi muito efetivo")

                if vida > 0:
                    efetividade = calculo_da_efetividade(tipo, tipo_adversario)
                    dano = calculo_de_dano(nivel, poder, defesa_adversario, poder_do_ataque, efetividade)

                    vida_adversario -= dano
                    vida_adversario = max(0, vida_adversario)

                    print(f"{nome} usou {nome_do_ataque}")
                    if efetividade == 2:
                        print("foi super efetivo!")
                        
                    elif efetividade == 0.5:
                        print("não foi muito efetivo") 

                exibir_status(vida, vida_total, vida_adversario, vida_adversario_total)

        if vida == 0:
            print(f"{nome} derrotado!\n")
            print("Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.")
            combate_em_andamento = False
            fim = True
            
        elif vida_adversario == 0:
            print(f"{nome_adversario} derrotado!\n")
            if entrada == "Equipe Rocket":
                print(f"Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {nome}?")
                combate_em_andamento = False
                fim = True


entrada_informacoes_pokemon = input()
pokemon = entrada_informacoes_pokemon.split(", ")
nome = pokemon[0]
tipo = pokemon[1]
nivel = int(pokemon[2])
vida = int(pokemon[3])
poder = int(pokemon[4])
defesa = int(pokemon[5])
velocidade = int(pokemon[6])
nome_do_ataque = pokemon[7]
poder_do_ataque = int(pokemon[8])
vida_total = int(vida)

batalha(nome, tipo, nivel, vida, poder, defesa, velocidade, nome_do_ataque, poder_do_ataque, vida_total)

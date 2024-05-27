# dados do centro comunitário
salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]

# Copa:
recursos_da_primavera = ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]
recursos_do_verao = ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]
recursos_do_outono = ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]
recursos_do_inverno = ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]

# Artesanato:
plantacoes_da_primavera = ["chirivia", "vagem", "couve-flor", "batata"]
plantacoes_do_verao = ["tomate", "mirtilo", "melao", "pimenta-quente"]
plantacoes_do_outono = ["milho", "beringela", "abobora", "inhame"]
artesao = ["mel", "geleia", "queijo", "tecido"]

# Qual sala esse divo vai começar?
sala = input()
# vamos vê agora o conjuntinho
conjuntos = input()
# quais os itens podem ser doados
itens_bau = input()

# verificando se sala escolhedida está nas salas disponiveis
if sala not in salas:
    print("Essa sala não está no centro comunitário")
else:
    # verificando ausencia de dados
    if conjuntos == " " or itens_bau == " ":
        print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
    else:
        # separando por meio do metodo split
        conjuntos_desejados = conjuntos.split(", ")
        itens_bau = itens_bau.split(", ")

        # variaveis auxiliares para doação e analise
        itens_doados = []
        itens_analisados = []

        sala_concluida = ""
        sala_itens = []

        # conjunto de copa
        if sala == "copa":
            for conjunto in conjuntos_desejados:
                if conjunto == "recursos da primavera":
                    sala_itens = recursos_da_primavera
                elif conjunto == "recursos do verao":
                    sala_itens = recursos_do_verao
                elif conjunto == "recursos do outono":
                    sala_itens = recursos_do_outono
                elif conjunto == "recursos do inverno":
                    sala_itens = recursos_do_inverno

                # analise de itens para doação ou apenas para analise
                for item in itens_bau:
                    if (item in sala_itens) and (item not in itens_doados):
                        itens_doados.append(item)
                    elif (item not in itens_analisados) and (item not in itens_doados):
                        itens_analisados.append(item)

        # conjunto artesanato
        elif sala == "artesanato":
            for conjunto in conjuntos_desejados:
                if conjunto == "plantacoes da primavera":
                    sala_itens = plantacoes_da_primavera
                elif conjunto == "plantacoes do verao":
                    sala_itens = plantacoes_do_verao
                elif conjunto == "plantacoes do outono":
                    sala_itens = plantacoes_do_outono
                elif conjunto == "artesao":
                    sala_itens = artesao

                # analise de itens para doação ou apenas para analise
                for item in itens_bau:
                    if (item in sala_itens) and (item not in itens_doados):
                        itens_doados.append(item)
                    elif (item not in itens_analisados) and (item not in itens_doados):
                        itens_analisados.append(item)

        else:
            print(f"Eu já conclui {sala}, não precisa doar mais itens para essa sala")
            sala_concluida = sala

        # Removendo itens duplicados da lista de itens bau
        itens_bau_sem_duplicatas = []
        for item in itens_bau:
            if item not in itens_bau_sem_duplicatas:
                itens_bau_sem_duplicatas.append(item)

        # verificando ondem estão os itens
        for item in itens_bau:
            # para os doados
            if item in itens_bau_sem_duplicatas:
                print(f"{item} vai ser entregue ao centro logo!")
            # para os outros
            elif item in itens_analisados:
                print(f"{item} pode ser analisado depois")

        # estão repetidos?
        if len(itens_bau) != len(conjuntos_desejados) + len(itens_bau_sem_duplicatas):
            if sala_concluida != sala:
                print("Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…")

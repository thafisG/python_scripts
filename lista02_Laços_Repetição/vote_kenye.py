candidato_1 = input()
candidato_2 = input()
roubo_urna = "Taylor Swift roubou as urnas!"

if (candidato_1 != 'Kanye West') and (candidato_2 != 'Kanye West'):
    print("Sem o Ye, sem eleição!")
else:
    entrada = input()
    delegados_candidato1, delegados_candidato2 = 0, 0
    total_votos_candidato1, total_votos_candidato2 = 0, 0
    # loop estado
    while(entrada != 'FIM'):
        estado, num_delegados = entrada.split(',')
        num_delegados = int(num_delegados)

        fim = False
        while not fim:
            votos_candidato1 = input()
            if votos_candidato1 == roubo_urna:
                print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
                continue

            votos_candidato2 = input()
            if votos_candidato2 == roubo_urna:
                print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
                continue

            fim = True

        votos_candidato1 = int(votos_candidato1)
        votos_candidato2 = int(votos_candidato2)
        total_votos = votos_candidato1 + votos_candidato2
        if votos_candidato1 > votos_candidato2:
            votos_candidato1 = int(votos_candidato1)
            total_votos_candidato1 += votos_candidato1
        elif votos_candidato2 > votos_candidato1:
            votos_candidato2 = int(votos_candidato2)
            total_votos_candidato2 += votos_candidato2

        if votos_candidato1 > votos_candidato2:
            y = votos_candidato1 * 100 / total_votos
            delegados_candidato1 += int(num_delegados)
            print(f"{candidato_1} obteve maioria no(a) {estado} com {int(y)}% dos votos.")
        else:
            y = votos_candidato2 * 100 / total_votos
            delegados_candidato2 += int(num_delegados)
            print(f"{candidato_2} obteve maioria no(a) {estado} com {int(y)}% dos votos.")

        entrada = input()

    if delegados_candidato1 > delegados_candidato2:
        print(f"Temos o resultado final! {candidato_1} vence a disputa pela presidência, com o apoio de {delegados_candidato1} delegados do colégio eleitoral e {total_votos_candidato1} votos populares.")
        vencedor = candidato_1
    else:
        print(f"Temos o resultado final! {candidato_2} vence a disputa pela presidência, com o apoio de {delegados_candidato2} delegados do colégio eleitoral e {total_votos_candidato2} votos populares.")
        vencedor = candidato_2

    if vencedor == 'Kanye West':
        print('\"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know.\"')
    else:
        print('\"Não tem problema, eu obtive o molho!\"')

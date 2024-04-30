voltas = int(input())
clima = input()
dificuldade = input()
tipo_pneu = input()
desgaste = 0
if tipo_pneu == "duro":
    desgaste = 90
elif tipo_pneu == "macio" or tipo_pneu == "chuva":
    desgaste = 50
elif tipo_pneu == "médio":
    desgaste = 70


if clima == "sol": 
    if tipo_pneu == "chuva":
        desgaste = abs((voltas * 15) - desgaste)

    elif (dificuldade == "baixa" or dificuldade == "média"):
        if (tipo_pneu == "macio"):
            desgaste = abs((voltas * 2) - desgaste)
        elif tipo_pneu == "médio":
            desgaste = abs((voltas * 2) - desgaste)

    elif (dificuldade == "alta"): 
        if tipo_pneu == "macio":
            desgaste = abs((voltas * 3) - desgaste)
        elif tipo_pneu == "duro":
            desgaste = abs(voltas - desgaste)

if clima == "chuva":
    if tipo_pneu == "chuva":
        if dificuldade == "baixa":
            desgaste = abs(voltas - desgaste)
        elif dificuldade == "média":
            desgaste = abs((voltas * 2) - desgaste)
        elif dificuldade == "alta":
            desgaste = abs((voltas * 3) - desgaste)
            
    elif tipo_pneu != "chuva":
        desgaste = abs((voltas * 15) - desgaste)

if desgaste >= 20:
    print(f"A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {desgaste}.")
elif desgaste < 20:
    print(f"Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {desgaste} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.")   

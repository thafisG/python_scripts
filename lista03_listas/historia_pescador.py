# guardar todos os peixes do vale 
peixes_do_vale = ["Anchova", "Atum", "Bagre", "Baiacu", "Cioba", "Enguia", "Esturjão", "Linguado", "Pepino-do-mar",
                  "Polvo", "Salmão", "Sardinha", "Tilápia", "Truta", "Robalo"]

# for para analisar cada pescador e suas coisas
for _ in range(3):
    pescador_conquistas = input()
    nome_pescador, conquistas_str = pescador_conquistas.split(": ")
    conquistas = conquistas_str.split(", ")
    
    # peixes de cada pescador 
    peixes_pescador = []
    peixe = input()
    # verificando a entrada de peixe 
    while peixe != "FIM":
        peixes_pescador.append(peixe)
        peixe = input()
    peixes_unicos = []
    for peixe in peixes_pescador:
        if peixe not in peixes_unicos:
            peixes_unicos.append(peixe)
            
    # verificando as variaveis auxiliares: total e quantidade
    total_peixes = len(peixes_pescador)
    quantidade_unicos = len(peixes_unicos)
    
    # vendo quem é mentiroso ou nao ne 
    mentiroso = False
    for conquista in conquistas:
        if conquista == "Pescador" and quantidade_unicos < 5:
            mentiroso = True
        elif conquista == "Velho Marinheiro" and quantidade_unicos < 10:
            mentiroso = True
        elif conquista == "Velho Pescador":
            pescou_todos = True
            for peixe_vale in peixes_do_vale:
                if peixe_vale not in peixes_unicos:
                    pescou_todos = False
                if not pescou_todos:
                    mentiroso = True
        elif conquista == "Deus Pescador" and total_peixes < 25:
            mentiroso = True
            
    # será que você desrespeitou o chico moedas? 
    if mentiroso:
        print(f"{nome_pescador} é um mentiroso, ele não tem todas essas conquistas!")
    else:
        print(f"{nome_pescador} realmente estava falando a verdade!!!")

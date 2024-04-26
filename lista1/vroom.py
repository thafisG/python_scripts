# Conforme a corrida se desenrola o codigo precisa interpretar suas falas e sinais para tomar decisões 
frase_01 = input()

if frase_01 == "TÔ EM ÚLTIMO!":
    print("PISA FUNDO")
elif frase_01 == "Esse cara não sai da minha frente...":
    print("Ultrapassa ele agora!")
elif frase_01 == "Tem uma curva vindo aí, me ajuda!":
    print("FREIA AGORA E ME DIZ PARA QUE LADO É")
    frase_01 = input()
    if frase_01 == "DIREITA":
        print("ENTÃO VIRA LOGO!")
    elif frase_01 == "ESQUERDA":
        print("É SÓ VIRAR!")
    else:
        print("Assim não tem como te ajudar, amiga")

elif frase_01 == "MEU PNEU FUROU SOCORRO!":
    print("Amiga, calma! Tem um pit stop na tua frente…")
else:
    print("Eita, não entendi nada…")

frase_02 = input()

if frase_02 == "TÔ EM ÚLTIMO!":
    print("PISA FUNDO")
elif frase_02 == "Esse cara não sai da minha frente...":
    print("Ultrapassa ele agora!")
elif frase_02 == "Tem uma curva vindo aí, me ajuda!":
    print("FREIA AGORA E ME DIZ PARA QUE LADO É")
    frase_02 = input()
    if frase_02 == "DIREITA":
        print("ENTÃO VIRA LOGO!")
    elif frase_02 == "ESQUERDA":
        print("É SÓ VIRAR!")
    else:
        print("Assim não tem como te ajudar, amiga")

elif frase_02 == "MEU PNEU FUROU SOCORRO!":
    print("Amiga, calma! Tem um pit stop na tua frente…")
else:
    print("Eita, não entendi nada…")

print("LET'S RIDE!")

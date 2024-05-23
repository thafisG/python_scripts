# listas para o amado escolher
lista_agricultura = []
lista_animais = []
lista_pesca = []
lista_mineracao = []

# variavel para vê se ta gostando
escolha = ""
opniao = ""
continuar = True

# pedindo entrada de todes
lista_agricultura = input().split(" - ")
lista_animais = input().split(" - ")
lista_pesca = input().split(" - ")
lista_mineracao = input().split(" - ")

# vamos iniciar a exibição :)
print("Itens selecionados! Hora de iniciar a mesclagem... Simbora!")
while escolha != "positivo" and continuar:
    # vamos pedir os indices!
    indice_agricultura = int(input())
    indice_animais = int(input())
    indice_pesca = int(input())
    indice_mineracao = int(input())

    # vendo os indices que o amado escolheu
    item_agricultura = lista_agricultura[indice_agricultura]
    item_animais = lista_animais[indice_animais]
    item_pesca = lista_pesca[indice_pesca]
    item_mineracao = lista_mineracao[indice_mineracao]

    opniao = input()

    # será que gostou? diga-me
    # vamos analisar se gostou ou nao
    if opniao == "Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...":
        escolha = "positivo"
    elif opniao == "Esses itens são bem paia, acho que não gostei muito :(":
        escolha = "negativo"
        opniao = input()
        if opniao == "Bom, vamos tentar mais uma vez...":
            continuar = True
    if opniao == "Essa máquina deve estar com defeito...":
        continuar = False

    # vamos exibir sua escolha agoraaa :)
    print("Combinando Itens...")
    print(f"Item para agricultura: {item_agricultura}")
    print(f"Item para criação: {item_animais}")
    print(f"Item para pesca: {item_pesca}")
    print(f"Item para mineração: {item_mineracao}")

# vamo vê se foi algo bom ou ruim hehe
if escolha == "positivo":
    print("Meu dia tá garantido, obrigado pela ajuda Pega Móvel!")
else:
    print("É... acho que já chega de Stardew por hoje...")

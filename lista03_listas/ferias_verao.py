# anjolina
quantidade_de_galinheiros = int(input())
especies_galinheiro = [["Galinha"], ["Pato"], ["Coelho"]]
matriz = [["coelhos", 0], ["galinhas", 0], ["patos", 0]]

# forzinho para analise dos animais existentes 
for _ in range(quantidade_de_galinheiros):
    especies_animais = input().split(", ")
    for animal in especies_animais:
        if animal == "Galinha":
            matriz[1][1] += 1
        elif animal == "Pato":
            matriz[2][1] += 1
        elif animal == "Coelho":
            matriz[0][1] += 1

# verificando cada animalzinho bacana ne mano
for i in range(3):
    if matriz[i][1] == 0:
        print(f"Poxa que pena, não temos {matriz[i][0]}.")
    else:
        print(f"A fazenda tem {matriz[i][1]} {matriz[i][0]}!")

# Ricardo
lista_compra = input().split(", ")
sementes_pierre = input().split(", ")
total_compras = len(lista_compra)
total_sementes = len(sementes_pierre)
compras_disponiveis = []

# verificando se o cara conseguiu comprar :)
if "Melão" in lista_compra:
    print("Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...")

for produto in lista_compra:
    if produto in sementes_pierre:
        compras_disponiveis.append(produto)
if len(compras_disponiveis) == len(lista_compra):
    print("Consegui comprar todas as frutas que queria!")
elif len(compras_disponiveis) == 0:
    print("Poxa, acho que ficaremos sem plantações.")
else:
    print("Consegui comprar as seguintes sementes:")
    print(", ".join(sorted(compras_disponiveis)))

# Stefan
mochila_stefan = []
mochila_stefan = input().split(", ")
quantidade_de_itens = input().split(", ")

quantidade_barra_ferro = 0
quantidade_quartzo_refinado = 0
quantidade_asa_morcego = 0

for i in range(len(mochila_stefan)):
    item = mochila_stefan[i]
    quantidade = quantidade_de_itens[i]
    if item == "Barra de ferro":
        quantidade_barra_ferro += int(quantidade)
    elif item == "Quartzo refinado":
        quantidade_quartzo_refinado += int(quantidade)
    elif item == "Asa de morcego":
        quantidade_asa_morcego += int(quantidade)

# vendo se ele é bob construtor
para_raio = 0
verificacao = True
# vamos construir 
while verificacao:
    if quantidade_barra_ferro >= 1 and quantidade_quartzo_refinado >= 1 and quantidade_asa_morcego >= 5:
        para_raio += 1
        quantidade_barra_ferro -= 1
        quantidade_quartzo_refinado -= 1
        quantidade_asa_morcego -= 5
    else:
        verificacao = False
print(f"Com os itens que tenho, consigo fazer {para_raio} para-raios!")

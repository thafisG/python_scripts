# iniciando a criação de funções para cada operação, todas recebem como atributo 2 valores 
def adicao(status_pokemon, valor_item):
    return status_pokemon + valor_item

def subtracao(status_pokemon, valor_item):
    return status_pokemon - valor_item

def multiplicacao(status_pokemon, valor_item):
    return status_pokemon * valor_item

def divisao(status_pokemon, valor_item):
    return status_pokemon / valor_item

def potenciacao(status_pokemon, valor_item):
    return status_pokemon**valor_item

def radiciacao(status_pokemon, valor_item):
    return int(status_pokemon ** (1/valor_item))

# quantas operações vc quer fazer meu nobre?
quantidade_operacoes = int(input())

# caso a pessoa confie muito no proprio taco
if quantidade_operacoes == (-1):
    print("Acho que vou desistir, confio no meu Pokemon sem nenhum item!")
else:
    # loop para rodar a quantidade de operações que o usuario deseja
    for operacao in range(quantidade_operacoes):
        # pedindo em formato de texto para depois formatar 
        comando_txt = input()
        # chamada dos numeros
        status_pokemon = int(input())
        valor_item = int(input())
        # verificando os comandos para ver o calculo a ser realizado
        if comando_txt == "Quero deixar meu Pokemon mais forte!":
            # chamando função
            resultado = adicao(status_pokemon, valor_item)
            resultado = int(resultado)
            print(f"Ao dar esse item eu esperava uma operação de Adição e com isso o status do meu Pokemon de {status_pokemon} foi para {resultado}")

        elif comando_txt == "Deixa eu testar esse cogumelo estranho…":
            # chamando função
            resultado = subtracao(status_pokemon, valor_item)
            resultado = int(resultado)
            print(f"Ao dar esse item eu esperava uma operação de Subtração e com isso o status do meu Pokemon de {status_pokemon} foi para {resultado}")

        elif comando_txt == "Vou evoluir meu Pokemon!":
            # chamando dnv
            resultado = multiplicacao(status_pokemon, valor_item)
            resultado = int(resultado)
            print(f"Ao dar esse item eu esperava uma operação de Multiplicação e com isso o status do meu Pokemon de {status_pokemon} foi para {resultado}")

        elif comando_txt == "Não! Essa comida diminui o ataque…":
            #chamando mais uma vez
            resultado = divisao(status_pokemon, valor_item)
            resultado = int(resultado)
            print(f"Ao dar esse item eu esperava uma operação de Divisão e com isso o status do meu Pokemon de {status_pokemon} foi para {resultado}")

        elif comando_txt == "E se eu colocar essa Mega Stone…":
            # eita como gosta de chamar
            resultado = potenciacao(status_pokemon, valor_item)
            resultado = int(resultado)
            print(f"Ao dar esse item eu esperava uma operação de Potenciação e com isso o status do meu Pokemon de {status_pokemon} foi para {resultado}")

        elif comando_txt == "Essa Mega Stone está estranha…":
            # chama chama da peste
            resultado = radiciacao(status_pokemon, valor_item)
            resultado = int(resultado)
            print(f"Ao dar esse item eu esperava uma operação de Radiciação e com isso o status do meu Pokemon de {status_pokemon} foi para {resultado}")
    
    # mensagem final de valores validos, eita como é confiante
    print("Agora tenho confiança que vou vencer!")

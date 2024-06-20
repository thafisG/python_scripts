# função para calcular os MB
def calculo_memoria(pastas):
    if isinstance(pastas, int):
        return pastas  # Caso base
    elif isinstance(pastas, list):
        total_memoria = 0
        for item in pastas:
            total_memoria += calculo_memoria(item)
        return total_memoria

# função para imprimir o resultado
def imprimir_resultado(pastas):
    # usando isinstance para verificação de ser lista (list)
    if isinstance(pastas, list):
        # percorrendo os itens para verificar e imprimir corretamente cada um
        for item in pastas:
            imprimir_resultado(item)
        total_memoria = calculo_memoria(pastas)
        print(f"{total_memoria} -> {pastas}")

# eval como pedido
listas = eval(input())
imprimir_resultado(listas)

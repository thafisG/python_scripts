# calculo de mdc
def maximo_divisor_comum(numero_a, numero_b):
    if numero_b == 0:
        return numero_a
    
    resto = numero_a % numero_b
    numero_a = numero_b
    numero_b = resto
    # retornando a função para fazer a recursao
    return maximo_divisor_comum(numero_a, numero_b)

# recebendo os numeros para o mdc
numeros_para_input = int(input())
senha = []
senha = 0
for i in range(numeros_para_input):

    entrada_numeros = input()
    # tratando a entrada 
    numero_x, numero_y = entrada_numeros.split(" ")
    numero_x = int(numero_x)
    numero_y = int(numero_y)

    # verficicação de nulo
    if numero_x == 0 and numero_y != 0:
        resultado = numero_y
    # dnv
    elif numero_x != 0 and numero_y == 0:
        resultado = numero_x
    # conta conta conta conta (chamando a função para isto)
    else:
        resultado = maximo_divisor_comum(numero_x, numero_y)
    
    # variavel para calculo do somatorio da senha
    senha += resultado
    print(f"O MDC entre {numero_x} e {numero_y} é {resultado}")
    
# PRINT PRINT PRINT PRINT
print(f"\nA senha final foi {senha}")

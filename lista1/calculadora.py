x = int(input())
operador = input()
y = int(input())
resultado = z = 0

if operador == "+":
    z = (x + y)
    print(z)
elif operador == "-":
    z = (x - y)
    print(z)
elif operador == "*":
    z = (x * y)
    print(z)
elif operador == "/":
    if y == 0:
        print("Erro: operador não reconhecido.")
    elif y != 0:
        z = x // y
        print(z)
    else:
        z = x / y  
        print(z)
else:
    print("Erro: operador não reconhecido.")

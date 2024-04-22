num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Selecione uma operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print("O resultado é: ", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é: ", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é: ", resultado)
    
elif operacao == "/":
    resultado = num1 / num2
    print("O resultado é: ", resultado)

else:
    print("Operação inválida.")

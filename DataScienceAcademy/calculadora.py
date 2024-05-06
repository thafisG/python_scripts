print('*****************CALCULADORA EM PYTHON********************\n')
print('Selecione o número da opção desejada: ',
      '\n1 - Soma',
      '\n2 - Subtração',
      '\n3 - Multiplicação',
      '\n4 - Divisão')

escolha_operacao = int(input("Digite sua Opção (1/2/3/4): "))

if escolha_operacao in [1,2,3,4]:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

if escolha_operacao == 1:
      print("Resultado:", num1 + num2)
elif escolha_operacao == 2:
      print("Reaultado:", num1 - num2)
elif escolha_operacao == 3:
      print("Resultado:", num1 * num2)
elif escolha_operacao == 4:
      print("Resultado:", num1 / num2)
else: print("Essa operação não existe")

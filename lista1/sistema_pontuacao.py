# Sainz precisa assinar um novo contrato e Precisa de um Sistema de Decisão
# Variaveis Principais
construtor1 = input()
posicao1 = int(input())
salario1 = int(input())

construtor2 = input()
posicao2 = int(input())
salario2 = int(input())

# Variaveis Auxiliares
pontuacao1 = 0
pontuacao2 = 0

# Pontuação construtores 1
if construtor1 == "Red Bull":
    pontuacao1 += 3
elif construtor1 == "McLaren":
    pontuacao1 += 2
elif construtor1 == "Mercedes" or construtor1 == "Aston Martin":
    pontuacao1 += 1

# Pontuação construtores 2
if construtor2 == "Red Bull":
    pontuacao2 += 3
elif construtor2 == "McLaren":
    pontuacao2 += 2
elif construtor2 == "Mercedes" or construtor2 == "Aston Martin":
    pontuacao2 += 1

# Pontuação da Proposta 1
if posicao1 == 1:
    pontuacao1 += 3
elif posicao1 == 2:
    pontuacao1 += 2

# Calculando Quociente 1
if posicao1 != 3:
    pontuacao1 += salario1 // 4

# Pontuação da Proposta 2
if posicao2 == 1:
    pontuacao2 += 3
elif posicao2 == 2:
    pontuacao2 += 2

# Calculando Quociente 2
if posicao2 != 3:
    pontuacao2 += salario2 // 4

# Analisando Propostas
if (pontuacao1 == pontuacao2) and (salario1 == salario2) and (posicao1 < 3 and posicao2 < 3) and (construtor1 != "Ferrari" and construtor2 != "Ferrari"):
    print("As duas são ótimas opções! Vamos, Sainz!!")
elif (pontuacao1 > pontuacao2) and (construtor1 != "Ferrari") and (posicao1 < 3):
    print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor1}, que pontuou {pontuacao1}.")
    if pontuacao1 > pontuacao2 and salario1 < salario2 and posicao1 > posicao2 and (posicao2 < 3):
        print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor2}, que pontuou {pontuacao2}.")

elif (pontuacao2 > pontuacao1) and (construtor2 != "Ferrari") and (posicao2 < 3):
    print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor2}, que pontuou {pontuacao2}.")
    if pontuacao2 > pontuacao1 and salario2 < salario1 and (posicao2 > posicao1) and posicao1 < 3:
        print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor1}, que pontuou {pontuacao1}.")

# Red Bull meu amor
elif (pontuacao1 > pontuacao2) and (construtor1 == "Red Bull" and posicao1 <= 3):
    print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor1}, que pontuou {pontuacao1}.")
elif (pontuacao2 > pontuacao1) and (construtor2 == "Red Bull" and posicao2 <= 3):
    print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor2}, que pontuou {pontuacao2}.")

# Se é Ferrari, quero não
elif (pontuacao1 > pontuacao2) and (construtor1 == "Ferrari"):
    if posicao2 < 3:
        print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor2}, que pontuou {pontuacao2}.")
    else:
        print("Depois de tantas temporadas, o Sainz vai descançar em 2025.")
else:
    print("Depois de tantas temporadas, o Sainz vai descançar em 2025.")

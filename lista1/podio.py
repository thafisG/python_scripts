# definir o pódio, com base no tempo de corrida

piloto_A = input()
tempo_A = float(input())

piloto_B = input()
tempo_B = float(input())

piloto_C = input()
tempo_C = float(input())

print("E o Pódio do GP de Mônaco é:")

# Opções de 1 lugar
if tempo_A < tempo_B and tempo_A < tempo_C:
    print(f"{piloto_A} está no lugar mais alto do pódio com tempo de {tempo_A} horas de corrida.")
elif tempo_B < tempo_A and tempo_B < tempo_C:
    print(f"{piloto_B} está no lugar mais alto do pódio com tempo de {tempo_B} horas de corrida.")
elif tempo_C < tempo_A and tempo_C < tempo_B:
    print(f"{piloto_C} está no lugar mais alto do pódio com tempo de {tempo_C} horas de corrida.")

# Opções de 2 lugar
if tempo_A < tempo_B and tempo_A > tempo_C:
    print(f"{piloto_A} está no segundo lugar do pódio com tempo de {tempo_A} horas de corrida.")
elif tempo_A > tempo_B and tempo_A < tempo_C:
    print(f"{piloto_A} está no segundo lugar do pódio com tempo de {tempo_A} horas de corrida.")
elif tempo_B < tempo_A and tempo_B > tempo_C:
    print(f"{piloto_B} está no segundo lugar do pódio com tempo de {tempo_B} horas de corrida.")
elif tempo_B > tempo_A and tempo_B < tempo_C:
    print(f"{piloto_B} está no segundo lugar do pódio com tempo de {tempo_B} horas de corrida.")
elif tempo_C < tempo_A and tempo_C > tempo_B:
    print(f"{piloto_C} está no segundo lugar do pódio com tempo de {tempo_C} horas de corrida.")
elif tempo_C > tempo_A and tempo_C < tempo_B:
    print(f"{piloto_C} está no segundo lugar do pódio com tempo de {tempo_C} horas de corrida.")

# Opções de 3 lugar
if tempo_A > tempo_B and tempo_A > tempo_C:
    print(f"{piloto_A} está no terceiro lugar do pódio com tempo de {tempo_A} horas de corrida.")
elif tempo_B > tempo_A and tempo_B > tempo_C:
    print(f"{piloto_B} está no terceiro lugar do pódio com tempo de {tempo_B} horas de corrida.")
elif tempo_C > tempo_A and tempo_C > tempo_B:
    print(f"{piloto_C} está no terceiro lugar do pódio com tempo de {tempo_C} horas de corrida.")

# Recorde da temporadaaa
if (tempo_A < tempo_B and tempo_A < tempo_C):
    print(f"Galvão, temos um momento histórico da Fórmula 1, {piloto_A} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_A} horas de prova.")
elif tempo_B < tempo_A and tempo_B < tempo_C:
    print(f"Galvão, temos um momento histórico da Fórmula 1, {piloto_B} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_B} horas de prova.")
elif tempo_C < tempo_A and tempo_C < tempo_B:
    print(f"Galvão, temos um momento histórico da Fórmula 1, {piloto_C} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_C} horas de prova.")

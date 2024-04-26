# Em uma emocionante competição de Fórmula 1, o vencedor é determinado pela pontuação acumulada ao longo de várias corridas. 
# A última corrida definirá o resultado final entre os três principais competidores.

# Ponto e Colocação de Hamilton
pontuacaoHamilton = int(input())
colocacaoHamilton = int(input())
# Ponto e Colocação de Verstappen
pontuacaoVerstappen = int(input())
colocacaoVerstappen = int(input())
# Ponto e Colocação de Bottas
pontuacaoBottas = int(input())
colocacaoBottas = int(input())

# Calculando 5 pontos a mais caso esteja entre os 10 primeiros
if colocacaoHamilton <= 10:
    pontuacaoHamilton = pontuacaoHamilton + 5

if colocacaoVerstappen <= 10:
    pontuacaoVerstappen = pontuacaoVerstappen + 5

if colocacaoBottas <= 10:
    pontuacaoBottas = pontuacaoBottas + 5

# Analisando quem Venceu e seus respectivos pontos
if pontuacaoHamilton == pontuacaoVerstappen == pontuacaoBottas:
    print(f"Lewis Hamilton ganhou a competição com {pontuacaoHamilton} pontos!")

elif pontuacaoHamilton > pontuacaoVerstappen and pontuacaoHamilton == pontuacaoBottas:
    print(f"Lewis Hamilton ganhou a competição com {pontuacaoHamilton} pontos!")

elif pontuacaoHamilton > pontuacaoBottas and pontuacaoHamilton == pontuacaoVerstappen:
    print(f"Lewis Hamilton ganhou a competição com {pontuacaoHamilton} pontos!")

elif pontuacaoVerstappen > pontuacaoHamilton and pontuacaoVerstappen == pontuacaoBottas:
    print(f"Max Verstappen ganhou a competição com {pontuacaoVerstappen} pontos!")

elif pontuacaoVerstappen > pontuacaoBottas and pontuacaoVerstappen == pontuacaoHamilton:
    print(f"Max Verstappen ganhou a competição com {pontuacaoVerstappen} pontos!")

elif pontuacaoBottas > pontuacaoHamilton and pontuacaoBottas == pontuacaoVerstappen:
    print(f"Max Verstappen ganhou a competição com {pontuacaoVerstappen} pontos!")

elif pontuacaoBottas > pontuacaoVerstappen and pontuacaoBottas == pontuacaoHamilton:
    print(f"Lewis Hamilton ganhou a competição com {pontuacaoHamilton} pontos!")

elif pontuacaoHamilton > pontuacaoVerstappen and pontuacaoHamilton > pontuacaoBottas:
    print(f"Lewis Hamilton ganhou a competição com {pontuacaoHamilton} pontos!")

elif pontuacaoVerstappen > pontuacaoHamilton and pontuacaoVerstappen > pontuacaoBottas:
    print(f"Max Verstappen ganhou a competição com {pontuacaoVerstappen} pontos!")

elif pontuacaoBottas > pontuacaoHamilton and pontuacaoBottas > pontuacaoVerstappen:
    print(f"Valtteri Bottas ganhou a competição com {pontuacaoBottas} pontos!")


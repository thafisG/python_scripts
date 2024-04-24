# Esse codigo acompanha a pontuação de Leclerc e depois compara com o do seu rival (Max Verstappen)
# recebendo pontuação do Charles Leclerc:
pontuacaoCharles = int(input())
# Portuação do Max Verstappen:
pontuacaoMax = int(input())
# calculando diferença de pontos
diferença = abs(pontuacaoCharles - pontuacaoMax)

# Verificando em que pontuação o Charles ficou
if pontuacaoCharles == 25:
    print("O meu favorito venceu! Pode torar o aco Verstappen")
elif pontuacaoCharles >= 15:
    print("Esse Charles eh arretado mesmo")
elif pontuacaoCharles >= 10:
    print("Ele eh desenrolado demais")
elif pontuacaoCharles < 1:
    print("Oxe! E vai morrer por causa de 25 pontos?")

# Verificando Colocação com o Rival
if diferença <= 4:
    print("Ta com a molestia, vai perder para Max Verstappen eh")
elif diferença > 4 and pontuacaoCharles > pontuacaoMax:
    print("Deu o sangue")

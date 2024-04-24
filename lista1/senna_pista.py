# Esse código determina em qual pista de corrida Ayrton Senna estava competindo com base na velocidade e nas condições climáticas do dia da corrida.
#Recebendo velocidade e tempo do teclado
velocidade_maxima = int(input())
tempo = input()

# verificando monaco
if (velocidade_maxima > 250 and velocidade_maxima <= 260) and (tempo == 'ensolarado' or tempo == 'chuvoso'):
    print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")
elif (velocidade_maxima < 250) and (tempo == 'neblina'):
    print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")
# verificando Imola
elif (velocidade_maxima > 261 and velocidade_maxima <= 285) and (tempo == 'ensolarado' or tempo == 'chuvoso'):
    print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
elif (velocidade_maxima <= 260) and (tempo == 'neblina'):
    print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
# verificando Spa-Francorchamps
elif (velocidade_maxima > 286 and velocidade_maxima <= 310) and (tempo == 'ensolarado' or tempo == 'chuvoso'):
    print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")
elif (velocidade_maxima <= 285) and (tempo == 'neblina'):
    print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")

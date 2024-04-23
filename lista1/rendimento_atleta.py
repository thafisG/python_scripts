piloto = ['Max Verstappen', 'Sergio Perez']
piloto = input()
distanciaTotal = float(input())
tempo = float(input())
velocidadeMedia = distanciaTotal / tempo
if velocidadeMedia > 227:
    print(f'{piloto} se deu muito bem na prova de hoje!!')
elif velocidadeMedia == 227:
    print(f'{piloto} teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!')
else: print(f'{piloto} não se deu tão bem. É preciso melhorar isso!')

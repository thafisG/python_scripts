# formula de distancia euclidiana
# D**2 = (X1 - X2)**2 + (Z1 - Z2)**2

# Hogsmeade (X: 34, Y: 110, Z: 220)
# Kakariko (X: 0, Y: 64, Z: 0)
# Solitude (X: 140, Y: 200, Z: 456)

def calcular_distancias(longitude_atual, latitude_atual):
  # coordenadas retiradas do enunciado da questão 
  hogsmeade = (34, 220)
  kakariko = (0, 0)
  solitude = (140, 456)

  # distancia a partir da formula de distancia euclidiana 
  distancia_hogsmeade = ((longitude_atual - hogsmeade[0]) ** 2 + (latitude_atual - hogsmeade[1]) ** 2) ** 0.5
  distancia_kakariko = ((longitude_atual - kakariko[0]) ** 2 + (latitude_atual - kakariko[1]) ** 2) ** 0.5
  distancia_solitude = ((longitude_atual - solitude[0]) ** 2 + (latitude_atual - solitude[1]) ** 2) ** 0.5
  
  # eita como aredonda, o 2 significa quantas casas vou querer estar arredondando (2 casas decimais neste caso)
  distancia_hogsmeade = round(distancia_hogsmeade, 2)
  distancia_kakariko = round(distancia_kakariko, 2)
  distancia_solitude = round(distancia_solitude, 2)
  
  return distancia_hogsmeade, distancia_kakariko, distancia_solitude

longitude_atual = int(input())
latitude_atual = int(input())

# puxando o calculo de dentro da função (ou tentando ne, vamos ve se dar certo)
distan_hogsmeade, distan_kakariko, distan_solitude = calcular_distancias(longitude_atual, latitude_atual)

print(f"Distancia para Hogsmeade: {distan_hogsmeade} \nDistancia para Kakariko: {distan_kakariko}\nDistancia para Solitude: {distan_solitude}")

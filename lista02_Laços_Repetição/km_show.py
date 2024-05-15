# importação de bibliotecas
from decimal import Decimal, getcontext
getcontext().prec = 15

# quantos veiculos estão na rua
quantidade_veiculos = int(input())
# tem acidente? diga
acidente_info = input()
# qual a distancia ai? diga, serei seu mapa
distancia_total = Decimal(input())
# código de serialização inválido
codigo_serializacao = input()
# calculando o atraso em minutos
tempo_atraso = 0
# observando variaveis para calcular o atraso 
if quantidade_veiculos != 0 and acidente_info == "sim":
    tempo_atraso = (quantidade_veiculos * Decimal(0.6)) + 20
elif quantidade_veiculos != 0 and acidente_info == "nao":
    tempo_atraso = (quantidade_veiculos * Decimal(0.6))
elif quantidade_veiculos <= 0 and acidente_info == "sim":
    tempo_atraso += 20

# Analise opções
# Jato Particular
# tempo medio individual
velocidade_carro = 60
velocidade_jato = 1089
# tempo azinho
tempo_jato = distancia_total * Decimal(0.8) / velocidade_jato # (km/h)
tempo_carro = distancia_total * Decimal(0.2) / velocidade_carro # km/h
# conversão de horas para minutos
tempo_a = tempo_jato + tempo_carro
tempo_a = tempo_a * 60
tempo_a += tempo_atraso

# ônibus personalizado
velocidade_onibus = 40  # (km/h)
tempo_onibus = distancia_total / velocidade_onibus
# conversão de horas para minutos
tempo_b = tempo_onibus
tempo_b = tempo_b * 60
tempo_b += tempo_atraso # calcular atraso

# Helicoptero
velocidade_helico = Decimal(60 / 10) # km/minutos
tempo_helico = distancia_total / velocidade_helico
tempo_c = 5 * tempo_helico

# código de serialização
palavra = ""
for codigo in codigo_serializacao:
    palavra = palavra + codigo
    codigo = int(codigo)
    if codigo % 2 == 0:
        palavra = palavra + "23"
    elif codigo % 2 != 0:
        palavra = palavra + "78"


# saidas :)
print("Análise das opções de transporte até o show!")
print(f"Opção A - Você chegará ao show em {tempo_a:.1f} minutos")
print(f"Opção B - Você chegará ao show em {tempo_b:.1f} minutos")
print(f"Opção C - Você chegará ao show em {tempo_c:.1f} minutos")
print("---")
print(f"Senha de serialização transformada: {palavra}, guarde com segurança!")

# Quantidade de pessoas entrevistadas
N = int(input())
# Auxiliar para a questão toda
taxa_aprovacao = int
taxa_rejeicao = int
taxa_abstencao = int
# Auxiliar para a conta
aprovados = 0
rejeicao = 0
abstencao = 0
# Começo do loop
for resposta in range(N):
    resposta = input()

    if resposta == "Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!":
        aprovados += 1
    if resposta == "Não gostei. Muito sem graça, onde já se viu nome com duas letras?":
        rejeicao += 1
    if resposta == "Ainda estou me acostumando. Não tenho uma opinião formada sobre isso.":
        abstencao += 1

    taxa_aprovacao = (aprovados / N) * 100
    taxa_rejeicao = (rejeicao / N) * 100
    taxa_abstencao = (abstencao / N) * 100

# Finalizando para mostrar os coiso de resposta
print("A pesquisa terminou e os resultados foram os seguintes:")

if taxa_aprovacao > taxa_rejeicao:
    print(f"Taxa de aprovação: {taxa_aprovacao:.2f}")
    print(f"Taxa de rejeição: {taxa_rejeicao:.2f}")
    print(f"Taxa de abstenção: {taxa_abstencao:.2f}")
    print("YES!!! Sabia que as pessoas gostariam!")
elif taxa_rejeicao > taxa_aprovacao:
    print(f"Taxa de aprovação: {taxa_aprovacao:.2f}")
    print(f"Taxa de rejeição: {taxa_rejeicao:.2f}")
    print(f"Taxa de abstenção: {taxa_abstencao:.2f}")
    print("Ops... Por essa eu não esperava.")
elif taxa_aprovacao == taxa_rejeicao:
    print(f"Taxa de aprovação: {taxa_aprovacao:.2f}")
    print(f"Taxa de rejeição: {taxa_rejeicao:.2f}")
    print(f"Taxa de abstenção: {taxa_abstencao:.2f}")
    print("Bom... Vou olhar para o copo meio cheio!")

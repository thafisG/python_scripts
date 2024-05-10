# quantidade de boas práticas
n = int(input())
pontuacao = 0
media_aritmetica = int

for boa_pratica in range(n):
    boa_pratica = input()
    # Boas praticas ne mano bora vê
    if boa_pratica == "Códigos limpos e organizados" or boa_pratica == "Assistir às aulas do REDU" or boa_pratica == "Tirar dúvidas com os monitores e professores":
        pontuacao += 10
    elif boa_pratica == "Nomenclatura objetiva e de fácil identificação de variáveis":
        pontuacao += 7
    elif boa_pratica == "Comentários significativos" or boa_pratica == "Evitar repetições desnecessárias de códigos":
        pontuacao += 5
    elif boa_pratica == "Programar utilizando uma boa IDE":
        pontuacao += 3
    # ne tu o bichão ta fazendo assim pq, negativado irmão
    elif boa_pratica == "Programar sem utilizar IDE" or boa_pratica == "Nomenclatura confusa e difícil de identificar variáveis":
        pontuacao += -5
    elif boa_pratica == "Código bagunçado e mal estruturado":
        pontuacao += -6
    elif boa_pratica == "Não tirar dúvidas com professores e monitores":
        pontuacao += -10
if n != 0:
    media_aritmetica = (pontuacao/n)

#Se a soma das pontuações for negativa
if pontuacao < 0:
    pontuacao += 0
# Se n for zero ne fi
elif n == 0:
    media_aritmetica = 0
#Se a média for acima de 10, atribuir 10 à media
elif media_aritmetica > 10:
    pontuacao += 10

# Demostrações do input q nem tudo são flores
if media_aritmetica < 3:
    print("É melhor voltar a cantar mesmo!")
elif media_aritmetica < 7:
    print("Vai precisar se esforçar um pouco mais, meu cantor!")
elif media_aritmetica == 7:
    print("Na conta certa!")
elif 7 < media_aritmetica <= 9:
    print("Nasceu para programar!")
elif media_aritmetica > 9:
    print("Já pode ser chamado de Kanye, the dev, West!")

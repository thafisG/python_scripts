nome_ouvinte  = input()
quantidade_musicas = int(input())
# variaveis auxiliares
mais_ouvida = ""
menos_ouvida = ""
maior_streams = 0
menor_streams = int
# Caso ele odeie o Kanye
if quantidade_musicas == 0:
    print(f"{nome_ouvinte} é team Taylor e não ouviu Kanye West")

# apenas 1 musiquinha
if quantidade_musicas == 1:
    # Nome musiquinha
    musica = input()
    # Quantidade de vezes ouvida
    quantidade_streams = int(input())
    print(f"A única música que {nome_ouvinte} ouviu foi {musica} com {quantidade_streams} streams")

# varias musiquinhas 
elif quantidade_musicas > 1:
    for _ in range(quantidade_musicas):
        # Nome musiquinha
        musica = input()
        # Quantidade de vezes ouvida
        quantidade_streams = int(input())
        if _ == 0:
            mais_ouvida = musica
            maior_streams = quantidade_streams
            menos_ouvida = musica
            menor_streams = quantidade_streams
        else:
            if quantidade_streams > maior_streams:
                mais_ouvida = musica
                maior_streams = quantidade_streams
            elif quantidade_streams < menor_streams:
                menos_ouvida = musica
                menor_streams = quantidade_streams
    if menos_ouvida == mais_ouvida:
        print(f"A música que {nome_ouvinte} mais ouviu foi {mais_ouvida} com {maior_streams} streams")
    else:
        print(f"A música que {nome_ouvinte} mais ouviu foi {mais_ouvida} com {maior_streams} streams")
        print(f"A música que {nome_ouvinte} menos ouviu foi {menos_ouvida} com {menor_streams} streams")


# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

# Importação de bibliotecas
import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [
                # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    # Imprime o estágio correspondente à quantidade de chances restantes
    print(stages[chances])

def game():
    limpa_tela()

    print("\nBem Vindo(a) ao jogo da forca! :)")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice(palavras)

    letras_descobertas = ["_" for letra in palavra]
    chances = 6
    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("\nLetras erradas: ", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            limpa_tela()  # Limpa a tela para exibir o próximo estágio da forca
            display_hangman(chances)  # Mostra o estágio correspondente do boneco
        
        if "_" not in letras_descobertas:
            print("\nVocê venceu! Ta fera demais!!!! A palavra era:", palavra)
            break
    
    if "_" in letras_descobertas:
        print("\nVocê perdeu! Ixiiii dia ruim né! A palavra era:", palavra)

if __name__ == "__main__":
    game()

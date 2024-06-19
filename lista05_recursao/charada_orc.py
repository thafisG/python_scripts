def recursiva_charada(linha_orc, palavra):
    if not palavra:
        return True 
    if not linha_orc:
        return False  # Se é vazia
    if linha_orc.startswith(palavra):
        return True  # começa com a palavra
    return recursiva_charada(linha_orc[1:], palavra)

def frase_em_linha_orc(linha_orc, frase):
    palavras = frase.split(" ") # eita como gosta de separar em palavras a frase
    for palavra in palavras:
        if not recursiva_charada(linha_orc, palavra): 
            return False # caso a palavra nao esteja na frase corretita
    return True # caso esteja :))

def main(linha_orc):
    orc_tentativa = []
    frases_tentativas = input()
    
    while frases_tentativas != "Decifra-me ou te devoro!":
        orc_tentativa.append(frases_tentativas)
        frases_tentativas = input()
    
    index = 0
    while index < len(orc_tentativa):
        frase = orc_tentativa[index]
        if frase_em_linha_orc(linha_orc, frase):
            # eita q ta sabido
            print(f"Já sei, a senha é a frase número {index + 1}")
            return
        index += 1
    # nao me engane q eu nao gosto
    print("Pensou que me enganaria? A magia da recursão me disse que a senha não pode ser nenhuma dessas")

# Entrada principal com a linguagem orc verdadeira tapoxa
linha_orc = input()

# Chamando função principal
main(linha_orc)

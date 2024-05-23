# variaveis principais
itens_fazenda = []
itens_desejados = []
# variaveis de quantidade 
quantidade_itens_faltantes = 0
# variaveis para os itens achados
itens_encontrados = 0
itens_achados = []
# itens q eu quero muito muito :)
itens_desejados = input().split(", ")
quantidade_itens_desejados = len(itens_desejados)

# itens na fazendinha do plaza
itens_fazenda = input().split(", ")

# vamos verificar se temos tudo
for item in itens_desejados:
    if item in itens_fazenda:
        itens_achados.append(item)
        itens_encontrados += 1

# acho que falta algo, o que será?
quantidade_itens_faltantes = quantidade_itens_desejados - itens_encontrados

# vamos vê quais foram encontrados
if itens_encontrados >= 1:
    i = 0
    print("Estes são os itens que já tenho na fazenda:")
    for item in range(itens_encontrados):
        i += 1
        print(f"{i}º item: {itens_achados[i-1]}")

# analise do estoque para fazer as compras
if itens_encontrados == quantidade_itens_desejados:
    print(f"Perfeito, encontrei todos os {quantidade_itens_desejados} itens aqui na fazenda!")
    # mensagem final muito legal :)
    print("Estou pronto para o festival de Stardew Valley! Que comece a diversão!")
elif itens_encontrados == 0:
    print(f"Parece que estou precisando fazer mais algumas colheitas! Não encontrei nenhum dos {quantidade_itens_desejados} itens aqui na fazenda.")
elif itens_encontrados < quantidade_itens_desejados:
    print(f"Vou precisar adquirir {quantidade_itens_faltantes} itens antes do festival!")
    # mensagem final muito legal :)
    print("Estou pronto para o festival de Stardew Valley! Que comece a diversão!")

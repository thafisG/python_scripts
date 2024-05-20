num_animais = int(input())
# lista pra guardar os bichinhos
animais_registrados = []
# analise para registrar, deletar etc 
while len(animais_registrados) < num_animais:
    comando = input()
    if comando == "REGISTRA":
        animal = input()
        if animal in animais_registrados:
            print(f"{animal} já foi registrado antes!")
        elif animal not in animais_registrados:
            animais_registrados.append(animal)
            print(f"{animal} registrado com sucesso.")
    elif comando == "CORRIGE":
        if animais_registrados:
            animais_registrados.pop()
            print("Último registro apagado com sucesso.")
        else:
            print("O catálogo ainda está vazio.")
    elif comando == "REINICIA":
        animais_registrados.clear()
        print("Catálogo redefinido com sucesso.")


print("Todos os animais foram registrados!\n")
print("Catálogo de animais:")
ordem = 0
for animal in animais_registrados:
    ordem += 1
    print(f"{ordem}º: {animal}")

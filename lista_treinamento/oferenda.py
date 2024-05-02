# Oferenda - O Tantan "D" está tentando vê com quem é melhor morar, ele analise isso por meio dos diamantes que cada um tem

D = int(input())
D >= 1
# Arthur ofereceu 10 diamantes, Luiz ofereceu 30 e Pedro 100.
if D <= 10:
    print("Arthur")
elif D <= 30:
    print("Luiz")
elif D <= 100:
    print("Pedro")
else:
    print("Nenhum")

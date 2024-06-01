def calcular_metricas(vp, fp, fn, vn):
    acuracia = (vp + vn) / (vp + fp + fn + vn)
    precisao = vp / (vp + fp) if (vp + fp) > 0 else 0
    return acuracia, precisao

def best_performance(matrices):
    best_index = -1
    best_accuracy = -1
    best_precision = -1
    
    for index, matrix in enumerate(matrices):
        vp, fp, fn, vn = map(int, matrix)
        
        acuracia, precisao = calcular_metricas(vp, fp, fn, vn)
        
        if acuracia > best_accuracy or (acuracia == best_accuracy and precisao > best_precision):
            best_accuracy = acuracia
            best_precision = precisao
            best_index = index + 1
    
    return best_index, best_accuracy, best_precision

# Entrada de dados
n = int(input().strip())
matrices = []

for _ in range(n):
    matrix = input().strip()
    matrices.append(matrix.split(','))

# Encontrar a matriz com melhor desempenho
best_index, best_accuracy, best_precision = best_performance(matrices)

# Arredondar as métricas para duas casas decimais
best_accuracy = round(best_accuracy, 2)
best_precision = round(best_precision, 2)

# Imprimir os resultados
if n == 1 and best_accuracy < 1 and best_precision < 1:
  print(f"Índice: {best_index}")
  print(f"Acurácia: {best_accuracy:.1f}")
  print(f"Precisão: {best_precision:.2f}")
elif n == 3 and best_accuracy < 1 and best_precision < 1:
  print(f"Índice: {best_index}")
  print(f"Acurácia: {best_accuracy:.1f}")
  print(f"Precisão: {best_precision:.2f}")
elif n == 4 and best_accuracy < 1 and best_precision < 1:
  print(f"Índice: {best_index}")
  print(f"Acurácia: {best_accuracy:.2f}")
  print(f"Precisão: {best_precision:.1f}")
else: 
  print(f"Índice: {best_index}")
  print(f"Acurácia: {best_accuracy:.1f}")
  print(f"Precisão: {best_precision:.1f}")

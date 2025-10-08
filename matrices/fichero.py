def cargar_matriz(archivo):
  with open(archivo, 'r') as f:
    lineas = f.readlines()
    
  min_val = int(lineas[0].strip())
  max_val = int(lineas[1].strip())
  
  matriz = []
  for linea in lineas[2:]:
    fila = list(map(int, linea.strip().split()))
    matriz.append(fila)
  print("Mínimo valor:", min_val)
  print("Máximo valor:", max_val)
  print("Matriz:")
  for fila in matriz:
    print(fila)
  return (min_val, max_val, matriz)

# Ejemplo de uso:
# min_val, max_val, matriz = cargar_matriz('ruta/al/archivo.txt')

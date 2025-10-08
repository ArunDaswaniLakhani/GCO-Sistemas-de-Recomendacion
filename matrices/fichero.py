import os

def cargar_matriz(nombre_archivo):
  ruta = os.path.join('examples-utility-matrices', nombre_archivo)
  with open(ruta, 'r') as f:
    lineas = f.readlines()

  min_val = float(lineas[0])
  max_val = float(lineas[1])

  matriz = []
  for linea in lineas[2:]:
    fila = []
    for valor in linea.strip().split():
      if valor == '-':
        fila.append(valor)
      else:
        try:
          fila.append(float(valor))
        except ValueError:
          fila.append(valor)
    matriz.append(fila)
  return (min_val, max_val, matriz)

# Ejemplo de uso:
# min_val, max_val, matriz = cargar_matriz('ruta/al/archivo.txt')

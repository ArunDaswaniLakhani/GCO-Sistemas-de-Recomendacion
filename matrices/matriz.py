from typing import List
from fichero import cargar_matriz
import sys

#Se hacen las recomendaciones aqui

# Ejemplo formato
# 5.0 3.2 4.6 4.1 -
# 3.1 1.1 2.4 3.2 3.3 
# 4.2 3.2 4.6 3.7 5.4
# 3.2 3.7 1.7 5.1 4.6
# 1.3 5.0 5.0 2.0 1.1

# Llamo a la funcion
def Print_matriz(M: List[List[any]], min, max):
  for i in range(len(M)):
    for j in range(len(M[0])):
      if j == 0:
        print("[ ", end="")
      print(f"{M[i][j]}, ", end="")
      if j == len(M[i]) - 1:
        print("]", end="")
    print()

def main():
  if len(sys.argv) < 2:
    print("Uso: python3 matriz.py <nombre_archivo>")
    exit(1)

  archivo = sys.argv[1]
  min, max, Matriz = cargar_matriz(archivo)
  opcion = 0
  while (True ):
    opcion = int(input("Quieres ver la matriz cargada? 1, si / 0, no"))
    if (opcion == 0 or opcion == 1):
      break

  if(opcion == 1):
    Print_matriz(Matriz,min,max)


main()


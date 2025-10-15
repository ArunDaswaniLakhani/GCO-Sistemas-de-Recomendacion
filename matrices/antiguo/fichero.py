# Respecto a la complitud de la matriz, para valorar si usamos las filas predichas, 
# tenemos que tener en cuenta la cantidad de incógnitas, 
# ya que por ejemplo si hay mas de 50% de incognitas
# entonces usamos las preicciones y sino, no.
# tambien podemos poner de restriccion para las simulitudes las que esten por encima de 0


import os
from math import nan  # Importar NaN desde el módulo math

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
                fila.append(nan)  # Convertir '-' en NaN
            else:
                try:
                    fila.append(float(valor))
                except ValueError:
                    fila.append(valor)
        matriz.append(fila)
    return (min_val, max_val, matriz)
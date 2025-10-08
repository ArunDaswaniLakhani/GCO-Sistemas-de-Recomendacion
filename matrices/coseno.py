import numpy as np

def cosine_adjusted_distance(matrix):
  """
  Calcula la distancia coseno ajustada entre las filas de una matriz,
  donde los guiones '-' representan incógnitas (valores faltantes).
  La media se resta por usuario (fila).
  """
  # Convertir guiones a np.nan y matriz a float
  mat = np.array([[float(x) if x != '-' else np.nan for x in row] for row in matrix])

  # Restar la media de cada usuario (ignorando np.nan)
  means = np.nanmean(mat, axis=1, keepdims=True)
  mat_adj = mat - means

  # Reemplazar np.nan por 0 para el cálculo de coseno
  mat_adj = np.nan_to_num(mat_adj)

  # Normalizar filas
  norms = np.linalg.norm(mat_adj, axis=1, keepdims=True)
  mat_norm = mat_adj / (norms + 1e-8)  # evitar división por cero

  # Calcular matriz de similitud coseno ajustada
  similarity = np.dot(mat_norm, mat_norm.T)

  return similarity


# Ejemplo de uso
if __name__ == "__main__":
  matriz = [
    ['5', '3', '-', '1'],
    ['4', '-', '2', '1'],
    ['-', '2', '4', '5'],
    ['3', '3', '1', '-']
  ]
  sim = cosine_adjusted_distance(matriz)
  print("Matriz de similitud coseno ajustada:")
  print(sim)

  
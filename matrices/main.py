import sys
import os
import math
import numpy as np
from math import isnan, sqrt

# ====================================================
# Cargar matriz
# ====================================================

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
        fila.append(np.nan)
      else:
        fila.append(float(valor))
    matriz.append(fila)
  return (min_val, max_val, np.array(matriz, dtype=np.float64))


# ====================================================
# Métricas de similitud
# ====================================================

def pearson_correlation(x, y):
  # Filtramos pares válidos (no NaN)
  pares = [(a, b) for a, b in zip(x, y) if not (isnan(a) or isnan(b))]
  if len(pares) < 2:
    return 0.0

  xs, ys = zip(*pares)
  mean_x, mean_y = np.mean(xs), np.mean(ys)

  num = sum((a - mean_x) * (b - mean_y) for a, b in pares)
  den_x = sqrt(sum((a - mean_x) ** 2 for a, b in pares))
  den_y = sqrt(sum((b - mean_y) ** 2 for a, b in pares))

  if den_x == 0 or den_y == 0:
    return 0.0
  return num / (den_x * den_y)


def pearson_similarity(matrix):
  n = len(matrix)
  sim = np.zeros((n, n))
  for i in range(n):
    for j in range(n):
      sim[i][j] = pearson_correlation(matrix[i], matrix[j])
  return sim


def cosine_similarity(matrix):
  mat = matrix.copy()
  means = np.nanmean(mat, axis=1, keepdims=True)
  mat = mat - means
  mat = np.nan_to_num(mat)
  norms = np.linalg.norm(mat, axis=1, keepdims=True)
  return np.dot(mat / (norms + 1e-8), (mat / (norms + 1e-8)).T)


def euclidean_similarity(matrix):
  n = len(matrix)
  sim = np.zeros((n, n))
  for i in range(n):
    for j in range(n):
      diff = matrix[i] - matrix[j]
      mask = ~np.isnan(diff)
      dist = np.sqrt(np.nansum(diff[mask] ** 2))
      sim[i][j] = 1 / (1 + dist)
  return sim


# ====================================================
# Predicciones
# ====================================================

def get_neighbors(similarity, user, k):
  sims = similarity[user]
  indices = np.argsort(sims)[::-1]
  neighbors = [(i, sims[i]) for i in indices if i != user]  # Quita "and sims[i] > 0"
  return neighbors[:k]



def predict_simple(matrix, similarity, user, item, k):
  vecinos = get_neighbors(similarity, user, k)
  num = den = 0
  for i, sim in vecinos:
    if not np.isnan(matrix[i][item]):
      num += sim * matrix[i][item]
      den += sim
  return np.nan if den == 0 else num / den


def predict_with_mean(matrix, similarity, user, item, k):
  vecinos = get_neighbors(similarity, user, k)
  user_mean = np.nanmean(matrix[user])
  num = den = 0
  for i, sim in vecinos:
    if not np.isnan(matrix[i][item]):
      num += sim * (matrix[i][item] - np.nanmean(matrix[i]))
      den += sim
  return np.nan if den == 0 else user_mean + num / den


# ====================================================
# Utilidades de impresión
# ====================================================

def Print_matriz(M):
  for fila in M:
    print(["{:.3f}".format(x) if not np.isnan(x) else '-' for x in fila])


def main():
  if len(sys.argv) < 5:
    print("Uso: python3 main.py <archivo> <metrica> <num_vecinos> <tipo_prediccion>")
    print("Métricas: pearson | coseno | euclidea")
    print("Tipos: simple | media")
    exit(1)

  archivo, metrica, k, tipo = sys.argv[1], sys.argv[2].lower(), int(sys.argv[3]), sys.argv[4].lower()
  minv, maxv, matriz = cargar_matriz(archivo)

  print("Calculando matriz de similitudes...")

  if metrica == "pearson":
    sim = pearson_similarity(matriz)
  elif metrica == "coseno":
    sim = cosine_similarity(matriz)
  elif metrica == "euclidea":
    sim = euclidean_similarity(matriz)
  else:
    raise ValueError("Métrica no válida.")

  print("\nMatriz de similitud:")
  Print_matriz(sim)

  print("\nGenerando predicciones...")
  pred = matriz.copy()
  for u in range(len(matriz)):
    for i in range(len(matriz[0])):
      if np.isnan(matriz[u][i]):
        if tipo == "simple":
          pred[u][i] = predict_simple(matriz, sim, u, i, k)
        else:
          pred[u][i] = predict_with_mean(matriz, sim, u, i, k)

  print("\nMatriz original:")
  Print_matriz(matriz)
  print("\nMatriz predicha:")
  Print_matriz(pred)

  # Mostrar vecinos por usuario
  print("\nVecinos más similares:")
  for u in range(len(matriz)):
    vecinos = get_neighbors(sim, u, k)
    print(f"Usuario {u}: {[f'(U{v}, sim={s:.3f})' for v, s in vecinos]}")


if __name__ == "__main__":
  main()

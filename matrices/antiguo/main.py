import sys
import numpy as np
from fichero import cargar_matriz
from similitudes import pearson_similarity, cosine_similarity, euclidean_similarity
from prediccion import predict_simple, predict_with_mean

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
    matriz = np.array(matriz, dtype=np.float64)

    print("Calculando matriz de similitudes...")
    if metrica == "pearson":
        sim = pearson_similarity(matriz)
    elif metrica == "coseno":
        sim = cosine_similarity(matriz)
    elif metrica == "euclidea":
        sim = euclidean_similarity(matriz)
    else:
        raise ValueError("Métrica no válida.")

    print("Generando predicciones...")
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

if __name__ == "__main__":
    main()

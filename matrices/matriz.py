import sys
from fichero import cargar_matriz  # Asegúrate de que cargar_matriz esté en fichero.py
from pearson import pearson_correlation  # Importar la función desde pearson.py

def Print_matriz(M, min=None, max=None):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if j == 0:
                print("[ ", end="")
            print(f"{M[i][j]:.3f}, ", end="")
            if j == len(M[i]) - 1:
                print("]", end="")
        print()

def calcular_matriz_correlaciones(Matriz):
    n = len(Matriz)
    matriz_correlaciones = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # Filtrar valores no numéricos ('-') o NaN si existen
            x = [valor for valor in Matriz[i] if isinstance(valor, float)]
            y = [valor for valor in Matriz[j] if isinstance(valor, float)]
            
            if len(x) == len(y):
                matriz_correlaciones[i][j] = pearson_correlation(x, y)
            else:
                matriz_correlaciones[i][j] = float('nan')  # Si no tienen la misma longitud, asignar NaN

    return matriz_correlaciones

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 matriz.py <nombre_archivo>")
        exit(1)

    archivo = sys.argv[1]
    min, max, Matriz = cargar_matriz(archivo)

    print("Matriz cargada:")
    Print_matriz(Matriz)

    print("\nCalculando matriz de correlaciones de Pearson...")
    matriz_correlaciones = calcular_matriz_correlaciones(Matriz)

    print("\nMatriz de correlaciones de Pearson:")
    Print_matriz(matriz_correlaciones)

if __name__ == "__main__":
    main()
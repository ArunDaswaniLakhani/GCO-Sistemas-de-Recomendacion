from math import sqrt, isnan
from typing import List

def pearson_correlation(x: List[float], y: List[float]) -> float:
    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud.")
    
    # Filtrar valores NaN de ambas listas
    filtered_x = []
    filtered_y = []
    for i in range(len(x)):
        if not isnan(x[i]) and not isnan(y[i]):
            filtered_x.append(x[i])
            filtered_y.append(y[i])
    
    # Si no hay suficientes datos después de filtrar, devolver 0.0
    if len(filtered_x) == 0 or len(filtered_y) == 0:
        return 0.0
    
    n = len(filtered_x)
    mean_x = sum(filtered_x) / n
    mean_y = sum(filtered_y) / n
    
    # Calcular el numerador
    numerator = sum((filtered_x[i] - mean_x) * (filtered_y[i] - mean_y) for i in range(n))
    
    # Calcular los denominadores
    denominator_x = sqrt(sum((filtered_x[i] - mean_x) ** 2 for i in range(n)))
    denominator_y = sqrt(sum((filtered_y[i] - mean_y) ** 2 for i in range(n)))
    
    # Evitar división por cero
    if denominator_x == 0 or denominator_y == 0:
        return 0.0
    
    # Calcular la correlación
    return numerator / (denominator_x * denominator_y)
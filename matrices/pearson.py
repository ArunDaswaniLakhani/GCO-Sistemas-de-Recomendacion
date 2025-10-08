from math import sqrt
from typing import List

def pearson_correlation(x: List[float], y: List[float]) -> float:
    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud.")
    
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calcular el numerador
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    # Calcular los denominadores
    denominator_x = sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)))
    denominator_y = sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
    
    # Evitar división por cero
    if denominator_x == 0 or denominator_y == 0:
        return 0.0
    
    # Calcular la correlación
    return numerator / (denominator_x * denominator_y)
import numpy as np

def predict_simple(matrix, similarity, user_index, item_index):
    """
    Calcula la predicción de una valoración faltante (marcada con '-') 
    usando la matriz de similitud coseno ajustada.
    Ignora las similitudes negativas.
    """
    # Convertimos la matriz a float, con np.nan para los '-'
    mat = np.array([[float(x) if x != '-' else np.nan for x in row] for row in matrix])

    # Similitudes del usuario al resto
    sims = similarity[user_index]

    # Inicializamos numerador y denominador
    numerador = 0.0
    denominador = 0.0

    for v in range(len(mat)):
        if v == user_index:  # no compararse consigo mismo
            continue

        sim = sims[v]
        rating = mat[v, item_index]

        # Ignoramos usuarios con similitud negativa o sin valoración en ese ítem
        if sim > 0 and not np.isnan(rating):
            numerador += sim * rating
            denominador += sim

    # Si nadie tiene valoración válida, devolvemos NaN
    if denominador == 0:
        return np.nan

    # Predicción final
    return numerador / denominador

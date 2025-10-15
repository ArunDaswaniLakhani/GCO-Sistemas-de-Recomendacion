import numpy as np
from pearson import pearson_correlation

def cosine_similarity(matrix):
    mat = np.array(matrix, dtype=np.float64)
    mat = np.nan_to_num(mat - np.nanmean(mat, axis=1, keepdims=True))
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    return np.dot(mat / (norms + 1e-8), (mat / (norms + 1e-8)).T)

def euclidean_similarity(matrix):
    mat = np.array(matrix, dtype=np.float64)
    n = len(mat)
    sim = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            diff = mat[i] - mat[j]
            diff = diff[~np.isnan(diff)]
            dist = np.sqrt(np.nansum(diff ** 2))
            sim[i][j] = 1 / (1 + dist)
    return sim

def pearson_similarity(matrix):
    n = len(matrix)
    sim = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            sim[i][j] = pearson_correlation(matrix[i], matrix[j])
    return sim

import numpy as np

def predict_simple(matrix, similarity, user, item, k):
    sims = similarity[user]
    valid_users = [(i, sims[i]) for i in range(len(matrix)) if i != user and not np.isnan(matrix[i][item]) and sims[i] > 0]
    valid_users.sort(key=lambda x: x[1], reverse=True)
    vecinos = valid_users[:k]

    num = sum(sim * matrix[i][item] for i, sim in vecinos)
    den = sum(sim for _, sim in vecinos)
    return np.nan if den == 0 else num / den

def predict_with_mean(matrix, similarity, user, item, k):
    user_mean = np.nanmean(matrix[user])
    sims = similarity[user]
    valid_users = [(i, sims[i]) for i in range(len(matrix)) if i != user and not np.isnan(matrix[i][item]) and sims[i] > 0]
    valid_users.sort(key=lambda x: x[1], reverse=True)
    vecinos = valid_users[:k]

    num = sum(sim * (matrix[i][item] - np.nanmean(matrix[i])) for i, sim in vecinos)
    den = sum(sim for _, sim in vecinos)
    return np.nan if den == 0 else user_mean + num / den

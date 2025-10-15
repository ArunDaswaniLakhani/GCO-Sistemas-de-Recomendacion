from math import sqrt, isnan

def pearson_correlation(x, y):
    filtered_x, filtered_y = [], []
    for i in range(len(x)):
        if not isnan(x[i]) and not isnan(y[i]):
            filtered_x.append(x[i])
            filtered_y.append(y[i])

    if len(filtered_x) < 2:
        return 0.0

    mean_x = sum(filtered_x) / len(filtered_x)
    mean_y = sum(filtered_y) / len(filtered_y)

    num = sum((filtered_x[i] - mean_x) * (filtered_y[i] - mean_y) for i in range(len(filtered_x)))
    den_x = sqrt(sum((filtered_x[i] - mean_x) ** 2 for i in range(len(filtered_x))))
    den_y = sqrt(sum((filtered_y[i] - mean_y) ** 2 for i in range(len(filtered_y))))

    if den_x == 0 or den_y == 0:
        return 0.0
    return num / (den_x * den_y)

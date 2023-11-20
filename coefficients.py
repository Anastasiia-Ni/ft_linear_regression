def mean(data):
    return sum(data) / len(data)

def std_deviation(data, mean_value):
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    return variance ** 0.5

def covariance(data1, data2, mean1, mean2):
    return sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / len(data1)

def correlation_coefficient(data1, data2):
    mean1 = mean(data1)
    mean2 = mean(data2)
    std_dev1 = std_deviation(data1, mean1)
    std_dev2 = std_deviation(data2, mean2)
    cov = covariance(data1, data2, mean1, mean2)

    coefficient = cov / (std_dev1 * std_dev2)
    return coefficient

def correlation_coefficient_test(data_csv):
    mileage = data_csv['km']
    prices = data_csv['price']
    pirson_coefficient = correlation_coefficient(mileage, prices)

    print(f"Pearson Correlation Coefficient: \033[1m{pirson_coefficient:.2f}\033[0m")
import math

# Нормализация данных
def normalize_data(data):
    normalized_data = (data - data.min()) / (data.max() - data.min())
    return normalized_data

#TODO 4 Реализация функции обучения (тренировки) модели
# Разбор формулы для обновления параметров theta0 и theta1 (tmpθ0 и tmpθ1).
# Создание функции, которая принимает данные и обучает модель с использованием градиентного спуска.
# Использование цикла для обновления theta0 и theta1 итеративно до сходимости модели.

def train_model(data_csv, learning_rate, num_iterations, theta0, theta1):

    # print(f'Thetas: theta1 = {theta1:.2f}, theta0 = {theta0:.2f}')
    
    normalized_data = data_csv.apply(normalize_data)
    mileage = normalized_data['km']
    prices = normalized_data['price']

    m = len(mileage) # Количество примеров в данных

    # время подбора мин эсктремума
    for _ in range(num_iterations):
        grad_theta0 = 0
        grad_theta1 = 0

        for i in range(m):
            prediction = (theta0 + theta1 * mileage[i] - prices[i])

            grad_theta0 += prediction
            grad_theta1 += prediction * mileage[i]

        grad_theta0 /= m
        grad_theta1 /= m

        # Проверка деления на переполнение и NaN
        if not math.isnan(grad_theta1) and not math.isinf(grad_theta1):
            theta1 -= learning_rate * grad_theta1

        if not math.isnan(grad_theta0) and not math.isinf(grad_theta0):
            theta0 -= learning_rate * grad_theta0
        
    
    print(f'Regression Line: y = {theta1:.2f}x + {theta0:.2f}')
    return theta0, theta1
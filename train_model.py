
# Нормализация данных
def normalize_data(data):
    try:
        normalized_data = (data - data.min()) / (data.max() - data.min())
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    return normalized_data

#TODO 4 Реализация функции обучения (тренировки) модели
# Разбор формулы для обновления параметров theta0 и theta1 (tmpθ0 и tmpθ1).
# Создание функции, которая принимает данные и обучает модель с использованием градиентного спуска.
# Использование цикла для обновления theta0 и theta1 итеративно до сходимости модели.

def train_model(data_csv, learning_rate, num_iterations, theta0, theta1):
    
    normalized_data = data_csv.apply(normalize_data)
    mileage = normalized_data['km']
    prices = normalized_data['price']

    m = len(mileage)

    theta0, theta1 = 0, 0
    # время подбора мин эсктремума
    for _ in range(num_iterations):
        grad_theta0 = 0
        grad_theta1 = 0

        for i in range(m):
            prediction = (theta0 + theta1 * mileage[i] - prices[i])
            grad_theta0 += prediction
            grad_theta1 += prediction * mileage[i]

        grad_theta0 = learning_rate * (1 / m) * grad_theta0
        grad_theta1 = learning_rate * (1 / m) * grad_theta1
        theta0 -= grad_theta0
        theta1 -= grad_theta1
        
    print(f'Regression Line: y = {theta1:.2f}x + {theta0:.2f}')
    return theta0, theta1

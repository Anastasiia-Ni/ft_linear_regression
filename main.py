import pandas as pnd
import matplotlib.pyplot as plt
from correlation_coefficient import correlation_coefficient
import math
import sys

theta0 = 0
theta1 = 0

#TODO 1 Изучение линейной регрессии и гипотезы
# Что такое линейная регрессия и как она работает?
# Понимание гипотезы для прогнозирования цены машины по пробегу
# (estimatePrice(mileage) = θ0 + (θ1 * mileage)).

def correlation_coefficient_test(data_csv) -> bool:
    mileage = [data_row['km'] for (index, data_row) in data_csv.iterrows()]
    prices = [data_row['price'] for (index, data_row) in data_csv.iterrows()]
    pirson_coefficient = correlation_coefficient(mileage, prices)

    print("Коэффициент корреляции Пирсона:", pirson_coefficient)
    return True


#TODO 2 Загрузка данных
# Подготовка и предобработка данных для обучения модели.

def load_data(path):
    data_csv = pnd.read_csv(path) #to_scv -- writer
    # print(data_csv)
    return data_csv


#TODO 3 Визуализация данных
# Изучение библиотеки matplotlib.pyplot для построения графиков.
# Нанесение точек данных на график для визуализации распределения пробега и цен на машины.

def build_graph(data_csv):
    mileage = [data_row['km'] for (index, data_row) in data_csv.iterrows()]
    prices = [data_row['price'] for (index, data_row) in data_csv.iterrows()]

    plt.plot(mileage, prices, 'ob')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Distribution of car prices relative to mileage')
    plt.rcParams.update({'font.size': 14})

    # if theta0 != 0 and theta1 != 0:
    #     x = np.linspace(0, 1, 100)
    #     f = 0.25 - (x - 0.5)**2
    #     plt.plot(x, f, '--r')
    #     plt.plot(x, f, '--r', label=f'f(x) = {theta1} * x + {theta0}')
    #     plt.legend(fontsize=12)


    plt.show()

#TODO 4 Реализация функции обучения (тренировки) модели
# Разбор формулы для обновления параметров theta0 и theta1 (tmpθ0 и tmpθ1).
# Создание функции, которая принимает данные и обучает модель с использованием градиентного спуска.
# Использование цикла для обновления theta0 и theta1 итеративно до сходимости модели.

#TODO 5 Реализация функции прогнозирования
# Создание функции, которая принимает пробег и возвращает предполагаемую цену машины,
# используя гипотезу (estimatePrice(mileage) = θ0 + (θ1 * mileage)) и
# последние значения theta0 и theta1.
def cost_forecast(milage) -> int:
    return (theta1 * milage + theta0)

#TODO 6 Вычисление точности алгоритма (бонусная часть)
# Разработка функции для вычисления точности модели.
# Сравнение предсказанных значений с реальными значениями и
# вычисление средней абсолютной ошибки или других метрик для оценки точности модели.


#TODO 7 Визуализация результатов (бонусная часть)
# Построение графика данных и линии регрессии, полученной после обучения модели.
# Добавление легенды и названий осей для лучшей визуализации.

def main():
    data = load_data("data.csv")
    correlation_coefficient_test(data)
    build_graph(data)


# if __name__ == "__main__":
main()
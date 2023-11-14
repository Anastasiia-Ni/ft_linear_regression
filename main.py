import pandas as pd
import matplotlib.pyplot as plt
from correlation_coefficient import correlation_coefficient
import plotly.express as px
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
    data_csv = pd.read_csv(path) #to_scv -- writer
    # print(data_csv.head())
    return data_csv


#TODO 3 Визуализация данных
# Изучение библиотеки matplotlib.pyplot для построения графиков.
# Нанесение точек данных на график для визуализации распределения пробега и цен на машины.

def build_graph(data_csv):
    mileage = [data_row['km'] for (index, data_row) in data_csv.iterrows()]
    prices = [data_row['price'] for (index, data_row) in data_csv.iterrows()]

    # Создаем DataFrame из данных
    data = {'Mileage': mileage, 'Price': prices}
    df = pd.DataFrame(data)

    # Строим точечный график
    fig = px.scatter(df, x='Mileage', y='Price', title='Distribution of car prices relative to mileage')

    # Настройка стиля графика
    fig.update_traces(marker=dict(color='blue', size=8))

    # Строим линейную регрессию, если theta0 и theta1 не равны 0
    if theta0 != 0 and theta1 != 0:
        x_range = range(int(min(mileage)), int(max(mileage)) + 1)
        y_range = theta1 * x_range + theta0
        fig.add_trace(px.line(x=x_range, y=y_range, mode='lines', line=dict(color='red', dash='dash'), name=f'f(x) = {theta1} * x + {theta0}').data[0])

    # Настройка осей и шрифта
    fig.update_xaxes(title_text='Mileage')
    fig.update_yaxes(title_text='Price')
    fig.update_layout(font=dict(size=14))

    # Настройка размера графика
    fig.update_layout(height=500, width=700)

    # где то тут добавить легенду

    # Показываем график
    fig.show()

    # то же самое в матлолибе
    # plt.plot(mileage, prices, 'ob')
    # plt.xlabel('Mileage')
    # plt.ylabel('Price')
    # plt.title('Distribution of car prices relative to mileage')
    # plt.rcParams.update({'font.size': 14})

    # if theta0 != 0 and theta1 != 0:
    #     x = range(int(min(mileage)), int(max(mileage)) + 1)
    #     f = [theta1 * xi + theta0 for xi in x]
    #     plt.plot(x, f, '--r')
    #     plt.plot(x, f, '--r', label=f'f(x) = {theta1} * x + {theta0}')
    #     plt.legend(fontsize=12)


    # plt.show()


def train_model(data_csv, learning_rate, num_iterations):
    mileage = [data_row['km'] for (index, data_row) in data_csv.iterrows()]
    prices = [data_row['price'] for (index, data_row) in data_csv.iterrows()]

    m = len(mileage) # Количество примеров в данных

    for _ in range(num_iterations):
        return theta0, theta1

#TODO 4 Реализация функции обучения (тренировки) модели
# Разбор формулы для обновления параметров theta0 и theta1 (tmpθ0 и tmpθ1).
# Создание функции, которая принимает данные и обучает модель с использованием градиентного спуска.
# Использование цикла для обновления theta0 и theta1 итеративно до сходимости модели.

# def train_func():
#     pass

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

    train_model(data, 0.01, 42)



# if __name__ == "__main__":
main()
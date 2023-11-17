import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import sys
import os
from correlation_coefficient import correlation_coefficient
from prediction import cost_forecast
from train_model import train_model


#TODO 1 Изучение линейной регрессии и гипотезы
# Что такое линейная регрессия и как она работает?
# Понимание гипотезы для прогнозирования цены машины по пробегу
# (estimatePrice(mileage) = θ0 + (θ1 * mileage)).

def correlation_coefficient_test(data_csv) -> bool:
    mileage = data_csv['km']
    prices = data_csv['price']
    pirson_coefficient = correlation_coefficient(mileage, prices)

    print("Pearson Correlation Coefficient: ", pirson_coefficient)
    return True


#TODO 2 Загрузка данных
# Подготовка и предобработка данных для обучения модели.

def load_data(path):

    if not os.path.exists(path):
        print(f"The file {path} does not exist.")
        return None
    
    try:
        data_csv = pd.read_csv(path)  # o_scv -- writer
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None
    
    if data_csv.isnull().any().any():
        print("Missing values detected in the data.")
        return None
    if (data_csv == 0).any().any():
        print("Zero values detected in the data.")
        return None

    return data_csv


#TODO 3 Визуализация данных
# Изучение библиотеки matplotlib.pyplot для построения графиков.
# Нанесение точек данных на график для визуализации распределения пробега и цен на машины.

def build_graph(data_csv, theta0, theta1):
    mileage = data_csv['km']
    prices = data_csv['price']

    # # Создаем DataFrame из данных
    # data = {'Mileage': mileage, 'Price': prices}
    # df = pd.DataFrame(data)

    # # Строим точечный график
    # fig = px.scatter(df, x='Mileage', y='Price', title='Distribution of car prices relative to mileage')

    # # Настройка стиля графика
    # fig.update_traces(marker=dict(color='blue', size=8))

    # # Строим линейную регрессию, если theta0 и theta1 не равны 0
    # if theta0 != 0 and theta1 != 0:
    #     print(f"theta0= {theta0}, theta1= {theta1}")
    #     x_range = range(int(min(mileage)), int(max(mileage)) + 1)
    #     y_range = theta1 * x_range + theta0
    #     fig.add_trace(px.line(x=x_range, y=y_range, mode='lines', line=dict(color='red', dash='dash'), name=f'f(x) = {theta1} * x + {theta0}').data[0])

    # # Настройка осей и шрифта
    # fig.update_xaxes(title_text='Mileage')
    # fig.update_yaxes(title_text='Price')
    # fig.update_layout(font=dict(size=14))

    # # Настройка размера графика
    # fig.update_layout(height=500, width=700)

    # # где то тут добавить легенду

    # # Показываем график
    # fig.show()

    # то же самое в матлолибе
    plt.plot(mileage, prices, 'ob')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Distribution of car prices relative to mileage')
    plt.rcParams.update({'font.size': 14})

    if theta0 != 0 and theta1 != 0:
        print(f"theta0= {theta0}, theta1= {theta1}")
        regression_line = theta0 + theta1 * mileage
        plt.plot(mileage, regression_line, '-r', label='Regression Line')
        # Добавление формулы в легенду
        formula_text = f'Regression Line: y = {theta1:.2f}x + {theta0:.2f}'
        plt.text(mileage.min(), regression_line.min(), formula_text, fontsize=12, color='r')


    plt.show()


#TODO 6 Вычисление точности алгоритма (бонусная часть)
# Разработка функции для вычисления точности модели.
# Сравнение предсказанных значений с реальными значениями и
# вычисление средней абсолютной ошибки или других метрик для оценки точности модели.
# for i in range(len): srednii_kv_otklon += (theta1 * x[i] + thetha0 - y[i]) ** 2
#  oshibka = srednii_kv_otklon/len


def main():
    try:
        data = load_data("data.csv")
        if data is None:
            return
        theta0, theta1 = 0, 0

        while True:
            command = input("Enter a command: ")
            if command == 't':
                correlation_coefficient_test(data)
                build_graph(data, theta0, theta1)
                theta0, theta1 = train_model(data, 0.5, 300, theta0, theta1)
            elif command == 'e':
                cost_forecast(theta0, theta1)
            elif command == 'g':
                build_graph(data, theta0, theta1)
            elif command == 'exit':
                sys.exit(0)
            else:
                print(f"Unknown command: '{command}'")


    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        sys.exit()
    except ZeroDivisionError:
        print("ZeroDivisionError: Please check the data in *.csv file.")
    except TypeError as e:
        print (f"TypeError: {e}")
    except ValueError as e:
        print (f"ValueError: {e}")

if __name__ == "__main__":
    main()

# добавить проверку на исключения
# норминет
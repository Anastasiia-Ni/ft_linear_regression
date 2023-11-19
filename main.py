import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import signal
from correlation_coefficient import correlation_coefficient
from prediction import cost_forecast
from train_model import train_model
from precision import calculate_precision


#TODO 1 Изучение линейной регрессии и гипотезы
# Что такое линейная регрессия и как она работает?
# Понимание гипотезы для прогнозирования цены машины по пробегу
# (estimatePrice(mileage) = θ0 + (θ1 * mileage)).

def correlation_coefficient_test(data_csv) -> bool:
    mileage = data_csv['km']
    prices = data_csv['price']
    pirson_coefficient = correlation_coefficient(mileage, prices)

    print(f"Pearson Correlation Coefficient: \033[1m{pirson_coefficient}\033[0m")
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

def build_graph(data_csv, theta0, theta1, est_mil, est_price):

    mileage = data_csv['km']
    prices = data_csv['price']

    plt.scatter(mileage, prices, color='xkcd:blue', marker='o', zorder=3, label="Training data")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', zorder=1)
    plt.xlabel('Mileage, km')
    plt.ylabel('Price, $')
    plt.title('Distribution of car prices relative to mileage')
    plt.rcParams.update({'font.size': 10})

    min_x = min(mileage)
    max_x = max(mileage)
    min_y = min(prices)
    max_y = max(prices)
    axic_x = [min_x, max_x]
    axic_y = []

    for point in axic_x:
        normalized_x = (point - min_x) / (max_x - min_x) if (max_x - min_x) != 0 else 0
        point = theta1 * normalized_x + theta0
        denormalized_y = point * (max_y - min_y) + min_y if point else 0
        axic_y.append(denormalized_y)

    if est_price:
        # Extend the x-axis range
        extended_min_x = min(min_x, est_mil)
        extended_max_x = max(max_x, est_mil)

        axic_x = [extended_min_x, extended_max_x]
        axic_y = []
        for point in axic_x:
            normalized_x = (point - min_x) / (max_x - min_x) if (max_x - min_x) != 0 else 0
            point_on_line = theta1 * normalized_x + theta0
            denormalized_y = point_on_line * (max_y - min_y) + min_y if point else 0
            axic_y.append(denormalized_y)

        plt.scatter([est_mil], [est_price], color='tab:red', marker='o', label='Car for sale', zorder=3)
        plt.legend()

    if theta0 and theta1:
        formula_text = f'Regression Line: \ny = {theta1:.2f}x + {theta0:.2f}'
        plt.plot(axic_x, axic_y, 'tab:orange', label=formula_text, zorder=2)
        plt.legend()

    plt.show()


def handle_ctrl_c(sig, frame):
    print("\nCtrl+C pressed. Exiting.")
    sys.exit(0)

def handle_ctrl_z(sig, frame):
    print("\nCtrl+Z pressed. Exiting.")
    sys.exit(0)

def main():
    try:
        data = load_data("data.csv")
        if data is None:
            return
        theta0, theta1 = 0, 0

        while True:
            signal.signal(signal.SIGINT, handle_ctrl_c)
            signal.signal(signal.SIGTSTP, handle_ctrl_z)
            command = input("Enter a command: ")
            if command == 't':
                correlation_coefficient_test(data)
                theta0, theta1 = train_model(data, 0.5, 300, theta0, theta1)
                build_graph(data, theta0, theta1, 0, 0)
            elif command == 'e':
                est_mil, est_for = cost_forecast(data, theta0, theta1)
                if est_for:
                    build_graph(data, theta0, theta1, est_mil, est_for)
            elif command == 'g':
                build_graph(data, theta0, theta1, 0, 0)
            elif command == 'p':
                calculate_precision(data, theta0, theta1)
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
    except EOFError:
        print("\nCtrl+D pressed. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()

# добавить проверку на исключения
# норминет
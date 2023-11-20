from coefficients import correlation_coefficient_test
from utils import load_data, save_theta_values, handle_ctrl_c, handle_ctrl_z
from build_graph import build_graph
from colorama import Fore, Style, init
import sys
import signal


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
    print(f'Regression Line: \033[1my = {theta1:.2f}x + {theta0:.2f}\033[0m')
    return theta0, theta1


def input_rate_iterations():
    learning_rate = 0.00
    num_iterations = 0
    while not learning_rate:
        signal.signal(signal.SIGINT, handle_ctrl_c)
        signal.signal(signal.SIGTSTP, handle_ctrl_z)
        rate_inp = input("Enter learning rate for the training (between 0 and 1): ")
        if rate_inp.strip():
            if rate_inp.replace('.', '').isdigit() or (rate_inp[0] == '-' and rate_inp[1:].replace('.', '').isdigit()):
                learning_rate = float(rate_inp)
                if 0 <= learning_rate <= 1:
                    print(f"Learning rate: {learning_rate}")
                else:
                    learning_rate = 0
                    print("Error: Please enter a number between 0 and 1.")
            else:
                print("Error: Please enter a valid number.")
        else:
            print("Error: Please enter a non-empty value.")
    
    while not num_iterations:
        signal.signal(signal.SIGINT, handle_ctrl_c)
        signal.signal(signal.SIGTSTP, handle_ctrl_z)
        it_inp = input("Enter iterations number rate for the training: ")
        if it_inp.strip():
            if it_inp.isdigit():
                num_iterations = int(it_inp)
                print(f"{Fore.GREEN}Iterations number: {num_iterations:.0f}{Style.RESET_ALL}")
            else:
                print(f"\033[31mError: Please enter a valid integer.\033[0m")
        else:
            print(f"\033[31mError: Please enter a non-empty value.\033[0m")

    return learning_rate, num_iterations


def main():
    try:
        data = load_data("data.csv")
        if data is None:
            return
        theta0, theta1 = 0, 0
        correlation_coefficient_test(data)
        lng_rate, num_itrs = input_rate_iterations()
        theta0, theta1 = train_model(data, lng_rate, num_itrs, theta0, theta1)
        build_graph(data, theta0, theta1, 0, 0)
        save_theta_values(theta0, theta1, 'theta_values.csv')
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
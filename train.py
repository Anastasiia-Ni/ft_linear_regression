from coefficients import correlation_coefficient_test
from utils import load_data, save_theta_values, handle_ctrl_c, handle_ctrl_z
from build_graph import build_graph
import sys
import signal
import time


def normalize_data(data):
    try:
        normalized_data = (data - data.min()) / (data.max() - data.min())
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    return normalized_data


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

    print("Model calculation...")
    time.sleep(1)

    print(f"\033[33m{43 * '-'}\033[0m")
    print(f"\033[33mRegression Line: \033[1my = {theta1:.2f}x + {theta0:.2f}\033[0m")
    print(f"\033[33m{43 * '-'}\033[0m\n")
    return theta0, theta1


def input_rate_iterations():
    learning_rate = 0.00
    num_iterations = 0
    while not learning_rate:
        signal.signal(signal.SIGINT, handle_ctrl_c)
        signal.signal(signal.SIGTSTP, handle_ctrl_z)
        rate_inp = input("\033[32mEnter learning rate for the training (between 0 and 1): \033[0m")
        if rate_inp.strip():
            if (rate_inp.strip() and
                (
                    rate_inp.replace('.', '', 1).replace('-', '', 1).isdigit() or 
                    (rate_inp[0] == '-' and 
                    rate_inp[1:].replace('.', '').isdigit()))
                ):
                learning_rate = float(rate_inp)
                if 0 < learning_rate < 1:
                    print()
                else:
                    learning_rate = 0
                    print("\033[31mError:\033[0m Please enter a number between 0 and 1 (not including).")
            else:
                print("\033[31mError:\033[0m Please enter a valid number.")
        else:
            print("\033[31mError:\033[0m Please enter a non-empty value.")
    
    while not num_iterations:
        signal.signal(signal.SIGINT, handle_ctrl_c)
        signal.signal(signal.SIGTSTP, handle_ctrl_z)
        it_inp = input("\033[32mEnter iterations number rate for the training: \033[0m")
        if it_inp.strip():
            if it_inp.isdigit() and int(it_inp) > 0:
                num_iterations = int(it_inp)
                print()
            else:
                print(f"\033[31mError:\033[0m Please enter a valid integer.")
        else:
            print(f"\033[31mError:\033[0m Please enter a non-empty value.")

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
    except KeyError as e:
        print (f"KeyError: {e}")
    except EOFError:
        print("\nCtrl+D pressed. Exiting.")
        sys.exit(0)

    

if __name__ == "__main__":
    main()
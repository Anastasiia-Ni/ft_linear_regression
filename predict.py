from utils import load_data, handle_ctrl_c, handle_ctrl_z
from build_graph import build_graph
import sys
import signal
import os
#TODO 5 Реализация функции прогнозирования
# Создание функции, которая принимает пробег и возвращает предполагаемую цену машины,
# используя гипотезу (estimatePrice(mileage) = θ0 + (θ1 * mileage)) и
# последние значения theta0 и theta1.
def cost_forecast(data, theta0, theta1):

    if not theta0 and not theta1:
        print ("First you need to \033[1mtrain\033[0m the model.")
        return 0
    mil_forecast = -1

    while mil_forecast < 0:
        signal.signal(signal.SIGINT, handle_ctrl_c)
        signal.signal(signal.SIGTSTP, handle_ctrl_z)
        milage_str = input("Write the mileage (in km) to predict the price: ") # добавить проверк, мб это все в отдельную функцию
        if milage_str.strip():
            if milage_str.isdigit():
                mil_forecast = int(milage_str) # while loop
            else:
                print(f"\033[31mError: Please enter a valid integer.\033[0m")
        else:
            print(f"\033[31mError: Please enter a non-empty value.\033[0m")
    
    # data = data.apply(normalize_data)
    mileage = data['km']
    prices = data['price']

    min_mil = min(mileage)
    max_mil = max(mileage)
    min_price = min(prices)
    max_price = max(prices)

    normalized_mileage = (mil_forecast - min_mil) / (max_mil - min_mil)
    normalized_price =  theta1 * normalized_mileage + theta0
    
    price_forecast = normalized_price * (max_price - min_price) + min_price if normalized_price > 0 else 0
    
    if price_forecast > 0:
        print(f"The estimated price of this car is: \033[1m{price_forecast:.2f}\033[0m.")
    else:
        price_forecast = 0
        print("The car cannot be sold.")

    return mil_forecast, price_forecast


def main():
    try:
        data = load_data("data.csv")
        if not os.path.exists('theta_values.csv'):
            print("First you need to \033[1mtrain\033[0m the model.")
        theta_data = load_data('theta_values.csv')
        if data is None:
            return
        theta0 = float(theta_data['theta0'].values[0])
        theta1 = float(theta_data['theta1'].values[0])
        est_mil, est_for = cost_forecast(data, theta0, theta1)
        if est_for:
            build_graph(data, theta0, theta1, est_mil, est_for)
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
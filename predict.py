from utils import load_data, handle_ctrl_c, handle_ctrl_z
from build_graph import build_graph
import sys
import signal
import os


def cost_forecast(data, theta0, theta1):

    if not theta0 and not theta1:
        print ("\033[36mFirst you need to \033[1mtrain\033[0m \033[36mthe model.033[0m")
        return 0
    mil_forecast = -1

    while mil_forecast < 0:
        signal.signal(signal.SIGINT, handle_ctrl_c)
        signal.signal(signal.SIGTSTP, handle_ctrl_z)
        milage_str = input("\033[32mWrite the mileage (in km) to predict the price: \033[0m")
        if milage_str.strip():
            if milage_str.isdigit():
                mil_forecast = int(milage_str)
            else:
                print(f"\033[31mError:\033[0m Please enter a valid integer.")
        else:
            print(f"\033[31mError:\033[0m Please enter a non-empty value.")
    
    mileage = data['km']
    prices = data['price']

    min_mil = min(mileage)
    max_mil = max(mileage)
    min_price = min(prices)
    max_price = max(prices)

    normalized_mileage = (mil_forecast - min_mil) / (max_mil - min_mil)
    normalized_price =  theta1 * normalized_mileage + theta0
    
    price_forecast = normalized_price * (max_price - min_price) + min_price if normalized_price > 0 else 0
    
    print(f"\033[33m{43 * '-'}\033[0m")
    if price_forecast > 0:
        print(f"\033[33mThe estimated price of the car is: \033[1m{price_forecast:.2f}\033[0m")
    else:
        price_forecast = 0
        print("\033[33mThe car cannot be sold.\033[0m")
    print(f"\033[33m{43 * '-'}\033[0m\n")

    return mil_forecast, price_forecast


def main():
    try:
        data = load_data("data.csv")
        if not os.path.exists('theta_values.csv'):
            print("\033[36mFirst you need to \033[1mtrain\033[0m \033[36mthe model.\033[0m")
            return
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
    except KeyError as e:
        print (f"KeyError: {e}")
    except EOFError:
        print("\nCtrl+D pressed. Exiting.")
        sys.exit(0)


if __name__ == "__main__":
    main()
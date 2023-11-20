import os
import sys
from utils import load_data

def create_predicted_prices(mileage, prices, theta0, theta1):
    min_mil = min(mileage)
    max_mil = max(mileage)
    min_price = min(prices)
    max_price = max(prices)

    predicted_prices = []
    for km in mileage:
        normalized_mileage = (km - min_mil) / (max_mil - min_mil)
        normalized_price =  theta1 * normalized_mileage + theta0
        price_forecast = normalized_price * (max_price - min_price) + min_price
        predicted_prices.append(price_forecast)
    return predicted_prices


def calculate_precision(data_csv, theta0, theta1):

    if not theta0 and not theta1:
        print ("\033[36mFirst you need to \033[1mtrain\033[0m \033[36mthe model.\033[0m")
        return 0
    mileage = data_csv['km']
    prices = data_csv['price']

    predicted_prices = create_predicted_prices(mileage, prices, theta0, theta1)

    mean_actual = sum(prices) / len(prices)
    total_variance = sum((actual - mean_actual) ** 2 for actual in prices)
    residual_variance = sum((actual - predicted) ** 2 for actual, predicted in zip(prices, predicted_prices))
    if not total_variance:
        print ("Calculation of the coefficient of determination is not possible.")
        return 0
    precision = 1 - (residual_variance / total_variance)

    mae = sum(abs(actual - predicted) for actual, predicted in zip(prices, predicted_prices)) / len(prices)

    print(f"\033[33m{43 * '-'}\033[0m")
    print(f"\033[33mMean Absolute Error: \033[1m{mae:.2f}\033[0m")
    print(f"\033[33m{43 * '-'}\033[0m\n")

    print(f"\033[33m{43 * '-'}\033[0m")
    print(f"\033[33mPrecision (R^2): \033[1m{precision:.4f}\033[0m") # Чем ближе к 1, тем лучше.
    print(f"\033[33m{43 * '-'}\033[0m\n")

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
        calculate_precision(data, theta0, theta1)
    except AssertionError as e:
        print(f"AssertionError: {e}")
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
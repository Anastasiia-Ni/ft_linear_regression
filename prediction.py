#TODO 5 Реализация функции прогнозирования
# Создание функции, которая принимает пробег и возвращает предполагаемую цену машины,
# используя гипотезу (estimatePrice(mileage) = θ0 + (θ1 * mileage)) и
# последние значения theta0 и theta1.
def cost_forecast(theta0, theta1) -> int:
    milage_str = input("Write the mileage (in km) to predict the price: ") # добавить проверк, мб это все в отдельную функцию

    # try:
    milage = int(milage_str)

    price = theta1 * milage + theta0
    print(f"The estimated price of this car is: \033[1m{price}\033[0m")

    return price

# build_graph c точкой по этой цене
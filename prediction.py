from train_model import normalize_data

#TODO 5 Реализация функции прогнозирования
# Создание функции, которая принимает пробег и возвращает предполагаемую цену машины,
# используя гипотезу (estimatePrice(mileage) = θ0 + (θ1 * mileage)) и
# последние значения theta0 и theta1.
def cost_forecast(data, theta0, theta1) -> int:

    if not theta0 and not theta1:
        print ("First you need to \033[1mtrain\033[0m the model.")
        return 0

    # try:
    milage_str = input("Write the mileage (in km) to predict the price: ") # добавить проверк, мб это все в отдельную функцию
    mil_forecast = int(milage_str) # while loop
    
    # normalized_data = data.apply(normalize_data)
    mileage = data['km']
    prices = data['price']

    min_mil = min(mileage)
    max_mil = max(mileage)
    min_price = min(prices)
    max_price = max(prices)

    normalized_mileage = (mil_forecast - min_mil) / (max_mil - min_mil)
    normalized_price =  theta1 * normalized_mileage + theta0

    price_forecast = normalized_price * (max_price - min_price) + min_price #if normalized_price > 0 else 0
    
    if price_forecast > 0:
        print(f"The estimated price of this car is: \033[1m{price_forecast:.2f}\033[0m.")
    else:
        price_forecast = 0
        print("The car cannot be sold.")

    return mil_forecast, price_forecast

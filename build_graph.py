import matplotlib.pyplot as plt

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
        est_mil = 1 if est_mil == 0 else est_mil 
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
# ft_linear_regression
## About the project
This machine learning project implements the basic concept of linear regression to predict car prices based on their mileage. 
The project consists of two main programs: `train.py` and `predict.py`. 
The training program utilizes gradient descent to find the optimal parameters for the linear function, while the estimation program uses these parameters to predict the price of a car given its mileage.

## Introduction
### Linear Regression:
Linear regression is a fundamental concept in machine learning and statistics used to model the relationship between a dependent variable and one or more independent variables. 
In simple linear regression, there is only one independent variable, and the relationship is represented by a straight line. 
The equation of a simple linear regression model is given by:

![Linear Regression Equation](https://latex.codecogs.com/svg.latex?y%20=%20\theta_0%20+%20\theta_1%20\cdot%20x).

Where:
- ![ y ](https://latex.codecogs.com/svg.latex?y) is the dependent variable (car price in this project).
- ![ x ](https://latex.codecogs.com/svg.latex?x) is the independent variable (car mileage).
- ![ \theta_0 ](https://latex.codecogs.com/svg.latex?\theta_0) is the intercept (displacement coefficient).
- ![ \theta_1 ](https://latex.codecogs.com/svg.latex?\theta_1) is the slope (slope factor).


  
  <img src="https://github.com/Anastasiia-Ni/ft_linear_regression/blob/main/assets/Graph_LR.png" width="500">
  

  The goal of regression is to find the coefficients of this linear combination, thereby determining the regression function.

### Pearson Correlation Coefficient:
The Pearson correlation coefficient, often denoted as r, measures the linear relationship between two variables. It takes values between -1 and 1, where:
- r = 1 indicates a perfect positive linear relationship.
- r = −1 indicates a perfect negative linear relationship.
- r = 0 indicates no linear relationship.

In the context of this project, the Pearson correlation coefficient is used to assess the correlation between car mileage and prices, 
providing insights into the strength and direction of the linear relationship. 
A coefficient close to 1 or -1 suggests a strong linear relationship, making it a valuable indicator for the quality of the linear regression model. 
The closer r is to 1 or -1, the better the linear regression captures the underlying patterns in the data. in the direction that reduces the cost.

### Method of least squares
The method of least squares aims to find parameters in such a way that the predicted values are as close as possible to the actual values. 
Graphically, this is expressed as follows:

<img src="https://github.com/Anastasiia-Ni/ft_linear_regression/blob/main/assets/Least_squares.jpg" width="500">

In the graphical representation, this corresponds to finding the line that minimizes the sum of the squared distances between each data point and the corresponding point on the line.


The method minimizes the sum of the squared differences between the observed and predicted values. The equation for the line (or curve) that best fits the data is determined by minimizing the sum of the squared vertical distances (residuals) from each data point to the line.

For linear regression, the objective function to minimize is often expressed as:

![Math Formula](https://latex.codecogs.com/svg.latex?%5Ctext%7BMinimize%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28Y_i%20-%20%28mx_i%20%2B%20b%29%29%5E2)

where: <img src="https://latex.codecogs.com/svg.latex?Y_i" /> represents the observed values, 
<img src="https://latex.codecogs.com/svg.latex?mx_i+b" /> represents the predicted values from the linear model, and the sum is taken over all data points. 

The parameters <img src="https://latex.codecogs.com/svg.latex?m" /> and <img src="https://latex.codecogs.com/svg.latex?b" /> are adjusted to minimize this sum, providing the best-fitting line through the data.


The method of least squares plays a crucial role in regression analysis. It is used to find the line that best represents the relationship between the independent variable (input) and the dependent variable (output). By minimizing the sum of squared differences, the method identifies the parameters that yield the most accurate predictions.


The method of least squares assumes a linear relationship between the input and output variables. While this assumption simplifies the model, it might not capture complex relationships in the data. It's essential to consider the linearity assumption and explore more advanced models for nonlinear relationships.



### Gradient Descent:

Gradient descent is an optimization algorithm used to find the minimum of a function iteratively. 
In the context of machine learning, it is employed to minimize the cost function, 
which measures the difference between the predicted values and the actual values. 
The algorithm adjusts the model parameters (in this case θ₀ and θ₁).

<img src="https://github.com/Anastasiia-Ni/ft_linear_regression/blob/main/assets/Gradient_desc.jpg" width="500">

The update rule for gradient descent in the context of linear regression is as follows:

![Update Rule for Gradient Descent](https://latex.codecogs.com/svg.latex?%5Ctheta_0%20=%20%5Ctheta_0%20-%20%5Calpha%20%5Cfrac{1}{m}%20%5Csum_{i=1}^{m}%20(h_%7B%5Ctheta%7D(x%5E%7B(i)%7D)%20-%20y%5E%7B(i)%7D))


![Update Rule for Gradient Descent](https://latex.codecogs.com/svg.latex?%5Ctheta_1%20=%20%5Ctheta_1%20-%20%5Calpha%20%5Cfrac{1}{m}%20%5Csum_{i=1}^{m}%20((h_%7B%5Ctheta%7D(x%5E%7B(i)%7D)%20-%20y%5E%7B(i)%7D)%20%5Ccdot%20x%5E%7B(i)%7D))

where:
- ![ \alpha ](https://latex.codecogs.com/svg.latex?\alpha) is the learning rate, controlling the step size in each iteration.
- ![ m ](https://latex.codecogs.com/svg.latex?m) is the number of training examples.
- ![ h_{\theta}(x^{(i)}) ](https://latex.codecogs.com/svg.latex?h_{\theta}(x^{(i)})) is the predicted value for the \( i \)-th example.
- ![ y^{(i)} ](https://latex.codecogs.com/svg.latex?y^{(i)}) is the actual value for the \( i \)-th example.
- ![ x^{(i)} ](https://latex.codecogs.com/svg.latex?x^{(i)}) is the input feature for the \( i \)-th example.

This formula represents the simultaneous update of the parameters  ![ \theta_0 ](https://latex.codecogs.com/svg.latex?\theta_0)  and  ![ \theta_1 ](https://latex.codecogs.com/svg.latex?\theta_1)  in the direction that minimizes the cost function.


Here is an simple illustration depicting the concept of gradient descent:

<img src="https://miro.medium.com/v2/resize:fit:1200/format:webp/1*iNPHcCxIvcm7RwkRaMTx1g.jpeg" width="350">



In this visualization, the algorithm iteratively adjusts the parameters to find the minimum of the cost function.

Influence of Step Size and Iterations:

- Learning Rate (α): A higher learning rate may cause the algorithm to converge faster, but if it's too high, it may overshoot the minimum. Conversely, a lower learning rate might converge more slowly but could be more stable. Experiment with different values to find an optimal balance.

- Number of Iterations: The number of iterations determines how many times the algorithm will update the parameters. Too few iterations may result in an incomplete convergence, while too many iterations could lead to overfitting. It's crucial to monitor the convergence of the cost function and select an appropriate number of iterations.


### Precision (bonus part):

**Mean Absolute Error** is a metric used to measure the average absolute differences between predicted and actual values. It is calculated as:

![MAE](https://latex.codecogs.com/svg.latex?\text{MAE}=\frac{1}{m}\sum_{i=1}^{m}|h_{\theta}(x^{(i)})-y^{(i)}|)

Here, ![m](https://latex.codecogs.com/svg.latex?m) is the number of predictions, ![h_{\theta}(x^{(i)})](https://latex.codecogs.com/svg.latex?h_{\theta}(x^{(i)})) is the predicted value, and ![y^{(i)}](https://latex.codecogs.com/svg.latex?y^{(i)}) is the actual value.



**Precision**, often represented by \( R^2 \), measures the proportion of the variance in the dependent variable that is predictable from the independent variable(s). It ranges from 0 to 1, where 1 indicates perfect predictions.

![R^2](https://latex.codecogs.com/svg.latex?R^2=1-\frac{\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})^2}{\sum_{i=1}^{m}(y^{(i)}-\bar{y})^2})

Here, \( \bar{y} \) is the mean of the actual values.

These metrics help assess the accuracy and performance of the model, providing insights into how well it predicts the target variable. A higher \( R^2 \) value and lower MAE indicate better model performance.


Объяснить как считается Mean Absolute Error: и Precision (R^2) и о чем вообще эти коээфициенты
<img src="https://github.com/Anastasiia-Ni/ft_linear_regression/blob/main/assets/Deviation.jpg" width="500">

## Specifications
- Language: Python 3.6.9
- Library: Matplotlib for data visualization
- Data Format: CSV files
- Programs:
  - training.py: Trains the model and stores the parameters in "theta.csv"
  - estimation.py: Estimates the price of a car based on user-input mileage using the trained model
  - accuracy.py: Calculates the coefficient of determination for model accuracy assessment

## Installation
```
$ git clone git@github.com:Anastasiia-Ni/ft_linear_regression
$ cd ft_linear_regression
```
## Requirements
`$ pip install matplotlib pandas`

## Usage
1. Training:
- Run train.py to generate θ0 and θ1 from the data in data.csv.
```
$ python3 train.py
-------------------------------------------
Pearson Correlation Coefficient: -0.86
-------------------------------------------

Enter learning rate for the training (between 0 and 1): 0.5

Enter iterations number rate for the training: 300

Model calculation...
-------------------------------------------
Regression Line: y = -1.00x + 0.94
-------------------------------------------
```

<img src="https://github.com/Anastasiia-Ni/ft_linear_regression/blob/main/assets/Distribution_of_car_prices.png" width="500">


2. Prediction:
- Run predict.py to predict car prices based on user-input mileage.
```
$ python3 predict.py

Write the mileage (in km) to predict the price: 50000
-------------------------------------------
The estimated price of the car is: 7426.41
-------------------------------------------
```
3. Precision (bonus part):
- Run precision.py to calculate the coefficient of determination for model accuracy assessment.
```
$ python3 precision.py
-------------------------------------------
Mean Absolute Error: 557.73
-------------------------------------------
-------------------------------------------
Precision (R^2): 0.7330
-------------------------------------------
```
  

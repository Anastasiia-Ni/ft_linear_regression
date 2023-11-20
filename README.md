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
`$ y = \theta_0 + \theta_1 \cdot x $`
Where:
- y is the dependent variable (car price in this project).
- x is the independent variable (car mileage).
- theta_0 is the intercept.
- theta_1 s the slope.

### Pearson Correlation Coefficient:
The Pearson correlation coefficient, often denoted as r, measures the linear relationship between two variables. It takes values between -1 and 1, where:
- r=1 indicates a perfect positive linear relationship.
- r=−1 indicates a perfect negative linear relationship.
- r=0 indicates no linear relationship.

In the context of this project, the Pearson correlation coefficient is used to assess the correlation between car mileage and prices, 
providing insights into the strength and direction of the linear relationship. 
A coefficient close to 1 or -1 suggests a strong linear relationship, making it a valuable indicator for the quality of the linear regression model. 
The closer r is to 1 or -1, the better the linear regression captures the underlying patterns in the data. in the direction that reduces the cost.

### Gradient Descent:
Gradient descent is an optimization algorithm used to find the minimum of a function iteratively. 
In the context of machine learning, it is employed to minimize the cost function, 
which measures the difference between the predicted values and the actual values. 
The algorithm adjusts the model parameters (in this case theta0 and theta1) 

СЮДА НАЙТИ НОРМАЛЬНУЮ формулу с объяснением и рисунки
про наименьшие квадраты и как считается оптимальный график

в прогрмме вводится шаг и число итераций. написуть тут что это и как влияет а так же оптимальные числа для нашего случая

### Precision (bonus part):
Объяснить как считается Mean Absolute Error: и Precision (R^2) и о чем вообще эти коээфициенты

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
  
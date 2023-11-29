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
- theta_0 is the intercept (displacement coefficient).
- theta_1 s the slope (slope factor).

![Gradient Descend](https://private-user-images.githubusercontent.com/73773741/286714200-01368c23-e176-4f22-9e41-f0f86aa59605.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDEyODUxNzcsIm5iZiI6MTcwMTI4NDg3NywicGF0aCI6Ii83Mzc3Mzc0MS8yODY3MTQyMDAtMDEzNjhjMjMtZTE3Ni00ZjIyLTllNDEtZjBmODZhYTU5NjA1LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTI5VDE5MDc1N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU4OGQ5N2ZiM2RjZWQwNjIwZGVhY2VmMDk1NThiOGJjNWU0YjY1ODUxYWMxNTgxNWUzNTAxYzgwNDY0MTQwYmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.HncNexrU0ZBUCDhYCFmgzKmZ0ikqZi24ZoI_do9LNeo)
  РИСУНОК Visualizing an example of linear regression on a graph.
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
РИСУНОК

In the graphical representation, this corresponds to finding the line that minimizes the sum of the squared distances between each data point and the corresponding point on the line.


### Gradient Descent:
Gradient descent is an optimization algorithm used to find the minimum of a function iteratively. 
In the context of machine learning, it is employed to minimize the cost function, 
which measures the difference between the predicted values and the actual values. 
The algorithm adjusts the model parameters (in this case theta0 and theta1) 

СЮДА НАЙТИ НОРМАЛЬНУЮ формулу с объяснением и рисунки


в прогрмме вводится шаг и число итераций. написуть тут что это и как влияет а так же оптимальные числа для нашего случая
на примере спуска человека с горы (рисунок есть )

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
  

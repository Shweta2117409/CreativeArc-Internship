OVERVIEW:
-This assessment focuses on understanding how Linear Regression works internally rather than relying on libraries.
-The model is implemented completely from scratch using NumPy, and its behavior is analyzed through loss curves and learning rate experiments.
-Finally, the results are compared with sklearn’s implementation to understand practical differences.

DATASET:
Name:Salary Dataset – Simple Linear Regression
File used: Salary_Data.csv
Feature (X): YearsExperience
Target (y): Salary

Why is this dataset suitable for Linear Regression?
-This dataset is suitable for Linear Regression because it shows a clear linear relationship between years of experience and salary. As experience increases, salary generally increases.

-There is only one feature, which simplifies the model and helps in understanding how weight and bias affect predictions.

-Additionally, the dataset has no categorical variables and very little noise, allowing gradient descent to converge smoothly.


What assumption does Linear Regression make about the relationship between X and y?
-Linear Regression assumes that the relationship between the independent variable (X) and the dependent variable (y) is linear.
                         
                         y=wx+b

-It also assumes that errors are continuous, independent, and normally distributed with constant variance.

-In this dataset, the trend between years of experience and salary approximately follows a straight line.

Comparison: Scratch Model vs sklearn Model
-Both the scratch implementation and sklearn’s Linear Regression produce similar values for weight and bias, but they are not exactly identical.

Why are the values similar but not exactly the same?
-The scratch model uses gradient descent, which is an iterative optimization technique. It updates parameters step by step and stops after a fixed number of epochs.

-On the other hand, sklearn uses highly optimized mathematical solvers that converge more precisely.

What does sklearn do differently internally?
-sklearn’s Linear Regression:
-Uses optimized numerical solvers
-Handles numerical stability better
-Converges faster and more precisely
-Automatically manages matrix operations and edge cases

Designed to show how learning actually happens through gradient descent.

CONCLUSION
-This assessment helped in understanding the complete learning process of Linear Regression, including prediction, loss calculation, gradient computation, and parameter updates.


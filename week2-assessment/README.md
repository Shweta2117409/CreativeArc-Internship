## Task 1: Data Understanding

### 1. Which column looks most dangerous and why?

-The **Installs** column appears to be the most dangerous. Although it represents numeric information, it is stored as an object type and contains non-numeric characters such as commas and the plus (+) symbol.
-If not carefully cleaned and converted, calculations involving this column may produce incorrect results or fail without obvious errors, making it particularly risky.

### 2. Which column should NEVER be used for ML and why?

-The **App** column should never be used for machine learning. It is an identifier that represents the name of each application rather than a feature with predictive meaning. 
-Additionally, this column has extremely high
cardinality, which can lead to overfitting and increased model complexity without improving performance.

### 3. Which column seems cleanest and why?

-The **Category** column appears to be one of the cleanest columns in the
dataset. It contains categorical values that are relatively consistent and meaningful, representing the type of application.
-Unlike numeric columns such as Installs or Price, it does not contain symbols or mixed
data types, and it is easier to interpret directly.
-While minor standardization may still be required, the column is largely usable in
its current form for analysis and modeling.

## Task 2: Missing Value Strategy

-Blindly dropping rows with missing values in this dataset would be dangerous because the missing data is not necessarily random.

 -Removing these rows would bias the dataset toward older and more popular apps, reducing the representation of new or less visible developers.

 -Such bias can result in misleading EDA conclusions and machine learning models that perform well on historical data but fail to generalize to real-world scenarios.
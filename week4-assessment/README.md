# Week 4 Assessment – Model Selection, Bias–Variance & Evaluation

## Dataset
The Heart Disease dataset was used for this assessment. It contains multiple numerical features describing patient health indicators such as age, cholesterol, blood pressure, and heart rate. The target variable indicates the presence or absence of heart disease.

## Data Understanding
The dataset is not linearly separable because the relationship between features and the target is non-linear. Multiple features interact with each other in complex ways (for example, age combined with cholesterol and maximum heart rate), which cannot be separated using a single linear boundary.

Model selection is difficult because:
- Different regions of the feature space show different patterns.
- Some models easily overfit due to the small dataset size.
- Noise and overlapping class distributions make generalization challenging.

## Models Trained
The following models were trained and evaluated:
- Decision Tree (no depth limit)
- Decision Tree (manually tuned max_depth)
- Random Forest
- K-Nearest Neighbors (with feature scaling)

Training and validation accuracy were compared to analyze bias–variance behavior and model generalization.

## Evaluation Strategy
A train-validation split was used consistently across models. Feature scaling was applied where required (KNN). Hyperparameters were varied manually to observe underfitting and overfitting transitions.

Plots were generated to visualize performance trends and support conclusions drawn from numerical results.

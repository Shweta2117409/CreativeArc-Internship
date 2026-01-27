# Week 5 – Final Decision & Reflection

## Model Selection
Logistic Regression was selected as the final model due to its simplicity,
interpretability, and stable performance across validation and cross-validation
experiments. With appropriate preprocessing and feature engineering, it achieved
competitive accuracy while remaining computationally efficient.

## Optimization Strategy
Model performance was improved through:
- Domain-driven feature engineering (interaction and non-linear features)
- Manual hyperparameter experimentation to understand bias–variance behavior
- Focused GridSearchCV to identify optimal regularization strength

This approach avoided exhaustive search while maintaining robustness.

## Evaluation & Reliability
Model evaluation used:
- Stratified train–validation splits
- Stratified K-Fold cross-validation
- Nested cross-validation for unbiased generalization estimation

Consistent performance across folds indicates strong model stability.

## Reproducibility & Deployment Readiness
The full preprocessing and model pipeline was saved using joblib.
Reloaded models produced identical predictions, and retraining with fixed random
states yielded reproducible results.

This confirms the solution is suitable for production deployment and future reuse.

## Final Conclusion
The final pipeline demonstrates a complete ML engineering workflow:
data cleaning, feature engineering, optimization, evaluation, persistence, and
reproducibility. The solution balances performance, interpretability, and
engineering best practices.

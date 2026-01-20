import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv("data/dataset.csv")


df = df.drop(columns=["id"])


X = df.drop(columns=["num"])
y = df["num"]


X = pd.get_dummies(X, drop_first=True)


X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model 3: Random Forest


rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


rf.fit(X_train, y_train)


train_pred_rf = rf.predict(X_train)
val_pred_rf = rf.predict(X_val)


train_acc_rf = accuracy_score(y_train, train_pred_rf)
val_acc_rf = accuracy_score(y_val, val_pred_rf)

print("\nRandom Forest")
print("Training Accuracy:", train_acc_rf)
print("Validation Accuracy:", val_acc_rf)
print("Accuracy Gap (Train - Val):", train_acc_rf - val_acc_rf)


# TASK 3: Random Forest - Number of Trees vs Accuracy


n_estimators_list = [10, 20, 50, 100, 150, 200]

train_accuracies = []
val_accuracies = []

for n in n_estimators_list:
    rf_model = RandomForestClassifier(
        n_estimators=n,
        random_state=42
    )
    rf_model.fit(X_train, y_train)

    train_pred = rf_model.predict(X_train)
    val_pred = rf_model.predict(X_val)

    train_accuracies.append(accuracy_score(y_train, train_pred))
    val_accuracies.append(accuracy_score(y_val, val_pred))

    import matplotlib.pyplot as plt

plt.figure()
plt.plot(n_estimators_list, train_accuracies, label="Training Accuracy")
plt.plot(n_estimators_list, val_accuracies, label="Validation Accuracy")
plt.xlabel("Number of Trees (n_estimators)")
plt.ylabel("Accuracy")
plt.title("Random Forest: Number of Trees vs Accuracy")
plt.legend()
plt.savefig("plots/elbow.png")
plt.show()



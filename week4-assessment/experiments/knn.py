import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# ===============================
# Load dataset
# ===============================
df = pd.read_csv("data/dataset.csv")

# Drop ID column (not useful)
df = df.drop(columns=["id"])

# Separate features and target
X = df.drop(columns=["num"])
y = df["num"]

# ===============================
# Encode categorical features
# ===============================
X = pd.get_dummies(X, drop_first=True)

# ===============================
# Handle missing values (MANDATORY for KNN)
# ===============================
X = X.fillna(X.median())

# ===============================
# Train-validation split
# ===============================
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# Feature scaling (MANDATORY for KNN)
# ===============================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# ===============================
# TASK 2: KNN Model (K = 5)
# ===============================
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

train_pred_knn = knn.predict(X_train_scaled)
val_pred_knn = knn.predict(X_val_scaled)

train_acc_knn = accuracy_score(y_train, train_pred_knn)
val_acc_knn = accuracy_score(y_val, val_pred_knn)

print("\nKNN (K = 5)")
print("Training Accuracy:", train_acc_knn)
print("Validation Accuracy:", val_acc_knn)
print("Accuracy Gap (Train - Val):", train_acc_knn - val_acc_knn)

# ===============================
# TASK 3: K vs Accuracy Experiment
# ===============================
k_values = range(1, 21)
train_accuracies = []
val_accuracies = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)

    train_pred = model.predict(X_train_scaled)
    val_pred = model.predict(X_val_scaled)

    train_accuracies.append(accuracy_score(y_train, train_pred))
    val_accuracies.append(accuracy_score(y_val, val_pred))

# ===============================
# Plot K vs Accuracy
# ===============================
plt.figure()
plt.plot(k_values, train_accuracies, label="Training Accuracy")
plt.plot(k_values, val_accuracies, label="Validation Accuracy")
plt.xlabel("Number of Neighbors (K)")
plt.ylabel("Accuracy")
plt.title("KNN: K vs Accuracy")
plt.legend()
plt.savefig("plots/k_vs_accuracy.png")
plt.show()

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv("data/dataset.csv")


df = df.drop(columns=["id"])

X = df.drop(columns=["num"])
y = df["num"]


X = pd.get_dummies(X, drop_first=True)


X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", X_train.shape[0])
print("Validation samples:", X_val.shape[0])


# MODEL 1 : DECISION TREE (NO DEPTH LIMIT)

dt_full = DecisionTreeClassifier(random_state=42)


dt_full.fit(X_train, y_train)

train_pred = dt_full.predict(X_train)
val_pred = dt_full.predict(X_val)


train_acc = accuracy_score(y_train, train_pred)
val_acc = accuracy_score(y_val, val_pred)

print("\nDecision Tree (No depth limit)")
print("Training Accuracy:", train_acc)
print("Validation Accuracy:", val_acc)
print("Accuracy Gap (Train - Val):", train_acc - val_acc)

# MODEL 2 : DECISION TREE (NO DEPTH LIMIT)

dt_full = DecisionTreeClassifier(random_state=42)


dt_full.fit(X_train, y_train)


train_pred = dt_full.predict(X_train)
val_pred = dt_full.predict(X_val)


train_acc = accuracy_score(y_train, train_pred)
val_acc = accuracy_score(y_val, val_pred)

print("\nDecision Tree (No depth limit)")
print("Training Accuracy:", train_acc)
print("Validation Accuracy:", val_acc)
print("Accuracy Gap (Train - Val):", train_acc - val_acc)

# MODEL 2 : DECISION TREE (LIMITED DEPTH)

dt_limited = DecisionTreeClassifier(
    max_depth=5,   # manually chosen
    random_state=42
)


dt_limited.fit(X_train, y_train)


train_pred_limited = dt_limited.predict(X_train)
val_pred_limited = dt_limited.predict(X_val)


train_acc_limited = accuracy_score(y_train, train_pred_limited)
val_acc_limited = accuracy_score(y_val, val_pred_limited)

print("\nDecision Tree (max_depth = 5)")
print("Training Accuracy:", train_acc_limited)
print("Validation Accuracy:", val_acc_limited)
print("Accuracy Gap (Train - Val):", train_acc_limited - val_acc_limited)



# TASK 3: Depth vs Accuracy Experiment


depths = range(1, 21)

train_accuracies = []
val_accuracies = []

for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    val_pred = model.predict(X_val)

    train_accuracies.append(accuracy_score(y_train, train_pred))
    val_accuracies.append(accuracy_score(y_val, val_pred))

    import matplotlib.pyplot as plt

plt.figure()
plt.plot(depths, train_accuracies, label="Training Accuracy")
plt.plot(depths, val_accuracies, label="Validation Accuracy")
plt.xlabel("Tree Depth")
plt.ylabel("Accuracy")
plt.title("Decision Tree: Depth vs Accuracy")
plt.legend()
plt.savefig("plots/bias_variance.png")
plt.show()




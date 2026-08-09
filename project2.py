"""
DecodeLabs - Project 2
Data Classification Using AI

This project demonstrates:
1. Loading the Iris dataset
2. Feature scaling using StandardScaler
3. Splitting data into training and testing sets
4. Training a K-Nearest Neighbors (KNN) classifier
5. Making predictions
6. Evaluating the model using a confusion matrix and F1 score
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score


# --------------------------------------------------
# 1. LOAD THE IRIS DATASET
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("Dataset: Iris")
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Classes:", iris.target_names)


# --------------------------------------------------
# 2. SPLIT DATA INTO TRAINING AND TESTING SETS
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# --------------------------------------------------
# 3. FEATURE SCALING
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# 4. CREATE THE KNN CLASSIFICATION MODEL
# --------------------------------------------------

model = KNeighborsClassifier(n_neighbors=5)


# --------------------------------------------------
# 5. TRAIN THE MODEL
# --------------------------------------------------

model.fit(X_train_scaled, y_train)


# --------------------------------------------------
# 6. MAKE PREDICTIONS
# --------------------------------------------------

y_pred = model.predict(X_test_scaled)


# --------------------------------------------------
# 7. EVALUATE THE MODEL
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

conf_matrix = confusion_matrix(y_test, y_pred)

f1 = f1_score(y_test, y_pred, average="weighted")


# --------------------------------------------------
# 8. DISPLAY RESULTS
# --------------------------------------------------

print("\n---------------- MODEL RESULTS ----------------")

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(conf_matrix)

print("\nF1 Score:", round(f1, 4))


# --------------------------------------------------
# 9. DISPLAY PREDICTIONS
# --------------------------------------------------

print("\nPredicted classes:")
print(iris.target_names[y_pred])

print("\nActual classes:")
print(iris.target_names[y_test])
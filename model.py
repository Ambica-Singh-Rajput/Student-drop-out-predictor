import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_squared_error, r2_score

print("Starting model training...")

data = pd.read_csv("student_dropout_dataset.csv")

X = data.drop("dropout",axis=1)

y = data["dropout"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

models = {

    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Decision Tree": DecisionTreeClassifier(),

    "Random Forest": RandomForestClassifier(),

    "SVM": SVC()

}

results = {}

for name,model in models.items():

    model.fit(X_train,y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test,pred)

    results[name] = acc

print("\nAlgorithm Accuracy Comparison")
print(results)

# graph
plt.figure()

plt.bar(results.keys(),results.values())

plt.title("Algorithm Accuracy Comparison")

plt.xticks(rotation=20)

plt.show()

# best model
best_model = RandomForestClassifier()

best_model.fit(X_train,y_train)

pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test,pred)

rmse = np.sqrt(mean_squared_error(y_test,pred))

r2 = r2_score(y_test,pred)

print("\nBest Model: Random Forest")

print("Accuracy:",accuracy)

print("RMSE:",rmse)

print("R2 Score:",r2)

cm = confusion_matrix(y_test,pred)

print("\nConfusion Matrix")

print(cm)

print("\nClassification Report")

print(classification_report(y_test,pred))

# feature importance
importance = best_model.feature_importances_

plt.figure()

plt.barh(X.columns,importance)

plt.title("Feature Importance")

plt.show()

# save model
pickle.dump(best_model,open("model.pkl","wb"))

print("\nmodel.pkl created successfully")
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

iris = pd.read_csviris = pd.read_csv ("C:\\Users\\naveen\\Desktop\\iris.csv")

print(iris.head())

X = iris.drop(columns=['target']) 
y = iris['target']                 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

dt_classifier = DecisionTreeClassifier(criterion='gini', max_depth=None, random_state=42)

dt_classifier.fit(X_train, y_train)

y_pred = dt_classifier.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

plt.figure(figsize=(12, 8))
plot_tree(dt_classifier, 
          feature_names=X.columns, 
          class_names=[str(label) for label in y.unique()], 
          filled=True)
plt.show()

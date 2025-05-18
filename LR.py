import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score
import pandas as pd

class LogisticRegression:
    def __init__(self, learning_rate=0.01, iteration=1000):
        self.learning_rate = learning_rate
        self.iteration = iteration
        self.theta = None

    def add_intercept(self, X):
        # Step 1: Create a column vector of ones with the same number of rows as X
        intercept_column = np.ones((X.shape[0], 1))

        # Step 2: Concatenate the intercept column with X horizontally
        X_with_intercept = np.concatenate((intercept_column, X),axis=1)

        # Step 3: Return the feature matrix with the intercept column added
        return X_with_intercept

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        X = self.add_intercept(X)
        self.theta = np.zeros((X.shape[1]))
        for _ in range(self.iteration):
            z = np.dot(X, self.theta)
            h = self.sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.theta -= gradient * self.learning_rate
            #print(self.theta)

    def predict_prob(self, X):
        X = self.add_intercept(X)
        return self.sigmoid(np.dot(X, self.theta))

    def predict(self, X, threshold=0.5):
        return self.predict_prob(X) >= threshold

data = pd.read_csv("Breastcancer_data.csv")
data.info()
data[4:]

X = data.iloc[:,2:-1].values
X = np.float64(X)
y = data.iloc[:,1].values
y = np.where(y == 'M', 1, 0)
y.shape, X.shape , y.size

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state = 42)

model = LogisticRegression()

model.fit(X_train,y_train)

val_predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, val_predictions)
precision = precision_score(y_test, val_predictions)
recall = recall_score(y_test, val_predictions)
f1 = f1_score(y_test, val_predictions)

print("Validation Set Metrics:")
print("Accuracy: {:.2f}".format(accuracy))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("F1 Score: {:.2f}".format(f1))

from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(y_test, val_predictions)
print(confusion)
# print("Class 0 predicted and true : ")
# print(confusion[0][0])
# print("Class 0 predicted and false : ")
# print(confusion[0][1])
# print("Class 1 predicted and false : ")
# print(confusion[1][0])
# print("Class 1 predicted and true : ")
# print(confusion[1][1])




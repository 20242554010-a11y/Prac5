from sklearn.tree import DecisionTreeClassifier

# Training data
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

# Create and train model
model = DecisionTreeClassifier()
model.fit(X, y)

def predict_pass(study_hours):
    prediction = model.predict([[study_hours]])

    if prediction[0] == 1:
        return "Likely to Pass"
    else:
        return "Needs More Study"
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, 'app/model.joblib')
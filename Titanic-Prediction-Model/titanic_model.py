import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load Titanic dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Basic preprocessing
df = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Survived"]]
df = df.dropna()
df["Sex"] = df["Sex"].map({"male": 1, "female": 0})

X = df.drop("Survived", axis=1)
y = df["Survived"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "titanic_model.pkl")

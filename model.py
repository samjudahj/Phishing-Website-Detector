import pandas as pd
from sklearn.linear_model import LogisticRegression
from feature_extraction import extract_features
import pickle

data = pd.read_csv("dataset.csv")

X = data["url"].apply(lambda x: extract_features(x)).tolist()
y = data["label"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        prediction = model.predict([extract_features(url)])
        result = "⚠️ Phishing Website" if prediction[0] == 1 else "✅ Legitimate Website"
    return render_template("index.html", result=result)

app.run()

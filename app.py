from flask import Flask, request
from model import predict_pass

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud ML Docker Application is Running!"

@app.route("/predict")
def predict():

    hours = float(request.args.get("hours", 5))

    result = predict_pass(hours)

    return {
        "study_hours": hours,
        "prediction": result
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
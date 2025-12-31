from flask import Flask, render_template, request
import joblib
import pandas as p

app = Flask(__name__)

# Load model
model = joblib.load("diabetes_model.pkl")

columns = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = [
        int(request.form["preg"]),
        int(request.form["glucose"]),
        int(request.form["bp"]),
        int(request.form["skin"]),
        int(request.form["insulin"]),
        float(request.form["bmi"]),
        float(request.form["dpf"]),
        int(request.form["age"])
    ]

    df = p.DataFrame([data], columns=columns)
    prediction = model.predict(df)[0]

    result = "Diabetic" if prediction == 1 else "Not Diabetic"
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

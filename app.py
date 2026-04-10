from flask import Flask, render_template, request
import pickle

model = pickle.load(open("model.pkl","rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():

    try:

        features = [

            float(request.form['attendance']),

            float(request.form['study_hours']),

            float(request.form['previous_grade']),

            float(request.form['assignments_completed']),

            float(request.form['internet_access']),

            float(request.form['family_income']),

            float(request.form['stress_level']),

            float(request.form['extracurricular'])

        ]

        prediction = model.predict([features])[0]

        if prediction == 1:

            result = "⚠ HIGH RISK OF DROPOUT"

        else:

            result = "✅ LOW RISK STUDENT"

        return render_template("index.html",prediction_text=result)

    except:

        return render_template("index.html",prediction_text="Invalid input")

if __name__ == "__main__":
    app.run(debug=True)
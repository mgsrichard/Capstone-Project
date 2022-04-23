from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

with open('rf_model_pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/graphs")
def graphs():
    return render_template('graphs.html')

@app.route("/predictor", methods=["GET","POST"])
def predictor():
    if request.method == "POST":
        yearsofexperience = request.form["yearsofexperience"]
        yearsatcompany = request.form["yearsatcompany"]
        region = request.form["region"]
        pred =  model.predict(np.array([[int(yearsofexperience), int(yearsatcompany), int(region)]]))
        return render_template('predictor.html', pred=str(pred))
    return render_template('predictor.html')


if __name__ == '__main__':
    app.run(debug=True)
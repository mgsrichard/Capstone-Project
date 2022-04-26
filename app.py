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
        if pred == 1:
            output = "Your predicted salary is between $25,000-50,000"
        elif pred == 2:
            output = "Your predicted salary is between $50,001-75,000"
        elif pred == 3:
            output = "Your predicted salary is between $75,001-100,000"  
        elif pred == 4:
            output = "Your predicted salary is between $100,001-125,000" 
        elif pred == 5:
            output = "Your predicted salary is between $125,001-150,000" 
        elif pred == 6:
            output = "Your predicted salary is between $150,001-175,000" 
        elif pred == 7:
            output = "Your predicted salary is between $175,001-200,000" 
        elif pred == 8:
            output = "Your predicted salary is between $200,001-225,000" 
        else:
            output = "Your predicted salary is greater than $225,000" 
        return render_template('predictor.html', output=str(output))
    return render_template('predictor.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Home")
def home():
    return render_template('index.html', title='Home')

@app.route("/Graphs")
def graphs():
    return render_template('graphs.html', title='Graphs')

@app.route("/Predictor")
def predictor():
    return render_template('predictor.html',title='Predictor')

if __name__ == '__main__':
    app.run()
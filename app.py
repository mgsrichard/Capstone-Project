from flask import Flask, render_template

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

@app.route("/predictor")
def predictor():
    return render_template('predictor.html')

if __name__ == '__main__':
    app.run(debug=True)
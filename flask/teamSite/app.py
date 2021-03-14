from flask import Flask, render_template
from datetime import date
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to our Team Site'

@app.route('/Mohamed')
def mohamed():
    return render_template('mohamed.html')

@app.route('/Cydney')
def cydney():
    return render_template('cydney.html')

@app.route('/Mia')
def mia():
    return render_template('mia.html')

@app.route('/Abdul')
def abdul():
    return render_template('abdul.html')

@app.route('/Nasa')
def nasa():
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data = response.json
    return render_template('nasa.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
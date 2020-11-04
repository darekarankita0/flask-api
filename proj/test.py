from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    #return render_template('temperature.html')
    name = request.form['name']
    r=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+name+'&appid=639abaa2a3314a03b2a01e926252ed4a')
    json_object=r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15)* 1.8 + 32
    return render_template('temperature.html', temp=temp_f)
    #return str(temp_k)

@app.route('/')
def index():
    #return 'Hello'
    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/convert/celsius_to_kelvin/<float:celsius>')
def celsius_to_kelvin(celsius):
    return f'{celsius + 273.15}K'

#URL - http://192.168.1.245:8080/convert/celsius_to_kelvin/122.3

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
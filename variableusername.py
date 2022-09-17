from platform import python_branch
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/order/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

#URL - http://192.168.1.245:8080/order/nishant/12
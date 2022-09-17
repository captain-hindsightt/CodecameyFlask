from platform import python_branch
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/order/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'


@app.route('/article/<article_name>')
def article(article_name):
  return f'''
  <h2>{article_name.replace('-', ' ').title()}</h2>
  <a href='/'>Return back to home page</a>
  '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
#URL - htt
#URL - http://192.168.1.245:8080/order/nishant/12

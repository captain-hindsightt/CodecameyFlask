from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')

def home():
    return '''
    <h1>Hello, World!</h1>
    <p>My first paragraph.</p>
    <a href="https://www.codecademy.com">CODECADEMY</a>
    '''

@app.route('/reporter')
def reporter():
    return '<h1>Reporter Bio</h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


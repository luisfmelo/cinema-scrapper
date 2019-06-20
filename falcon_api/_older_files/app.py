import os

from flask import Flask
app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']


@app.route("/")
def signup():
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)


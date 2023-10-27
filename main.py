from flask import Flask
import config

app = Flask(__name__)

EMAIL = config.EMAIL
PASSWORD = config.PASSWORD


@app.route('/')
def home():
    return f"My {EMAIL} and My {PASSWORD}"


if __name__ == '__main__':
    app.run(debug=True)

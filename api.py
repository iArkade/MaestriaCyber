from flask import Flask
from yahoo_data_fetcher import get_price

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/")
def api():
    return get_price("DIS")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
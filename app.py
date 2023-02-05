from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/page1")
def pageOne():
    return "This is page One"

if __name__ == "__main__":
    app.run(host="192.168.0.67")

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_Owner():
    return "Hello,Owner!"


if __name__ == "__main__":
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/env")
def env():
    env_str = app.config["ENV"]
    return {"env": env_str}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")

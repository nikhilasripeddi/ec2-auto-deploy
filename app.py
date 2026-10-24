
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Flask app deployed automatically using AWS EC2 and GitHub Actions."

if __name__ == "__main__":
    app.run()

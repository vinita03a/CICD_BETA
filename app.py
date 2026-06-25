from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to CICD Project"

if __name__=="_main__":
    app.run(debug=True)
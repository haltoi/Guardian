from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/apply")
def studentApply():
    print("hi")

if __name__ == "__main__":
    app.run()
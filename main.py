from flask import Flask, request, jsonify
from time import sleep
import os

app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({ "data": "Hello SENG2021" }), 200

@app.route("/slow")
def slow():
    delay = 2
    delay_arg = request.args.get("delay")
    if delay_arg is not None:
        try:
            delay = int(delay_arg)
        except:
            print("error converting delay to int")

    sleep(delay)
    return jsonify({ "data": f"So Slow, {delay} seconds Slow" }), 200

if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", default=5000)))

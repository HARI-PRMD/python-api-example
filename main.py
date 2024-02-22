from flask import Flask, request, jsonify
from time import sleep

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
    return jsonify({ "data": "So Slow, {delay} seconds Slow" }), 200

if __name__ == "__main__":
    app.run(debug=True)
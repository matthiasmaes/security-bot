from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route("/ping")
def me_api():
    return {
        "response": "pong",
    }

@app.post("/unlocked")
def unlocked():
    parsed_json = request.get_json(silent=True)
    print(parsed_json['key'])
    return 'ok'


    # r = requests.post("https://hooks.slack.com/services/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", json = {'text': 'Yes, this works'})
    # return r.text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
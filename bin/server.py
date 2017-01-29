from flask import Flask, jsonify, request
from detect import predictor
import lxml.html

app = Flask(__name__)


@app.route("/detect", methods=["GET"])
def detect():
    headline = request.args.get("headline", "")
    clickbaitiness = predictor.predict(headline)
    return jsonify({ "clickbaitiness": round(clickbaitiness * 100, 2) })
    

@app.route("/detect/url", methods=["GET"])
def detect_from_url():
    url = request.args.get("url", "")
    clickbaitiness = predictor.predict(lxml.html.parse(url).find(".//title").text)
    return jsonify({ "clickbaitiness": round(clickbaitiness * 100, 2) })


if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify



app=Flask(__name__)
@app.route("/")
def home():
  return "Hello. This is the home page"
@app.route("/ping")
def ping():
  return jsonify(status="ok")
@app.route("/echo", methods=["POST"])
def echo():
  return jsonify(request.json)
if __name__ == "__main__":
  app.run()

from flask import Flask, request, jsonify
import random




players=[]
choices=[]
resutl=None




app=Flask(__name__)
@app.route("/")
def home():
  return "Hello. This is the home page for rock paper scissors game"
@app.route("/ping")
def ping():
  return jsonify(status="ok")
@app.route("/echo", methods=["POST"])
def echo():
  return jsonify(request.json)
@app.route("/join", methods=["GET"])
def join():
  player_id=random.randint(3000,9000)
  players.append({"id":player_id})
  return jsonify(player_id=player_id)
@app.route("/play",methods=["POST"])
def play():
  request_data=request.json
  if(request_data["player_id"] not in player):
    return jsonify({"message":"no player with that id found"})
  if(len(players)==2):
    a=0
    winner=decide_winner()
  else:
    a=0
    choices.append(request_data["choice"])
  
  
if __name__ == "__main__":
  app.run()

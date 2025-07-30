from flask import Flask, request, jsonify, render_template
from agent_ai.agent_ai import class_agent_ai
from entities.client import class_client
from entities.service import class_service
from entities.coiffeur import class_coiffeur
from entities.rendezvous import class_rendezvous
from entities.salon import class_salon

app = Flask(__name__)

salon = class_salon("Salon Intelligents")
agent = class_agent_ai("Agent Coiffure", salon)



@app.route("/parler", methods=["POST"])
def parler():
    data = request.get_json()
    message = data.get("message", "")
    reponse = agent.discuter(message)
    return jsonify({"reponse": reponse})

@app.route("/reset", methods=["POST"])
def reset():
    agent.etat = "attente"
    agent.temp_data.clear()
    return jsonify({"message": "Agent réinitialisé."})



@app.route("/")
def accueil():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)



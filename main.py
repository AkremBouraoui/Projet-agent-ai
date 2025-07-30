import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()  # لتحميل متغيرات .env
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def accueil():
    return jsonify({"message": "Bienvenue dans l'API du salon intelligent."})

@app.route("/parler", methods=["POST"])
def discuter():
    data = request.get_json()
    message = data.get("message", "")

    try:
        reponse_ai = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un agent pour un salon de coiffure. Réponds aux demandes des clients comme prendre, modifier ou annuler un rendez-vous."},
                {"role": "user", "content": message}
            ]
        )
        texte = reponse_ai.choices[0].message["content"]
        return jsonify({"reponse": texte})

    except Exception as e:
        return jsonify({"erreur": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

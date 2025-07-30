import openai
import os
from entities.client import class_client
from entities.rendezvous import class_rendezvous
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class class_agent_ai:
    def __init__(self, nom, salon):
        self.nom = nom
        self.salon = salon
        self.etat = "attente"
        self.memoire = {}
        self.id_rdv_counter = 1

    def discuter(self, message):
        msg = message.lower().strip()

        # --- 🔎 Fonctionnalité 2 : Recherche par nom
        if msg.startswith("je suis "):
            nom_recherche = msg.replace("je suis", "").strip()
            for client in self.salon.clients:
                if client.nom.lower() == nom_recherche:
                    rdvs = [r for r in self.salon.rendezvous if r.id_client == client.id_client]
                    if not rdvs:
                        return f"Aucun rendez-vous trouvé pour {client.nom}."
                texte = f"📅 Rendez-vous pour {client.nom} :\n"
                for rdv in rdvs:
                    coiffeur = next((c for c in self.salon.coiffeurs if c.id_coiffeur == rdv.id_coiffeur), None)
                    service = next((s for s in self.salon.services if s.id_service == rdv.id_service), None)
                    if coiffeur and service:
                        texte += f"   ↪️ {rdv.date} à {rdv.heure} avec {coiffeur.nom} pour {service.nom_service}\n"
                    else:
                        texte += f"   ↪️ {rdv.date} à {rdv.heure} (coiffeur ou service inconnu)\n"
                return texte


        # --- Cas spécial : GPT uniquement
        if self.etat == "attente" and all(mot not in msg for mot in ["service", "coiffeur", "prendre", "rendez", "modifier", "supprimer", "client"]):
            try:
                reponse_ai = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Tu es un agent intelligent pour un salon de coiffure. Réponds de manière simple."},
                        {"role": "user", "content": message}
                    ]
                )
                texte = reponse_ai.choices[0].message["content"]
                return texte
            except Exception as e:
                return f"Erreur IA: {str(e)}"

        # --- Système interne ---
        if self.etat == "attente" or "supprimer" in msg or "modifier" in msg:

            if "client" in msg or "liste des clients" in msg:
                if not self.salon.clients:
                    return "Aucun client enregistré pour le moment."
                texte = "👥 Liste des clients :\n"
                for client in self.salon.clients:
                    texte += f"{client.id_client}. Nom: {client.nom}, Téléphone: {client.telephone}\n"
                    for rdv in self.salon.rendezvous:
                        if rdv.id_client == client.id_client:
                            coiffeur = next((c for c in self.salon.coiffeurs if c.id_coiffeur == rdv.id_coiffeur), None)
                            service = next((s for s in self.salon.services if s.id_service == rdv.id_service), None)
                            nom_coiffeur = f"{coiffeur.nom} ({coiffeur.specialite})" if coiffeur else f"Coiffeur #{rdv.id_coiffeur}"
                            nom_service = service.nom_service if service else f"Service #{rdv.id_service}"
                            texte += f"   ↪️ Rendez-vous: {rdv.date} à {rdv.heure} avec {nom_coiffeur} pour {nom_service}\n"
                return texte

            if "modifier" in msg:
                self.etat = "modif_id"
                return "Entrez l'ID du rendez-vous à modifier :"

            elif "supprimer" in msg:
                self.etat = "supprimer_id"
                return "Entrez l'ID du rendez-vous à supprimer :"

            elif "service" in msg:
                return "Voici la liste des services:\n" + "\n".join(
                    [f"{s.id_service}. {s.nom_service} - {s.prix}$" for s in self.salon.services])

            elif "coiffeur" in msg:
                return "Voici la liste des coiffeurs:\n" + "\n".join(
                    [f"{c.id_coiffeur}. {c.nom} ({c.specialite})" for c in self.salon.coiffeurs])

            elif "prendre" in msg or "rendez" in msg:
                self.etat = "nom"
                return "Très bien ! Quel est votre nom ?"

            elif "bonjour" in msg or "salut" in msg:
                return "👋 Bonjour ! Je suis votre assistant pour prendre un rendez-vous. Que souhaitez-vous faire ?"

            else:
                return "Je n'ai pas compris. Souhaitez-vous voir les services, les coiffeurs ou prendre un rendez-vous ?"

        elif self.etat == "nom":
            self.memoire["nom"] = msg
            self.etat = "telephone"
            return "Entrez votre numéro de téléphone :"

        elif self.etat == "telephone":
            self.memoire["telephone"] = msg
            self.etat = "service"
            return "Entrez l'ID du service souhaité :"

        elif self.etat == "service":
            self.memoire["service"] = int(msg)
            self.etat = "coiffeur"
            return "Entrez l'ID du coiffeur souhaité :"

        elif self.etat == "coiffeur":
            self.memoire["coiffeur"] = int(msg)
            self.etat = "date"
            return "Entrez la date (YYYY-MM-DD) :"

        elif self.etat == "date":
            self.memoire["date"] = msg
            self.etat = "heure"
            return "Entrez l'heure (HH:MM) :"

        elif self.etat == "heure":
            self.memoire["heure"] = msg
            self.etat = "confirmation"
            return f"Confirmez-vous le rendez-vous ? (oui/non)"

        elif self.etat == "confirmation":
            if "oui" in msg:
                id_client = len(self.salon.clients) + 1
                client = class_client(id_client, self.memoire["nom"], self.memoire["telephone"])
                self.salon.ajouter_client(client)
                rdv = class_rendezvous(
                    id_rdv=self.id_rdv_counter,
                    id_client=id_client,
                    id_service=self.memoire["service"],
                    id_coiffeur=self.memoire["coiffeur"],
                    date=self.memoire["date"],
                    heure=self.memoire["heure"]
                )
                self.salon.ajouter_rendezvous(rdv)
                self.id_rdv_counter += 1

                # ✅ Fonctionnalité 5 : Confirmation détaillée
                coiffeur = next((c for c in self.salon.coiffeurs if c.id_coiffeur == rdv.id_coiffeur), None)
                service = next((s for s in self.salon.services if s.id_service == rdv.id_service), None)
                nom_coiffeur = f"{coiffeur.nom} ({coiffeur.specialite})" if coiffeur else f"#{rdv.id_coiffeur}"
                nom_service = service.nom_service if service else f"#{rdv.id_service}"

                self.etat = "attente"
                self.memoire.clear()
                return (
                    f"✅ Rendez-vous confirmé !\n"
                    f"📅 Date : {rdv.date}\n"
                    f"🕒 Heure : {rdv.heure}\n"
                    f"💇‍♂️ Coiffeur : {nom_coiffeur}\n"
                    f"🔧 Service : {nom_service}\n"
                    f"🆔 Numéro : {rdv.id_rdv}"
                )
            else:
                self.etat = "attente"
                self.memoire.clear()
                return "❌ Rendez-vous annulé."

        elif self.etat == "modif_id":
            self.memoire["modif_id"] = int(msg)
            self.etat = "modif_date"
            return "Nouvelle date (YYYY-MM-DD) :"

        elif self.etat == "modif_date":
            self.memoire["modif_date"] = msg
            self.etat = "modif_heure"
            return "Nouvelle heure (HH:MM) :"

        elif self.etat == "modif_heure":
            for rdv in self.salon.rendezvous:
                if rdv.id_rdv == self.memoire["modif_id"]:
                    rdv.date = self.memoire["modif_date"]
                    rdv.heure = msg
                    self.etat = "attente"
                    self.memoire.clear()
                    return "✏️ Rendez-vous modifié avec succès."
            self.etat = "attente"
            return "ID non trouvé."

        elif self.etat == "supprimer_id":
            id_a_supprimer = int(msg)
            for rdv in self.salon.rendezvous:
                if rdv.id_rdv == id_a_supprimer:
                    self.salon.rendezvous.remove(rdv)
                    self.etat = "attente"
                    return "🗑️ Rendez-vous supprimé."
            self.etat = "attente"
            return "ID non trouvé."

        return "Je n'ai pas compris votre message."

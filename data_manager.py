import json
from entities.client import class_client
from entities.coiffeur import class_coiffeur
from entities.service import class_service
from entities.rendezvous import class_rendezvous

class class_data_manager:
    def __init__(self):
        self.clients_file = "data/clients.json"
        self.coiffeurs_file = "data/coiffeurs.json"
        self.services_file = "data/services.json"
        self.rendezvous_file = "data/rendezvous.json"

    def charger_clients(self):
        try:
            with open(self.clients_file, "r") as f:
                data = json.load(f)
                return [class_client(**c) for c in data]
        except:
            return []

    def charger_coiffeurs(self):
        try:
            with open(self.coiffeurs_file, "r") as f:
                data = json.load(f)
                return [class_coiffeur(**c) for c in data]
        except:
            return []

    def charger_services(self):
        try:
            with open(self.services_file, "r") as f:
                data = json.load(f)
                return [class_service(**s) for s in data]
        except:
            return []

    def charger_rendezvous(self):
        try:
            with open(self.rendezvous_file, "r") as f:
                data = json.load(f)
                return [class_rendezvous(**r) for r in data]
        except:
            return []

    def sauvegarder(self, chemin, liste_objets):
        try:
            with open(chemin, "w") as f:
                json.dump([obj.__dict__ for obj in liste_objets], f, indent=2)
        except Exception as e:
            print(f"Erreur de sauvegarde: {e}")

    def sauvegarder_tout(self, salon):
        self.sauvegarder(self.clients_file, salon.clients)
        self.sauvegarder(self.coiffeurs_file, salon.coiffeurs)
        self.sauvegarder(self.services_file, salon.services)
        self.sauvegarder(self.rendezvous_file, salon.rendezvous)

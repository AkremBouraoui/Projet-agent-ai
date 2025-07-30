from data_manager import class_data_manager

class class_salon:
    def __init__(self, nom):
        self.nom = nom
        self.data_manager = class_data_manager()
        self.clients = self.data_manager.charger_clients()
        self.coiffeurs = self.data_manager.charger_coiffeurs()
        self.services = self.data_manager.charger_services()
        self.rendezvous = self.data_manager.charger_rendezvous()

    def ajouter_client(self, client):
        self.clients.append(client)
        self.data_manager.sauvegarder(self.data_manager.clients_file, self.clients)

    def ajouter_coiffeur(self, coiffeur):
        self.coiffeurs.append(coiffeur)
        self.data_manager.sauvegarder(self.data_manager.coiffeurs_file, self.coiffeurs)

    def ajouter_service(self, service):
        self.services.append(service)
        self.data_manager.sauvegarder(self.data_manager.services_file, self.services)

    def ajouter_rendezvous(self, rdv):
        self.rendezvous.append(rdv)
        self.data_manager.sauvegarder(self.data_manager.rendezvous_file, self.rendezvous)

    def lister_services(self):
        return "\n".join([f"{s.id_service}. {s.nom_service} - {s.prix}$" for s in self.services])

    def lister_coiffeurs(self):
        return "\n".join([f"{c.id_coiffeur}. {c.nom} - {c.specialite}" for c in self.coiffeurs])

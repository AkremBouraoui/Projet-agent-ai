<img width="809" height="452" alt="1" src="https://github.com/user-attachments/assets/9d366a3e-8361-4c3a-ab9b-1553729ea314" />



1- Agent AI – Salon de Coiffure Intelligent :

Notre projet consiste à développer un agent intelligent capable de communiquer avec les utilisateurs pour gérer les services d’un salon de coiffure.
Cet agent est accessible via une interface web moderne et permet :
- La prise de rendez-vous
- La consultation des services et des coiffeurs
- La gestion des données (ajout, modification, suppression)



2- Objectifs du projet :

- Automatiser la communication avec les clients
- Faciliter la gestion des rendez-vous
- Offrir une expérience interactive grâce à un Agent AI
- Gérer dynamiquement les entités du salon : clients, coiffeurs, services, etc.



3- Structure du projet :

<img width="425" height="553" alt="2" src="https://github.com/user-attachments/assets/41f000c2-901e-403e-b647-c855242cf211" />





4- Diagramme de classes UML :

<img width="1018" height="893" alt="image" src="https://github.com/user-attachments/assets/8dbfd014-afda-4618-96c9-fc77581bef53" />



Ce diagramme représente la structure orientée objet de notre application « Agent AI ». Il permet de visualiser les entités principales du système, leurs attributs, leurs méthodes, ainsi que les relations entre elles.

- Classe AgentAI : 
C’est l’agent intelligent du système. Il communique avec l’utilisateur, comprend ses demandes, et agit en conséquence.

Attributs :
nom : le nom de l’agent.
salon : une instance de la classe Salon.
etat : l’état actuel de l’agent (ex : “attente”, “réservation”...).
memoire : pour stocker temporairement les informations du dialogue.

Méthode :
discuter(message) : permet de traiter les messages et d’y répondre.

- Classe Salon :
Elle représente le salon de coiffure. C’est le cœur du système, qui contient toutes les données.

Attributs :
nom : le nom du salon.
clients, coiffeurs, services, rendezvous : des listes qui contiennent les entités correspondantes.

Méthodes :
ajouter_client(), ajouter_coiffeur(), ajouter_service(), ajouter_rendezvous() : pour ajouter des éléments.
lister_clients(), lister_coiffeurs(), lister_services(), lister_rendezvous() : pour les afficher.

- Classe RendezVous :
Elle représente un rendez-vous entre un client et un coiffeur, pour un service donné.

Attributs :
id_rendezvous, date, heure
id_client, id_service, id_coiffeur : références aux autres entités.

- Classe Client :
Elle représente un client du salon.

Attributs :
id_client, nom, téléphone

- Classe Coiffeur : 
Elle représente un coiffeur travaillant dans le salon.

Attributs :
id_coiffeur, nom, spécialité

- Classe Service :
Elle représente un service proposé (ex : coupe, barbe...).

Attributs :
id_service, nom_service, prix
........

Les relations :
- L’AgentAI contrôle le Salon.
- Le Salon gère plusieurs clients, coiffeurs, services et rendez-vous.
- Un RendezVous relie un Client, un Coiffeur et un Service.





5-Fonctionnement de l’Agent AI :

- L’agent intelligent agit comme un assistant virtuel pour le salon de coiffure.
Il traite les messages des utilisateurs en analysant leur intention (prise, modification ou suppression de rendez-vous),
Selon l’état de la conversation, il guide l’utilisateur étape par étape (nom, téléphone, service, coiffeur, date, heure…).
Une fois toutes les informations collectées, il crée un client et enregistre un rendez-vous dans le système.
En cas de message général (sans mots-clés), il utilise l’API OpenAI pour répondre de manière naturelle et contextuelle.
Cela permet une interaction fluide, intelligente et personnalisée avec chaque utilisateur.





6- Technologies utilisées :

- Python (Flask) pour le backend
- HTML / CSS pour l’interface 
- GitHub pour la gestion de version
- JSON pour la persistance des données
- VS Code comme environnement de développement 




7- Données JSON :

Toutes les données sont sauvegardées en local dans des fichiers :
- clients.json
- coiffeurs.json
- services.json
- rendezvous.json
Aucune base de données externe n’est utilisée (stockage en mémoire locale).




8- Code source :

Les technologies utilisées :
- Python (Flask)
- HTML / CSS (interface utilisateur)
- JSON (données)
- OpenAI API (optionnel) 
- GitHub (versioning)





9- Conclusion :

- En résumé, ce projet met en œuvre une solution intelligente pour la gestion d’un salon de coiffure.
- Grâce à l’agent AI, l’utilisateur interagit facilement pour réserver, modifier ou supprimer un rendez-vous.
- Le système repose sur une architecture claire basée sur les classes, les fichiers JSON et une interface web.
- Le projet respecte les bonnes pratiques de programmation en Python.
- L’ajout de l’intelligence artificielle améliore considérablement l’expérience utilisateur.
- C’est une application simple, efficace et extensible.

Accéder à l’interface : Ouvrir votre navigateur sur http://127.0.0.1:5000

<img width="1366" height="697" alt="Capture" src="https://github.com/user-attachments/assets/05bcdd42-3fc2-407b-a08f-64129d8d6fe2" />
















💈 Agent AI – Salon de Coiffure Intelligent :

Ce projet est un agent conversationnel intelligent pour la gestion d’un salon de coiffure. 
Il permet aux utilisateurs d’interagir naturellement afin de prendre, modifier ou annuler des rendez-vous, ainsi que consulter les services et les coiffeurs disponibles.


🎯 Objectifs du projet :

- Créer un système intelligent de prise de rendez-vous
- Simuler une vraie conversation avec un agent AI
- Proposer une interface web intuitive (HTML/CSS)
- Organiser le code autour d’entités (classes), d’un gestionnaire de données et d’un agent


🧠 Fonctionnalités principales :

- 🤖 Agent AI intelligent (avec ou sans l’API OpenAI)
- 📅 Prise, modification et suppression de rendez-vous
- 💇‍♂️ Liste des coiffeurs et leurs spécialités
- 💆‍♀️ Liste des services proposés
- 📋 Affichage des clients et de leurs rendez-vous
- 🌐 Interface web interactive (chat)
- 📁 Stockage en mémoire (pas de base de données externe)


🗂️ Structure du projet :

projet_agent_ai/
│
├── app.py (serveur Flask)
├── agent/  Contient class_agent_ai.py
├── entities/ Classes : client, coiffeur, service, rendezvous, salon
├── data_manager/ Gestion de fichiers JSON
├── templates/
│ └── chat.html Interface utilisateur
├── static/
│ └── style.css Fichier de style CSS
└── .env Clé API OpenAI (non versionnée)





Installer les dépendances :

- pip install flask openai python-dotenv
- Lancer le serveur Flask :
- python app.py



Accéder à l’interface :
Ouvrir votre navigateur sur http://localhost:5000



💬 Exemples de messages possibles :

- Bonjour
- Je veux prendre un rendez-vous
- Afficher les coiffeurs
- Afficher les services
- Modifier un rendez-vous
- Supprimer un rendez-vous


👨‍🎓 Réalisé par
Bouraoui Akrem
Nemous Abdelatif
Kahil amine






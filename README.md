<div align="center">
<img src="https://www.google.com/search?q=https://upload.wikimedia.org/wikipedia/fr/thumb/c/c3/Office_national_des_a%25C3%25A9roports_logo.svg/1200px-Office_national_des_a%25C3%25A9roports_logo.svg.png" width="150"/>
<h1>Application de Supervision des Équipements <abbr title="Very High Frequency">VHF</abbr></h1>
<p>Une solution de monitoring et de configuration à distance pour les infrastructures de communication aéronautique.</p>
<p><i>Projet réalisé dans le cadre d'un stage d'initiation au sein de l'Office National Des Aéroports (ONDA) - Aéroport Al Hoceima.</i></p>

<p>
<img src="https://img.shields.io/badge/Python-3.11%2B-blue.svg" alt="Python Version">
<img src="https://img.shields.io/badge/Framework-PySide6-orange.svg" alt="Framework">
<img src="https://img.shields.io/badge/Database-MySQL-blue.svg" alt="Database">
<img src="https://img.shields.io/badge/Protocol-Modbus_RTU-red.svg" alt="Protocol">
<img src="https://img.shields.io/badge/Architecture-MVC-green.svg" alt="Architecture">
</p>
</div>

# CONTEXTE DU PROJET
> Ce projet s'inscrit dans une démarche de modernisation des outils de maintenance du **Service Technique Navigation** de l'aéroport d'Al Hoceima. Les communications <abbr title="Very High Frequency">VHF</abbr> entre la tour de contrôle et les aéronefs sont un pilier de la sécurité aérienne, reposant sur des équipements Telerad robustes mais dont la supervision est restée manuelle.  

## La Problématique : De la Fiche Papier au Temps Réel
> Jusqu'à présent, la vérification des paramètres critiques des équipements <abbr title="Very High Frequency">VHF</abbr> (température, puissance, ROS, etc.) s'effectuait physiquement dans la salle technique, avec un relevé manuel sur des fiches de contrôle.
**Cette méthode présentait plusieurs limitations :**

- **Lenteur** : Un temps de réaction élevé en cas d'anomalie;

- **Manque de vision globale** : Absence de centralisation des données et de vue d'ensemble;

- **Absence d'historique** : Difficulté à analyser les pannes passées et à identifier des tendances.

## La Solution : Une Supervision Centralisée et Intelligente
> Cette application a été conçue pour répondre à ces enjeux en offrant une plateforme de supervision centralisée, temps réel et intelligente. Elle permet aux techniciens et ingénieurs de :

- **Superviser** l'état de tous les équipements <abbr title="Very High Frequency">VHF</abbr> depuis un seul poste;

- **Configurer** à distance les paramètres de fonctionnement;

- **Recevoir des alertes** sonores et visuelles instantanées en cas de défaillance ou d'anomalie;

- **Analyser** l'historique des données pour une maintenance proactive.

# APERÇU DE L'INTERFACE
> L'interface a été conçue pour être intuitive, claire et adaptée à un environnement technique, en s'inspirant des systèmes de supervision modernes.

  * *(Image inspirée de la maquette Page d'authentification.png)*

<div align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/GZ5fE7C.png" alt="Aperçu de l'authentification de l'application"/>
</div>

  * *(Image inspirée de la maquette ONDA - Dashboard.png)*

<div align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/GZ5fE7C.png" alt="Aperçu du Dashboard de l'application"/>
</div>

  * *(Image inspirée de la maquette ONDA - Emetteur.png)*

<div align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/GZ5fE7C.png" alt="Aperçu de l'Emetteur de l'application"/>
</div>

  * *(Image inspirée de la maquette ONDA - Récepteur VHF.png)*

<div align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/GZ5fE7C.png" alt="Aperçu du Récepteur de l'application"/>
</div>

  * *(Image inspirée de la maquette ONDA - Basculeur.png)*

<div align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/GZ5fE7C.png" alt="Aperçu du Basculeur de l'application"/>
</div>

  * *(Image inspirée de la maquette ONDA - Historique et Rapports.png)*

<div align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/GZ5fE7C.png" alt="Aperçu de l'Historique de l'application"/>
</div>

# FONCTIONNALITÉS CLÉS
> L'application est structurée en plusieurs modules accessibles depuis un menu latéral :

  - 📊 **Tableau de Bord Principal :** Vue d'ensemble de l'état du système, des alertes en cours et des indicateurs de performance clés (<abbr title="Key Performance Indicator">KPIs</abbr>);

  - 📡 **Module Émetteur (Tx) :** Supervision et configuration des émetteurs Telerad EM9000;

    - **Supervision :** Fréquence, Puissance (W), <abbr title="Rapport d'Ondes Stationnaires">ROS</abbr>, Température (°C), Taux de Modulation (%), Tension (V);

    - **Configuration :** Modification de la fréquence, réglage de la puissance, Modifier <abbr title="Taux De Modulation">TDM</abbr>, activation/désactivation.

  - 📻 **Module Récepteur (Rx) :** Supervision et configuration des récepteurs Telerad RE9000;

    - **Supervision :** Fréquence, Température (°C), Tension (V), Puissance <abbr title="Basse Fréquence">BF</abbr> (dBm), Seuil et état du Squelch, Tension (V);

    - **Configuration :** Changement de fréquence, ajustement du Squelch.

  - 🔄 **Module Basculeur (N/S) :** Gestion de la redondance avec le Telerad BNS 9008;

    - **Supervision :** Voie active (Principal/Secours), Mode (Auto/Manuel), Cause du dernier basculement;

    - **Configuration :** Forcer le basculement manuel, activer/désactiver le mode automatique.

  - 📈 **Historique & Rapports :** Consultation des événements passés avec des filtres (par date, type d'alerte, équipement) et exportation des données en format PDF/Excel.

# ARCHITECTURE TECHNIQUE
> L'application est construite sur le patron d'architecture **(**<abbr title="Modèle-Vue-Contrôleur">**MVC**</abbr>**)**, garantissant une séparation nette entre la logique métier, l'interface utilisateur et la gestion des données.

  - **Modèle (Model) :** Contient la logique métier, l'état des équipements, et gère la communication avec la base de données et les équipements via Modbus;

  - **Vue (View) :** L'interface graphique construite avec PySide6. Elle est passive et se contente d'afficher les informations du modèle et de capturer les actions de l'utilisateur;

  - **Contrôleur (Controller) :** Fait le lien entre la Vue et le Modèle. Il traite les actions de l'utilisateur et met à jour le modèle, qui à son tour notifie la vue des changements.

## Technologies Utilisées

| Composant                | Technologie                     | Rôle                                                                 |
|--------------------------|----------------------------------|----------------------------------------------------------------------|
| Interface Graphique      | PySide6 (Qt for Python)         | Création d'une application de bureau native et performante.          |
| Logique & Contrôle       | Python 3.11+                    | Langage principal pour sa simplicité et son écosystème riche.        |
| Base de Données          | MySQL                           | Stockage persistant des utilisateurs, alertes et historique.         |
| Communication Matérielle | pymodbus                        | Implémentation Modbus RTU (J-BUS) via RS-485.                        |
| Asynchronisme            | qasync & asyncio                | Permet d'exécuter les tâches longues (requêtes réseau) sans jamais bloquer l'interface utilisateur.   |

# 🚀 INSTALLATION ET LANCEMENT
Suivez ces étapes pour lancer l'application en mode développement avec le simulateur.

  1. **Prérequis**

      - **Python 3.10+** (Version 3.13.7 recommandée pour ce projet);

      - Un serveur **MySQL** (ou MariaDB) fonctionnel et accessible;

      - **Git** pour cloner le projet.

  2. **Installation**

            # 1. Cloner le dépôt du projet sur votre machine locale
            git clone [https://votre-lien-vers-le-projet.git](https://votre-lien-vers-le-projet.git)
            cd votre-projet

            # 2. Créer un environnement virtuel pour isoler les dépendances du projet
            # C'est une bonne pratique pour éviter les conflits de versions.
            python -m venv venv

            # 3. Activer l'environnement virtuel
            # Sur Windows :
            venv\Scripts\activate
            # Sur macOS/Linux :
            source venv/bin/activate

            # 4. Installer toutes les bibliothèques Python nécessaires en une seule commande
            pip install -r requirements.txt

  3. **Configuration de la Base de Données**
  Avant de lancer l'application, la base de données `supervision_vhf` doit être créée et peuplée.

            # Connectez-vous à votre serveur MySQL en ligne de commande.
            # Remplacez 'votre_utilisateur_mysql' par votre nom d'utilisateur MySQL.
            mysql -u votre_utilisateur_mysql -p

            # Une fois connecté, exécutez les commandes suivantes pour créer la base
            # et l'utilisateur dédiés à l'application. Remplacez 'Onda@123'.
            CREATE DATABASE supervision_vhf;
            CREATE USER 'supervision_user'@'localhost' IDENTIFIED BY 'Onda@123';
            GRANT ALL PRIVILEGES ON supervision_vhf.* TO 'supervision_user'@'localhost';
            FLUSH PRIVILEGES;
            EXIT;

            # Maintenant, importez la structure des tables depuis les fichiers .sql fournis.
            # Assurez-vous d'exécuter ces commandes depuis la racine de votre projet.
            mysql -u supervision_user -p supervision_vhf < database/supervision_vhf_users.sql
            mysql -u supervision_user -p supervision_vhf < database/supervision_vhf_emetteurs.sql
            mysql -u supervision_user -p supervision_vhf < database/supervision_vhf_recepteurs.sql
            mysql -u supervision_user -p supervision_vhf < database/supervision_vhf_basculeurs.sql
            mysql -u supervision_user -p supervision_vhf < database/supervision_vhf_alertes.sql
            mysql -u supervision_user -p supervision_vhf < database/supervision_vhf_historique.sql

      **Alternative :** Vous pouvez également utiliser un outil graphique comme **MySQL Workbench** ou **DBeaver** pour exécuter le contenu de chaque fichier `.sql` du dossier `database/` directement dans l'éditeur de requêtes.

  4. **Configuration de l'Environnement**
  Pour des raisons de sécurité, les informations sensibles comme les identifiants de la base de données ne sont pas stockées directement dans le code.

      1. **Créez un fichier** `.env` à la racine du projet (au même niveau que `main.py`);
      2. **Copiez-collez le contenu suivant** dans votre fichier `.env` et adaptez les valeurs à votre configuration :

                # Fichier .env - Configuration de l'environnement

                # --- Base de données ---
                DB_HOST=localhost
                DB_PORT=3306
                DB_NAME=supervision_vhf
                DB_USER=supervision_user
                DB_PASSWORD=Onda@123

                # --- Simulateur Modbus ---
                SIMULATOR_HOST=localhost
                SIMULATOR_PORT=5020

  5. **Lancement de l'Application**
  L'application fonctionne avec un simulateur Modbus pour permettre le développement sans matériel physique.

            # 1. Dans un premier terminal (avec l'environnement virtuel activé),
            # lancez le simulateur d'équipements. Il restera en attente de connexions.
            python simulateur_modbus.py

            # 2. Dans un second terminal (avec l'environnement virtuel également activé),
            # lancez l'application principale.
            python main.py

      Identifiants de connexion par défaut : `admin` / `admin`

# AUTEUR
**Ilyas BEL EL YAZID** - Étudiant Ingénieur en Transformation Digitale & Intelligence Artificielle.

*Ce projet a été réalisé sous l'encadrement de M. Mohamed OUKHATTOU et M. Abdelmoula HAOUZI BAHI (<abbr title="Office National Des Aéroports">ONDA</abbr>).*

# Contact
Pour toute question, n'hésitez pas à m'écrire à belelyazidilyas@gmail.com.

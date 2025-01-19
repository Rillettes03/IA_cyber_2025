# Détection d'Anomalies dans les Logs avec Machine Learning

Ce projet a pour objectif de détecter les anomalies dans les logs systèmes en utilisant une Intelligence Artificielle. Il s'appuie sur un cluster ElasticSearch pour la collecte, le stockage et l'analyse des logs, ainsi qu'un script Python pour l'entraînement et l'évaluation d'un modèle d'IA.

---

## Table des Matières
1. [Prérequis](#prérequis)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Pipeline de Traitement des Logs](#pipeline-de-traitement-des-logs)
5. [Entraînement de l'IA](#entraînement-de-lia)
6. [Utilisation](#utilisation)
7. [Contributions](#contributions)

---

## Prérequis
Tout d'abord, si t'as pas Windows, ça va pas fonctionner.

Avant de commencer, assurez-vous d'avoir installé les outils suivants :

- **Python 3.8+** : Pour exécuter les scripts d'extraction et d'entraînement de l'IA.

---

## Architecture

Voici les principaux composants du projet :

1. **Collecte des Logs** : Les logs sont envoyés vers Logstash, où ils sont parsés et nettoyés.
2. **Indexation dans ElasticSearch** : Les logs nettoyés sont indexés dans ElasticSearch pour un accès rapide.
3. **Extraction des Logs** : Un script Python récupère les logs depuis ElasticSearch et les convertit en format JSON pour l'entraînement de l'IA.
4. **Entraînement de l'IA** : Les données JSON sont utilisées pour entraîner un modèle de machine learning capable d'identifier les anomalies.
5. **Détection en Temps Réel** : Une fois entraînée, l'IA retourne un score de dangerosité (entre 0 et 1) pour chaque log envoyé.

---

## Installation

1. Clonez le dépôt :
   ```bash
   git clone [https://github.com/Rillettes03/IA_cyber_2025.git](https://github.com/Rillettes03/IA_cyber_2025.git)

## Pipeline de Traitement des Logs

Les logs bruts sont collectés, parsés et nettoyés avec Logstash avant d’être envoyés dans ElasticSearch, où ils sont indexés pour un accès rapide et structuré. Cela permet d’utiliser ces données comme base pour l’entraînement du modèle d’intelligence artificielle.

Étape 1 : Parsing et Nettoyage
Logstash est utilisé pour parser les logs bruts, supprimer les champs inutiles et normaliser les données.
Les logs nettoyés sont envoyés dans un index ElasticSearch dédié.

Étape 2 : Indexation
Les logs normalisés sont indexés dans ElasticSearch, rendant les données accessibles via des requêtes.

## Entraînement de l'IA

Le script `recup_log.py` récupère les logs des index ElasticSearch et les sauvegarde sous forme de fichiers JSON.

Le script `train.py` lit les fichiers JSON (1 malicieux et 1 normal), afin d'entraîner le modèle et sauvegarde le modèle entraîné dans le home de l'utilisateur.
Les logs ont permis d'entrainer l'IA à reconnaître les logs malicieux ou non.

## Utilisation

On lance le script `detect.py` en lui précisant le chemin vers le log (format json) que l'on souhaite auditer.
Ce script renvoit une string précisant si le log est malicieux ou non. S'il est malicieux, il renvoit le log en plus.

Le modèle retourne un score entre 0 et 1, où :
0 : Aucun danger.
1 : Danger critique.

## Contributions
On a 
- Victor Cissay à l'entrainement de l'IA
- Sacha Bando à Reddit
- Paul Terrien comme auditeur logstach
- Aurore Lépine en arbitrage









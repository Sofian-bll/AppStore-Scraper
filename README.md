# App Store Price Scraper v2

> Note: Au moment de ce projet, j'étais à ma 2e semaine d'apprentissage de Python.

Un outil complet de scraping des prix du App Store d'Apple, permettant de collecter et analyser les prix des achats
intégrés à travers différents pays et devises.

## 📋 Description du Projet

Ce projet permet de récupérer automatiquement les prix des achats intégrés (in-app purchases) depuis l'App Store d'Apple
pour différentes applications et régions géographiques. Il inclut également des fonctionnalités de conversion de devises
pour normaliser les données en euros.

## 🗂️ Structure du Projet

### Fichiers Python

#### `request.py` - Script Original

**🏗️ Codé entièrement par l'auteur de A à Z en Python**

Ce fichier est le script original, développé entièrement à la main par l'auteur du projet. Il s'agit de la première
version qui permet de :

- Se connecter à l'API Apple App Store
- Récupérer les données d'achats intégrés pour une application spécifique
- Gérer les erreurs de base (applications non disponibles dans certains pays)
- Afficher les prix formatés dans la console

**Fonctionnalités principales :**

- Configuration des headers et paramètres d'API
- Support de base pour différents codes pays
- Extraction des noms et prix des achats intégrés
- Gestion d'erreurs avec affichage des détails

#### `Request2.py` - Version Améliorée avec Directives IA

**🤖 Version améliorée développée avec les directives données à l'IA**

Cette version est une amélioration significative du script original, développée avec l'aide et les directives de l'IA.
Elle inclut :

- Support étendu pour 36 pays différents
- Export automatique des données en format CSV
- Barre de progression en temps réel
- Meilleure gestion d'erreurs et robustesse
- Stockage organisé des données

**Améliorations apportées :**

- Liste complète de 36 codes pays internationaux
- Export CSV avec colonnes structurées (country, name, price, price_formatted, currency)
- Interface utilisateur améliorée avec progression visuelle
- Gestion plus robuste des erreurs et des cas limites
- Architecture plus modulaire et maintenable

#### `price_converter.py` - Convertisseur de Devises

**🤖 Script créé avec les directives données à l'IA**

Ce script a été développé entièrement avec les directives fournies à l'IA pour ajouter des fonctionnalités de conversion
de devises. Il permet de :

- Convertir automatiquement tous les prix en euros
- Utiliser une API de taux de change en temps réel
- Traiter les fichiers CSV générés par Request2.py
- Fournir des rapports détaillés de conversion

**Caractéristiques techniques :**

- Classe `CurrencyConverter` avec cache des taux de change
- API Exchange Rate gratuite pour les conversions
- Traitement par lots avec gestion d'erreurs
- Rapports de progression et statistiques de conversion
- Sauvegarde automatique des résultats

### Données CSV

Le dossier `App Price/` contient les résultats d'extraction de prix :

- **`Chat-Gpt Price.csv`** - Données de prix pour ChatGPT
- **`Claude Price.csv`** - Données de prix pour Claude
- **`Raycast Price.csv`** - Données de prix pour Raycast (avec conversion EUR)

## 🚀 Utilisation

### Prérequis

```bash
pip install requests pandas
```

### Exécution du Scraper de Base

```bash
python request.py
```

Ce script affichera les prix dans la console pour un pays et une application spécifiés.

### Exécution du Scraper Avancé

```bash
python Request2.py
```

Ce script générera un fichier CSV avec tous les prix collectés pour les 36 pays supportés.

### Conversion des Devises

```bash
python price_converter.py
```

Ce script lira le fichier CSV généré et ajoutera une colonne avec les prix convertis en euros.

## ⚙️ Configuration

### Modification des Applications Cibles

Pour scraper une application différente, modifiez la variable `app_id` dans les fichiers :

- `request.py` : ligne 36
- `Request2.py` : ligne 37

### Ajout de Nouveaux Pays

Dans `Request2.py`, vous pouvez modifier la liste `country_codes` (lignes 38-42) pour ajouter ou retirer des pays.

### Personnalisation de la Devise de Conversion

Dans `price_converter.py`, vous pouvez changer la devise cible en modifiant le paramètre `to_currency` dans les
fonctions de conversion.

## 🔧 Détails Techniques

### API Utilisée

- **Apple App Store API** : `https://amp-api-edge.apps.apple.com/v1/catalog/{country}/apps/{app_id}`
- **Exchange Rate API** : `https://api.exchangerate-api.com/v4/latest`

### Authentification

Le projet utilise un token Bearer pour l'authentification avec l'API Apple (token inclus dans les headers).

### Gestion des Erreurs

- Gestion des applications non disponibles dans certains pays
- Timeout et retry pour les appels API
- Validation des données avant export CSV
- Cache des taux de change pour optimiser les performances

## 📊 Format des Données de Sortie

Le fichier CSV généré contient les colonnes suivantes :

- `country` : Code pays (ex: "us", "fr", "de")
- `name` : Nom de l'achat intégré
- `price` : Prix numérique
- `price_formatted` : Prix formaté avec devise
- `currency` : Code de devise (ex: "USD", "EUR")
- `price_eur` : Prix converti en euros (ajouté par price_converter.py)

## 🏆 Évolution du Projet

1. **Version 1** (`request.py`) - Script original développé à la main
2. **Version 2** (`Request2.py`) - Améliorations majeures avec aide IA
3. **Extension** (`price_converter.py`) - Fonctionnalités de conversion ajoutées

## 📝 Notes Importantes

- Les tokens d'authentification peuvent expirer et nécessiter une mise à jour
- L'API Exchange Rate gratuite a des limites de requêtes
- Certaines applications peuvent ne pas être disponibles dans tous les pays
- Les prix peuvent varier selon les régions pour la même application

## 👤 Auteur

- **Script original** (`request.py`) : Développé entièrement à la main par l'auteur
- **Améliorations** (`Request2.py`, `price_converter.py`) : Développées avec l'assistance et les directives données à l'
  IA

---

*Dernière mise à jour : Octobre 2025*
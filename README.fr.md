<div align="center">

[![Licence: MIT](https://img.shields.io/github/license/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/releases)
[![Stars](https://img.shields.io/github/stars/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/stargazers)
<br>
![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/requests-%23000000.svg?style=flat&logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-%23FF6B6B.svg?style=flat&logo=fastapi&logoColor=white)

> [Read in English](README.md) | [Lire en Francais](README.fr.md)

</div>

<p align="center">
  <img src="docs/assets/logo.png" alt="Logo App Store Price Scraper" width="160"/>
</p>

# App Store Price Scraper

Collecte et analyse les prix des achats in-app depuis l'App Store d'Apple a travers 36 pays et 30+ devises — avec conversion en euros en temps reel.

## C'est quoi ?

Un outil Python qui scrape les prix des achats in-app depuis l'API de l'App Store d'Apple pour n'importe quelle application, dans 36 pays. Il exporte des donnees structurees en CSV et inclut une conversion en euros en temps reel via l'Exchange Rate API.

> Developpe pendant ma 2eme semaine d'apprentissage de Python — du prototype code main au projet multi-couches assiste par IA.

## Fonctionnalites

- **36 pays** — Couverture de toutes les regions majeures de l'App Store (US, UE, Asie, Moyen-Orient)
- **Export CSV** — Sortie structuree avec les colonnes pays, nom, prix et devise
- **Conversion de devises** — Conversion en euros en temps reel avec taux de change live et cache
- **Barre de progression** — Suivi en temps reel pendant les operations de scraping

## Demarrage rapide

```bash
# Installer les dependances
pip install -r requirements.txt

# Scraper les achats in-app pour 36 pays (modifier app_id dans Request2.py)
python Request2.py

# Convertir les prix en euros
python price_converter.py
```

## Fichiers & Attribution

| Fichier | Auteur | Description |
|---------|--------|-------------|
| `request.py` | Code main integral | V1 originale — scraper mono-pays avec sortie console |
| `Request2.py` | Assiste par IA (directives humaines) | V2 amelioree — 36 pays, export CSV, barre de progression |
| `price_converter.py` | Assiste par IA (directives humaines) | Conversion de devises en EUR avec taux live et cache |

## Evolution du projet

1. **V1** (`request.py`) — Script original, entierement code main par l'auteur
2. **V2** (`Request2.py`) — Ameliorations majeures avec l'IA : multi-pays, export CSV, suivi de progression
3. **Extension** (`price_converter.py`) — Couche de conversion de devises ajoutee avec l'IA

## Structure du projet

```
.
├── App Price/              # Donnees CSV de sortie
│   ├── Chat-Gpt Price.csv
│   ├── Claude Price.csv
│   └── Raycast Price.csv
├── docs/                   # Documentation et page d'accueil
│   └── assets/
│       └── logo.png
├── LICENSE
├── README.md
├── README.fr.md
├── Request2.py             # Scraper multi-pays ameliore (v2)
├── price_converter.py      # Conversion de devises en EUR
├── request.py              # Scraper mono-pays original (v1)
└── requirements.txt
```

## Configuration

Modifier `app_id` dans `Request2.py` (ligne 37) pour cibler une autre application. Modifier `country_codes` (lignes 38-42) pour ajouter ou retirer des pays. Dans `price_converter.py`, changer `to_currency` pour convertir vers une autre devise cible.

## Format de sortie

Colonnes CSV : `country`, `name`, `price`, `price_formatted`, `currency`, `price_eur` (ajoute par price_converter.py).

## Auteur

- **Script original** (`request.py`) : Entierement developpe a la main
- **Ameliorations** (`Request2.py`, `price_converter.py`) : Developpees avec assistance IA et directives humaines

## Licence

MIT — voir [LICENSE](LICENSE) pour plus de details.

---

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Sofian-bll/AppStore-Scraper&type=Date)](https://star-history.com/#Sofian-bll/AppStore-Scraper&Date)

</div>

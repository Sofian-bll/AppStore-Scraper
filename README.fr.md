<div align="center">

[![License: MIT](https://img.shields.io/github/license/Sofian-bll/AppStore-Scraper?style=for-the-badge)](https://github.com/Sofian-bll/AppStore-Scraper/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/Sofian-bll/AppStore-Scraper?style=for-the-badge)](https://github.com/Sofian-bll/AppStore-Scraper/releases)
[![Stars](https://img.shields.io/github/stars/Sofian-bll/AppStore-Scraper?style=for-the-badge)](https://github.com/Sofian-bll/AppStore-Scraper/stargazers)

> [Read in English](README.md) | [Lire en Francais](README.fr.md)

</div>

<p align="center">
  <img src="docs/assets/logo.png" alt="Logo App Store Price Scraper" width="160"/>
</p>

# App Store Price Scraper

Collectez et analysez les prix des achats integres du App Store d'Apple a travers differents pays et devises.

## C'est quoi ?

Un outil Python qui recupere les donnees de prix des achats integres depuis l'API App Store d'Apple pour n'importe quelle application, dans 36 pays. Il exporte les donnees en CSV structure et inclut la conversion des devises en euros en temps reel.

> Note: Au moment de ce projet, j'etais a ma 2e semaine d'apprentissage de Python.

## Fichiers et Attribution

| Fichier | Auteur | Description |
|---------|--------|-------------|
| `request.py` | Code entierement a la main | V1 originale — scraper mono-pays avec affichage console |
| `Request2.py` | Assiste par IA (directives humaines) | V2 amelioree — 36 pays, export CSV, barre de progression |
| `price_converter.py` | Assiste par IA (directives humaines) | Conversion de devises en EUR avec taux de change en direct et cache |

## Evolution du Projet

1. **V1** (`request.py`) — Script original, developpe entierement a la main par l'auteur
2. **V2** (`Request2.py`) — Ameliorations majeures avec l'aide de l'IA : multi-pays, CSV, progression
3. **Extension** (`price_converter.py`) — Couche de conversion de devises ajoutee avec l'assistance IA

## Demarrage Rapide

```bash
# Installer les dependances
pip install -r requirements.txt

# Scraper les achats integres pour 36 pays (modifier app_id dans Request2.py)
python Request2.py

# Convertir les prix en euros
python price_converter.py
```

## Structure du Projet

```
.
├── App Price/              # Donnees CSV de sortie
│   ├── Chat-Gpt Price.csv
│   ├── Claude Price.csv
│   └── Raycast Price.csv
├── docs/                   # Documentation et site
│   └── assets/
│       └── logo.png
├── LICENSE
├── README.md
├── README.fr.md
├── Request2.py             # Scraper multi-pays ameliore (v2)
├── price_converter.py      # Conversion de devises en EUR
├── request.py              # Scraper original mono-pays (v1)
└── requirements.txt
```

## Configuration

Modifiez `app_id` dans `Request2.py` (ligne 37) pour cibler une autre application. Modifiez `country_codes` (lignes 38-42) pour ajouter ou retirer des pays. Dans `price_converter.py`, changez `to_currency` pour convertir vers une autre devise cible.

## Format de Sortie

Colonnes CSV : `country`, `name`, `price`, `price_formatted`, `currency`, `price_eur` (ajoute par price_converter.py).

## Auteur

- **Script original** (`request.py`): Developpe entierement a la main
- **Ameliorations** (`Request2.py`, `price_converter.py`): Developpees avec l'assistance IA et des directives humaines

## Licence

MIT — voir [LICENSE](LICENSE) pour plus de details.

---

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Sofian-bll/AppStore-Scraper&type=Date)](https://star-history.com/#Sofian-bll/AppStore-Scraper&Date)

</div>

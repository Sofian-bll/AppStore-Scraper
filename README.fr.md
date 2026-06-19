<div align="center">

[![Licence: MIT](https://img.shields.io/github/license/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/releases)
[![Stars](https://img.shields.io/github/stars/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/stargazers)

<p align="center">
  <img src="docs/assets/logo.png" alt="Logo App Store Price Scraper" width="160"/>
</p>

<a id="readme-top"></a>
<h1 align="center">App Store Price Scraper</h1>

<p align="center">Collecte et analyse les prix des achats in-app depuis l'App Store d'Apple a travers 36 pays et 30+ devises — avec conversion en euros en temps reel.</p>

<p align="center">🇬🇧 <a href="README.md">English</a> · 🇫🇷 <a href="README.fr.md"><b>Français</b></a></p>

[Explorer la doc](docs/) · [Signaler un bug](https://github.com/Sofian-bll/AppStore-Scraper/issues) · [Proposer une fonctionnalite](https://github.com/Sofian-bll/AppStore-Scraper/issues)

</div>

<details open>
  <summary>Table des matieres</summary>
  <ol>
    <li><a href="#cest-quoi-">C'est quoi ?</a></li>
    <li><a href="#comment-ca-marche">Comment ca marche</a></li>
    <li><a href="#construit-avec">Construit avec</a></li>
    <li><a href="#demarrage-rapide">Demarrage rapide</a></li>
    <li><a href="#structure-du-projet">Structure du projet</a></li>
    <li><a href="#documentation">Documentation</a></li>
    <li><a href="#evolution-du-projet">Evolution du projet</a></li>
    <li><a href="#configuration">Configuration</a></li>
    <li><a href="#format-de-sortie">Format de sortie</a></li>
    <li><a href="#contribuer">Contribuer</a></li>
    <li><a href="#auteur">Auteur</a></li>
    <li><a href="#licence">Licence</a></li>
  </ol>
</details>

## C'est quoi ?

Un outil Python qui scrape les prix des achats in-app depuis l'API de l'App Store d'Apple pour n'importe quelle application, dans 36 pays. Il exporte des donnees structurees en CSV et inclut une conversion en euros en temps reel via l'Exchange Rate API.

> Developpe pendant ma 2eme semaine d'apprentissage de Python — du prototype code main au projet multi-couches assiste par IA.

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Comment ca marche

```mermaid
graph LR
    A[App Store API] --> B(request.py<br/>Scraper v1)
    A --> C(Request2.py<br/>Scraper v2)
    B --> D[CSV Output]
    C --> D
    D --> E(price_converter.py<br/>Conversion EUR)
    E --> F[CSV Final]
```

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Construit avec

- [![Python][python-shield]](https://www.python.org/) — Langage principal
- [![Pandas][pandas-shield]](https://pandas.pydata.org/) — Manipulation de donnees et export CSV
- [![Requests][requests-shield]](https://requests.readthedocs.io/) — Client HTTP pour l'API App Store
- [![API][api-shield]](https://www.exchangerate-api.com/) — Conversion de devises en temps reel

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Demarrage rapide

```bash
# Installer les dependances
pip install -r requirements.txt

# Scraper les achats in-app pour 36 pays (modifier app_id dans Request2.py)
python Request2.py

# Convertir les prix en euros
python price_converter.py
```

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

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

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Documentation

| Fichier | Description |
|---------|-------------|
| [`request.py`](request.py) | V1 originale — scraper mono-pays avec sortie console. Code main integral. |
| [`Request2.py`](Request2.py) | V2 amelioree — 36 pays, export CSV, barre de progression. Assiste par IA avec directives humaines. |
| [`price_converter.py`](price_converter.py) | Conversion de devises en EUR avec taux de change live et cache. Assiste par IA avec directives humaines. |

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Evolution du projet

1. **V1** (`request.py`) — Script original, entierement code main par l'auteur
2. **V2** (`Request2.py`) — Ameliorations majeures avec l'IA : multi-pays, export CSV, suivi de progression
3. **Extension** (`price_converter.py`) — Couche de conversion de devises ajoutee avec l'IA

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Configuration

| Variable | Fichier | Ligne | Description |
|----------|---------|-------|-------------|
| `app_id` | `Request2.py` | 37 | ID de l'app a scraper |
| `country_codes` | `Request2.py` | 38-42 | Pays a interroger |
| `to_currency` | `price_converter.py` | – | Devise cible (defaut : EUR) |

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Format de sortie

| Colonne | Source | Description |
|---------|--------|-------------|
| `country` | `Request2.py` | Nom du pays |
| `name` | `Request2.py` | Nom du produit |
| `price` | `Request2.py` | Prix brut (numerique) |
| `price_formatted` | `Request2.py` | Prix formate (ex. `4,99 $`) |
| `currency` | `Request2.py` | Code devise (ex. `USD`) |
| `price_eur` | `price_converter.py` | Prix converti en EUR |

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Contribuer

Les contributions sont les bienvenues. Ouvrez une issue pour discuter de ce que vous souhaitez modifier, ou soumettez une pull request directement.

<a href="https://github.com/Sofian-bll/AppStore-Scraper/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Sofian-bll/AppStore-Scraper" />
</a>

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Auteur

- **Script original** (`request.py`) : Entierement developpe a la main
- **Ameliorations** (`Request2.py`, `price_converter.py`) : Developpees avec assistance IA et directives humaines

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Licence

MIT — voir [LICENSE](LICENSE) pour plus de details.

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

---

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Sofian-bll/AppStore-Scraper&type=Date)](https://star-history.com/#Sofian-bll/AppStore-Scraper&Date)

</div>

<!-- REFERENCE LINKS -->
[python-shield]: https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54
[pandas-shield]: https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white
[requests-shield]: https://img.shields.io/badge/requests-%23000000.svg?style=flat&logo=python&logoColor=white
[api-shield]: https://img.shields.io/badge/API-%23FF6B6B.svg?style=flat&logo=fastapi&logoColor=white

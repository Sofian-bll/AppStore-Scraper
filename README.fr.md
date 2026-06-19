<div align="center">

[![Licence : MIT](https://img.shields.io/github/license/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/releases)
[![Stars](https://img.shields.io/github/stars/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/stargazers)

<p align="center">
  <img src="docs/assets/logo.png" alt="Logo App Store Price Scraper" width="160"/>
</p>

<a id="readme-top"></a>
<h1 align="center">App Store Price Scraper</h1>

<p align="center">Collecte et analyse les prix des achats intégrés de l'App Store d'Apple dans 36 pays et 30+ devises — avec conversion en euros en temps réel.</p>

<p align="center">🇬🇧 <a href="README.md">English</a> · 🇫🇷 <a href="README.fr.md"><b>Français</b></a></p>

</div>

## C'est quoi ?

Un outil Python qui extrait les prix des achats intégrés depuis l'API de l'App Store d'Apple pour n'importe quelle application, dans 36 pays. Il exporte les données en CSV structuré et inclut une conversion en euros en temps réel via l'Exchange Rate API.

> Développé durant ma 2e semaine d'apprentissage de Python — d'un prototype codé à la main à un outil multi-couches assisté par IA.

<p align="right">(<a href="#readme-top">haut de page</a>)</p>

## Fonctionnalités

- **36 pays** — interroge l'API App Store d'Apple sur 36 vitrines en une seule exécution
- **30+ devises** — capture les prix locaux dans la devise native de chaque pays
- **Export CSV** — sortie structurée avec pays, nom du produit, prix et devise par ligne
- **Conversion EUR** — conversion en temps réel avec cache des taux de change

<p align="right">(<a href="#readme-top">haut de page</a>)</p>

## Technologies

- [![Python][python-shield]](https://www.python.org/)
- [![Pandas][pandas-shield]](https://pandas.pydata.org/)
- [![Requests][requests-shield]](https://requests.readthedocs.io/)
- [![API][api-shield]](https://www.exchangerate-api.com/)

<p align="right">(<a href="#readme-top">haut de page</a>)</p>

## Démarrage rapide

```bash
# Installer les dépendances
pip install -r requirements.txt

# Extraire les achats intégrés pour 36 pays (modifier app_id dans Request2.py)
python Request2.py

# Convertir les prix en euros
python price_converter.py
```

<p align="right">(<a href="#readme-top">haut de page</a>)</p>

## Format de sortie

| Colonne | Source | Description |
|---------|--------|-------------|
| `country` | `Request2.py` | Nom du pays |
| `name` | `Request2.py` | Nom du produit |
| `price` | `Request2.py` | Prix brut (numérique) |
| `price_formatted` | `Request2.py` | Prix formaté (ex. `4,99 $`) |
| `currency` | `Request2.py` | Code devise (ex. `USD`) |
| `price_eur` | `price_converter.py` | Prix converti en EUR |

<p align="right">(<a href="#readme-top">haut de page</a>)</p>

## Évolution du projet

1. **V1** (`request.py`) — scraper simple pays, sortie console. Entièrement codé à la main durant la 2e semaine d'apprentissage de Python.
2. **V2** (`Request2.py`) — 36 pays, export CSV, barre de progression en temps réel. Assisté par IA sous direction humaine.
3. **Extension** (`price_converter.py`) — conversion EUR en temps réel avec cache. Assisté par IA, construit sur la base existante.

<p align="right">(<a href="#readme-top">haut de page</a>)</p>

## Licence

MIT — voir [LICENSE](LICENSE) pour plus de détails.

<p align="right">(<a href="#readme-top">haut de page</a>)</p>

---

<div align="center">

[![Graphique Star History](https://api.star-history.com/svg?repos=Sofian-bll/AppStore-Scraper&type=Date)](https://star-history.com/#Sofian-bll/AppStore-Scraper&Date)

</div>

<!-- LIENS DE REFERENCE -->
[python-shield]: https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54
[pandas-shield]: https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white
[requests-shield]: https://img.shields.io/badge/requests-%23000000.svg?style=flat&logo=python&logoColor=white
[api-shield]: https://img.shields.io/badge/API-%23FF6B6B.svg?style=flat&logo=fastapi&logoColor=white

<div align="center">

[![License: MIT](https://img.shields.io/github/license/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/releases)
[![Stars](https://img.shields.io/github/stars/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/stargazers)

<p align="center">
  <img src="docs/assets/logo.png" alt="App Store Price Scraper Logo" width="160"/>
</p>

<a id="readme-top"></a>
<h1 align="center">App Store Price Scraper</h1>

<p align="center">Collect and analyze in-app purchase prices from Apple's App Store across 36 countries and 30+ currencies — with real-time EUR conversion.</p>

<p align="center">🇬🇧 <a href="README.md"><b>English</b></a> · 🇫🇷 <a href="README.fr.md">Français</a></p>

</div>

## What is this?

A Python tool that scrapes in-app purchase pricing data from Apple's App Store API for any app, across 36 countries. It exports structured CSV data and includes real-time currency conversion to euros via the Exchange Rate API.

> Built during my 2nd week of learning Python — from hand-coded prototype to AI-assisted multi-layer tool.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

- **36 countries** — queries Apple's App Store API across 36 storefronts in a single run
- **30+ currencies** — captures local pricing in each country's native currency
- **CSV export** — structured output with country, product name, price, and currency per row
- **EUR conversion** — real-time exchange rate conversion with request caching

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

- [![Python][python-shield]](https://www.python.org/)
- [![Pandas][pandas-shield]](https://pandas.pydata.org/)
- [![Requests][requests-shield]](https://requests.readthedocs.io/)
- [![API][api-shield]](https://www.exchangerate-api.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Scrape in-app purchases for 36 countries (edit app_id in Request2.py)
python Request2.py

# Convert prices to euros
python price_converter.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Output Format

| Column | Source | Description |
|--------|--------|-------------|
| `country` | `Request2.py` | Country name |
| `name` | `Request2.py` | Product name |
| `price` | `Request2.py` | Raw price (numeric) |
| `price_formatted` | `Request2.py` | Formatted price (e.g. `$4.99`) |
| `currency` | `Request2.py` | Currency code (e.g. `USD`) |
| `price_eur` | `price_converter.py` | Price converted to EUR |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Evolution

1. **V1** (`request.py`) — single-country scraper with console output. Hand-coded entirely from scratch during week 2 of learning Python.
2. **V2** (`Request2.py`) — 36 countries, CSV export, real-time progress bar. AI-assisted with human direction.
3. **Extension** (`price_converter.py`) — real-time EUR conversion with request caching. AI-assisted, built on top of existing codebase.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

MIT — see [LICENSE](LICENSE) for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Sofian-bll/AppStore-Scraper&type=Date)](https://star-history.com/#Sofian-bll/AppStore-Scraper&Date)

</div>

<!-- REFERENCE LINKS -->
[python-shield]: https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54
[pandas-shield]: https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white
[requests-shield]: https://img.shields.io/badge/requests-%23000000.svg?style=flat&logo=python&logoColor=white
[api-shield]: https://img.shields.io/badge/API-%23FF6B6B.svg?style=flat&logo=fastapi&logoColor=white

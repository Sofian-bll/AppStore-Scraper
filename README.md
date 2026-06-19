<div align="center">

[![License: MIT](https://img.shields.io/github/license/Sofian-bll/AppStore-Scraper?style=flat)](https://github.com/Sofian-bll/AppStore-Scraper/blob/main/LICENSE)
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
  <img src="docs/assets/logo.png" alt="App Store Price Scraper Logo" width="160"/>
</p>

# App Store Price Scraper

Collect and analyze in-app purchase prices from Apple's App Store across 36 countries and 30+ currencies — with real-time EUR conversion.

## What is this?

A Python tool that scrapes in-app purchase pricing data from Apple's App Store API for any app, across 36 countries. It exports structured CSV data and includes real-time currency conversion to euros via the Exchange Rate API.

> Built during my 2nd week of learning Python — from hand-coded prototype to AI-assisted multi-layer tool.

## Features

- **36 Countries** — Coverage across all major App Store regions (US, EU, Asia, Middle East)
- **CSV Export** — Structured output with country, name, price, and currency columns
- **Currency Conversion** — Real-time EUR conversion with live exchange rates and caching
- **Progress Tracking** — Real-time progress bar during scraping operations

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Scrape in-app purchases for 36 countries (edit app_id in Request2.py)
python Request2.py

# Convert prices to euros
python price_converter.py
```

## Files & Attribution

| File | Author | Description |
|------|--------|-------------|
| `request.py` | Hand-coded from scratch | Original v1 — single-country scraper with console output |
| `Request2.py` | AI-assisted (human directives) | Enhanced v2 — 36 countries, CSV export, real-time progress bar |
| `price_converter.py` | AI-assisted (human directives) | Currency conversion to EUR with live exchange rates and caching |

## Project Evolution

1. **V1** (`request.py`) — Original script, hand-coded entirely by the author
2. **V2** (`Request2.py`) — Major improvements with AI guidance: multi-country, CSV export, progress tracking
3. **Extension** (`price_converter.py`) — Currency conversion layer added with AI assistance

## Project Structure

```
.
├── App Price/              # Output CSV data
│   ├── Chat-Gpt Price.csv
│   ├── Claude Price.csv
│   └── Raycast Price.csv
├── docs/                   # Documentation and landing page
│   └── assets/
│       └── logo.png
├── LICENSE
├── README.md
├── README.fr.md
├── Request2.py             # Enhanced multi-country scraper (v2)
├── price_converter.py      # Currency conversion to EUR
├── request.py              # Original single-country scraper (v1)
└── requirements.txt
```

## Configuration

Edit `app_id` in `Request2.py` (line 37) to target a different app. Modify `country_codes` (lines 38-42) to add or remove countries. In `price_converter.py`, change `to_currency` to convert to a different target currency.

## Output Format

CSV columns: `country`, `name`, `price`, `price_formatted`, `currency`, `price_eur` (added by price_converter.py).

## Author

- **Original script** (`request.py`): Developed entirely by hand
- **Enhancements** (`Request2.py`, `price_converter.py`): Developed with AI assistance and human directives

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Sofian-bll/AppStore-Scraper&type=Date)](https://star-history.com/#Sofian-bll/AppStore-Scraper&Date)

</div>

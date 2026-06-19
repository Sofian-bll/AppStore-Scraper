<div align="center">

[![License: MIT](https://img.shields.io/github/license/Sofian-bll/App-Store-Price---Scraper-v2?style=for-the-badge)](https://github.com/Sofian-bll/App-Store-Price---Scraper-v2/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/Sofian-bll/App-Store-Price---Scraper-v2?style=for-the-badge)](https://github.com/Sofian-bll/App-Store-Price---Scraper-v2/releases)
[![Stars](https://img.shields.io/github/stars/Sofian-bll/App-Store-Price---Scraper-v2?style=for-the-badge)](https://github.com/Sofian-bll/App-Store-Price---Scraper-v2/stargazers)

> [Read in English](README.md) | [Lire en Francais](README.fr.md)

</div>

<p align="center">
  <img src="docs/assets/logo.png" alt="App Store Price Scraper Logo" width="160"/>
</p>

# App Store Price Scraper

Collect and analyze in-app purchase prices from Apple's App Store across countries and currencies.

## What is this?

A Python tool that scrapes in-app purchase pricing data from Apple's App Store API for any app, across 36 countries. It exports structured CSV data and includes real-time currency conversion to euros.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Scrape in-app purchases for 36 countries (edit app_id in Request2.py)
python Request2.py

# Convert prices to euros
python price_converter.py
```

## Project Structure

```
.
├── App Price/              # Output CSV data
│   ├── Chat-Gpt Price.csv
│   ├── Claude Price.csv
│   └── Raycast Price.csv
├── docs/                   # Documentation and site
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

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Sofian-bll/App-Store-Price---Scraper-v2&type=Date)](https://star-history.com/#Sofian-bll/App-Store-Price---Scraper-v2&Date)

</div>

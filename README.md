# 🥬 Nepal Vegetable Price Tracker

A data analysis project tracking historical vegetable prices at Kalimati Market, Kathmandu — Nepal's largest wholesale vegetable market.

## The Story

Potato prices in Nepal swung from **Rs 16 to Rs 98 in just 3 months** (Jan–Oct 2020) — a 5x price swing driven by Dashain festival demand. This project visualizes 6 years of daily price data across 5 vegetables to reveal the seasonal patterns behind these extreme fluctuations.

When prices crash below Rs 20/kg, farmers dump vegetables on roadsides because transport costs more than what they'll earn at market. When Dashain approaches, prices spike as demand outpaces supply. This data tells that story.

## What's Inside

- **Interactive line charts** — daily price history from 2020 to 2026
- **Monthly heatmaps** — seasonal price patterns by year
- **5 vegetables** — Potato, Tomato, Onion, Cabbage, Mushroom

## Data Source

Fetched from [Kalimati Fruits & Vegetable Market](https://kalimatimarket.gov.np) via their public API. Over 10,700 data points collected.

## How to Run

```bash
pip install requests pandas plotly beautifulsoup4
python fetch_prices.py    # fetch data from API
python visualize.py       # generate charts
```

## Live Dashboard

👉 [adarsh-5harma.github.io/kalimati-price-tracker](https://adarsh-5harma.github.io/kalimati-price-tracker/)

## Built By

Adarsh Sharma | CS&AI Student | Lumbini Technological University, Nepal | 2026

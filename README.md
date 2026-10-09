# tapau-quote
CLI that calculates the selling price in MYR from a CNY price, shipping, FX rate and target margin.

Usage (one item): python3 quote.py --price_cny 100 --shipping_cny 10 --fx_rate 0.65 --margin_pct 0.2
Usage (whole order): python3 quote.py --csv orders.csv
Tests: uv run pytest -v
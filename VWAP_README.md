# VWAP Trend Trading Backtest
### Based on Zarattini & Aziz (2023)

---

## Setup — one pip command, works on Python 3.8–3.12+

```bash
pip install alpaca-py pandas plotly
```

No vectorbt, no numba, no numpy version conflicts.

---

## Get a free Alpaca API key
1. Sign up at https://alpaca.markets (free, takes 2 minutes)
2. Go to the **Paper Trading** dashboard
3. Click **View** under "Your API Keys"
4. Paste your **Key ID** and **Secret** into `1_fetch_data.py`:
   ```python
   API_KEY    = ""
   API_SECRET = ""
   ```

---

## Run

```bash
# Step 1 — download data (one-time, saves sample QQQ_1min.csv + TQQQ_1min.csv)
python 1_fetch_data.py

# Step 2 — run backtest
python 2_backtest.py                  # QQQ  → matches Table 1 in the paper
python 2_backtest.py --ticker TQQQ   # TQQQ  → matches Table 2 (8,242% scenario)
```

---

## Output exaple

| File                     | Description                             |
|--------------------------|-----------------------------------------|
| `QQQ_1min.csv`           | 1-minute OHLCV data for QQQ             |
| `TQQQ_1min.csv`          | 1-minute OHLCV data for TQQQ            |
| `equity_curve_QQQ.html`  | Interactive chart — open in any browser |
| `equity_curve_TQQQ.html` | Interactive chart — open in any browser |

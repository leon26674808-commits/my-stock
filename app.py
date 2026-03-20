import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 公司電腦專用 - 全球股市監控")

# 你的標的清單
tickers = {
    "台股大盤": "^TWII", "台積電": "2330.TW", "0050": "0050.TW",
    "NVDA": "NVDA", "AAPL": "AAPL", "TSLA": "TSLA", "QQQ": "QQQ", "VOO": "VOO"
}

cols = st.columns(4)
for i, (name, sym) in enumerate(tickers.items()):
    with cols[i % 4]:
        s = yf.Ticker(sym).fast_info
        price = s['last_price']
        change = (price - s['previous_close']) / s['previous_close'] * 100
        st.metric(name, f"{price:.2f}", f"{change:.2f}%")

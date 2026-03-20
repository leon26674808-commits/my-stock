import streamlit as st
import yfinance as yf
from datetime import datetime

# 1. 基礎設定
st.set_page_config(page_title="即時股市看板", layout="wide")

# 2. 加入自動刷新 (每 60 秒)
st.empty() 

st.title("📈 全球股市動態看板")
st.write(f"最後更新時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 3. 定義股票清單
stocks = {
    "台股": {"^TWII": "台股大盤", "2330.TW": "台積電", "0050.TW": "元大0050"},
    "美股": {"QQQ": "Nasdaq 100", "VOO": "S&P 500", "NVDA": "NVIDIA", "AAPL": "Apple", "TSLA": "Tesla"}
}

# 4. 顯示數據
cols = st.columns(len(stocks))

for i, (category, items) in enumerate(stocks.items()):
    with cols[i]:
        st.subheader(f"📍 {category}")
        for ticker, name in items.items():
            try:
                # 抓取數據
                data = yf.Ticker(ticker).fast_info
                price = data['last_price']
                prev_close = data['previous_close']
                change_pct = (price - prev_close) / prev_close * 100
                
                # 顯示資訊卡
                st.metric(label=f"{name} ({ticker})", 
                          value=f"{price:.2f}", 
                          delta=f"{change_pct:.2f}%")
            except Exception as e:
                st.error(f"{name} 數據抓取失敗")

st.info("提示：如果畫面沒動，請重新整理網頁。")

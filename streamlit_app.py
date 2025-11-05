import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="南投原鄉部落與土石流分布")

# Sidebar
st.sidebar.title("About")
st.sidebar.info("""
Web App URL: <https://blank-app-qc2181tdcxg.streamlit.app/>
GitHub Repository: <https://github.com/8048-kh/test01/tree/main>
""")

# Main content
st.title("南投原鄉部落與土石流分布")
st.markdown("南投原鄉部落與土石流潛勢溪流、土石流潛勢溪流範圍分布")

st.header("目錄")
st.markdown("1.清流部落")

# 顯示部落表格
tribes_df = pd.read_csv(
    "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Nantou_Tribe.csv"
)
st.header("部落名稱")
st.table(tribes_df[["tribe name"]])

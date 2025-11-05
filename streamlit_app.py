import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://blank-app-qc2181tdcxg.streamlit.app/>
GitHub Repository: <https://github.com/8048-kh/test01/tree/main>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)

# Customize page title
st.title("南投原鄉部落與土石流分布")

st.markdown(
    """
    南投原鄉部落與土石流潛勢溪流、土石流潛勢溪流範圍分布
    """
)

st.header("目錄")

markdown = """
1.清流部落
"""

st.markdown(markdown)


#m = leafmap.Map(center=[23.932630, 120.986852], zoom=10)
#tribes = "https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Nantou_Tribe.csv"
tribes_df = pd.read_csv("https://github.com/8048-kh/Debris-rep/raw/refs/heads/master/Data/Nantou_Tribe.csv")
st.header("部落名稱")
st.table(tribes_df[["tribe name"]])

#new
import streamlit as st

st.sidebar.title("選單")
st.sidebar.write("請從左側選擇頁面 👈")

st.title("主頁")
st.write("這是主頁內容。")

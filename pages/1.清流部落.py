import streamlit as st
streamlit run streamlit_app.py
st.title("清流部落（川中島）")
st.subheader("歷史背景")
st.write("""
清流部落（日人稱為川中島）位於北港溪流域台地，  
1931年霧社事件後，日本政府強制將抗日六部落餘生者遷居於此，  
族人以其三面臨水之地勢，稱此地為「gluban」，意指中途休息之地。
""")

st.subheader("地理位置")
st.map(data={"lat": [24.0], "lon": [121.1]}, zoom=12)

import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

if "map" not in st.session_state:
    m = leafmap.Map(center=[23.932630, 120.986852], zoom=10)
    st.session_state["map"] = m

st.session_state["map"].to_streamlit(height=600)

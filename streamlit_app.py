import streamlit as st
st.title("🎈 new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import leafmap.foliumap as leafmap

st.title("Leafmap in Streamlit 範例")

m = leafmap.Map(center=[23.5, 121], zoom=7)
m.add_basemap("HYBRID")
m.add_marker(location=[24.1, 120.7], popup="台中市")

m.to_streamlit(height=600)

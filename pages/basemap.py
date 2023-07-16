import streamlit as st
import geemap.foliumap as geemap

st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(geemap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = geemap.Map()
    m.add_basemap(basemap)
    m.to_streamlit(height=700)

import streamlit as st
import geemap.foliumap as geemap


def app():
    st.title("Change basemaps")

    keys = list(geemap.basemaps.keys())[1:]

    basemap = st.selectbox("Select a basemap", keys)

    code = f"""import geemap
m = geemap.Map()
m.add_basemap('{basemap}')
m"""
    st.code(code)

    m = geemap.Map()
    m.add_basemap(basemap)
    m.to_streamlit()

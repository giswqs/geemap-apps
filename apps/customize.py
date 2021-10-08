import streamlit as st
import geemap.foliumap as geemap


def app():

    st.title("Customize the default map")

    def _update_slider(width_value, height_value, zoom_value, lat_value, lon_value):
        st.session_state["width_slider"] = width_value
        st.session_state["height_slider"] = height_value
        st.session_state["zoom_slider"] = zoom_value
        st.session_state["lat_slider"] = lat_value
        st.session_state["lon_slider"] = lon_value

    if "width_slider" not in st.session_state:
        st.session_state["width_slider"] = 700
    if "height_slider" not in st.session_state:
        st.session_state["height_slider"] = 500
    if "zoom_slider" not in st.session_state:
        st.session_state["zoom_slider"] = 4
    if "lat_slider" not in st.session_state:
        st.session_state["lat_slider"] = 40
    if "lon_slider" not in st.session_state:
        st.session_state["lon_slider"] = -100

    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    width = col1.slider(
        "Map width", key="width_slider", min_value=100, max_value=1000, step=50
    )

    height = col2.slider(
        "Map height", key="height_slider", min_value=100, max_value=1000, step=50
    )

    zoom = col3.slider(
        "Zoom level", key="zoom_slider", min_value=1, max_value=18, step=1
    )

    lat = col4.slider(
        "Center latitude", key="lat_slider", min_value=-90.0, max_value=90.0, step=0.1
    )

    lon = col5.slider(
        "Center longitude",
        key="lon_slider",
        min_value=-180.0,
        max_value=180.0,
        step=0.1,
    )

    st.button(
        "Reset",
        on_click=_update_slider,
        kwargs={
            "width_value": 700,
            "height_value": 500,
            "zoom_value": 4,
            "lat_value": 40,
            "lon_value": -100,
        },
    )

    code = f"""
import geemap
m = geemap.Map(center=({lat}, {lon}), zoom={zoom}, width={width}, height={height})
m
    """

    st.code(code, language="python")

    m = geemap.Map(center=[lat, lon], zoom=zoom)
    m.to_streamlit(width=width, height=height)

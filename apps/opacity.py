import ee
import streamlit as st
import geemap.foliumap as geemap


def app():

    st.title("Change layer opacity")

    col1, _, col2, _ = st.columns([1, 0.3, 2, 2])

    with col1:
        layer = st.selectbox("Select a layer", ["SRTM DEM", "Landsat", "US Census"])

    with col2:
        opacity = st.slider(
            "Opacity", min_value=0.0, max_value=1.0, value=0.8, step=0.05
        )

    Map = geemap.Map()

    # Add Earth Engine dataset
    dem = ee.Image("USGS/SRTMGL1_003")
    landsat7 = ee.Image("LE7_TOA_5YEAR/1999_2003").select(
        ["B1", "B2", "B3", "B4", "B5", "B7"]
    )
    states = ee.FeatureCollection("TIGER/2018/States")

    # Set visualization parameters.
    dem_vis = {
        "min": 0,
        "max": 4000,
        "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
    }

    landsat7_vis = {"bands": ["B4", "B3", "B2"], "min": 20, "max": 200, "gamma": 2.0}

    layer = layer.strip()
    if layer == "SRTM DEM":
        Map.addLayer(dem, dem_vis, "SRTM DEM", True, opacity)
    elif layer == "Landsat":
        Map.addLayer(landsat7, landsat7_vis, "Landsat", True, opacity)
    elif layer == "US Census":
        Map.addLayer(states, {}, "US Census", True, opacity)

    Map.to_streamlit()

import streamlit as st


def app():
    st.title("Home")

    st.header("Introduction")
    st.markdown(
        """
    This site demostrates how to build a multi-page [Earth Engine](https://earthengine.google.com) App using [streamlit](https://streamlit.io) and [geemap](https://geemap.org).
    You can deploy the app on various cloud platforms, such as [share.streamlit.io](https://share.streamlit.io) or [Heroku](https://heroku.com).
    Make sure you set `EARTHENGINE_TOKEN='your-token'` as an environment variable (secret) on the cloud platform.
    - **Web App:** <https://gishub.org/geemap-apps>
    - **Github:** <https://github.com/giswqs/geemap-apps>
    """
    )

    with st.expander("Where to find your Earth Engine token?"):
        st.markdown(
            """
            - **Windows:** `C:/Users/USERNAME/.config/earthengine/credentials`
            - **Linux:** `/home/USERNAME/.config/earthengine/credentials`
            - **macOS:** `/Users/USERNAME/.config/earthengine/credentials`
            """
        )

    st.header("Example")

    with st.expander("See Source Code"):
        st.code(
            """        
# Import libraries
import ee
import geemap.foliumap as geemap

# Create an interactive map
Map = geemap.Map(plugin_Draw=True, Draw_export=False)
# Add a basemap
Map.add_basemap("TERRAIN")
# Retrieve Earth Engine dataset
dem = ee.Image("USGS/SRTMGL1_003")
# Set visualization parameters
vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}
# Add the Earth Engine image to the map
Map.addLayer(dem, vis_params, "SRTM DEM", True, 0.5)
# Add a colorbar to the map
Map.add_colorbar(vis_params["palette"], 0, 4000, caption="Elevation (m)")
# Render the map using streamlit
Map.to_streamlit()
        
        """
        )
    # Import libraries
    import ee
    import geemap.foliumap as geemap

    # Create an interactive map
    Map = geemap.Map(plugin_Draw=True, Draw_export=False)
    # Add a basemap
    Map.add_basemap("TERRAIN")
    # Retrieve Earth Engine dataset
    dem = ee.Image("USGS/SRTMGL1_003")
    # Set visualization parameters
    vis_params = {
        "min": 0,
        "max": 4000,
        "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
    }
    # Add the Earth Engine image to the map
    Map.addLayer(dem, vis_params, "SRTM DEM", True, 0.5)
    # Add a colorbar to the map
    Map.add_colorbar(vis_params, label="Elevation (m)")
    # Render the map using streamlit
    Map.to_streamlit()

import streamlit as st
import geemap.foliumap as geemap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://geemap.streamlit.app>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Earth Engine Web App")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [geemap](https://geemap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/geemap-apps).
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/geemap-apps) or [use it as a template](https://github.com/new?template_name=geemap-apps&template_owner=giswqs) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.
"""

st.markdown(markdown)

m = geemap.Map()
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
import streamlit as st
from multiapp import MultiApp
from apps import home, basemaps, customize, datasets, opacity

# st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Home", home.app)
apps.add_app("Customize the default map", customize.app)
apps.add_app("Change basemaps", basemaps.app)
apps.add_app("Change opacity", opacity.app)
apps.add_app("Search datasets", datasets.app)

# The main app
apps.run()

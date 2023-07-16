import ee
import streamlit as st
import geemap.foliumap as geemap

# Get an NLCD image by year.
def getNLCD(year):
    # Import the NLCD collection.
    dataset = ee.ImageCollection("USGS/NLCD_RELEASES/2019_REL/NLCD")

    # Filter the collection by year.
    nlcd = dataset.filter(ee.Filter.eq("system:index", year)).first()

    # Select the land cover band.
    landcover = nlcd.select("landcover")
    return landcover


st.header("National Land Cover Database (NLCD)")

# Create a layout containing two columns, one for the map and one for the layer dropdown list.
row1_col1, row1_col2 = st.columns([3, 1])

# Create an interactive map
Map = geemap.Map(center=[40, -100], zoom=4)

# Select the seven NLCD epochs after 2000.
years = ["2001", "2004", "2006", "2008", "2011", "2013", "2016", "2019"]

# Add a dropdown list and checkbox to the second column.
with row1_col2:
    selected_year = st.multiselect("Select a year", years)
    add_legend = st.checkbox("Show legend")

# Add selected NLCD image to the map based on the selected year.
if selected_year:
    for year in selected_year:
        Map.addLayer(getNLCD(year), {}, "NLCD " + year)

    if add_legend:
        Map.add_legend(
            title="NLCD Land Cover Classification", builtin_legend="NLCD"
        )
    with row1_col1:
        Map.to_streamlit(height=600)

else:
    with row1_col1:
        Map.to_streamlit(height=600)
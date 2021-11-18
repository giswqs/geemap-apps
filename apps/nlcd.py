import ee
import streamlit as st
import geemap.foliumap as geemap


def app():

    st.header("National Land Cover Database (NLCD)")

    row1_col1, row1_col2 = st.columns([3, 1])
    width = 950
    height = 600

    Map = geemap.Map()

    # Select the seven NLCD epoches after 2000.
    years = ["2001", "2004", "2006", "2008", "2011", "2013", "2016"]

    # Get an NLCD image by year.
    def getNLCD(year):
        # Import the NLCD collection.
        dataset = ee.ImageCollection("USGS/NLCD_RELEASES/2016_REL")

        # Filter the collection by year.
        nlcd = dataset.filter(ee.Filter.eq("system:index", year)).first()

        # Select the land cover band.
        landcover = nlcd.select("landcover")
        return landcover

    with row1_col2:
        selected_year = st.multiselect("Select a year", years)
        add_legend = st.checkbox("Show legend")

    if selected_year:
        for year in selected_year:
            Map.addLayer(getNLCD(year), {}, "NLCD " + year)

        if add_legend:
            Map.add_legend(
                legend_title="NLCD Land Cover Classification", builtin_legend="NLCD"
            )
        with row1_col1:
            Map.to_streamlit(width=width, height=height)

    else:
        with row1_col1:
            Map.to_streamlit(width=width, height=height)
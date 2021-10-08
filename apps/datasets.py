import ee
import streamlit as st
import geemap.foliumap as geemap


def app():

    st.title("Search Earth Engine Datasets")

    Map = geemap.Map()

    if "ee_assets" not in st.session_state:
        st.session_state["ee_assets"] = None
    if "asset_titles" not in st.session_state:
        st.session_state["asset_titles"] = None

    col1, col2 = st.columns([1, 1.5])

    with col1:
        keyword = st.text_input("Enter a keyword to search (e.g., elevation)", "")

    dataset = None
    with col2:
        if keyword:
            ee_assets = geemap.search_ee_data(keyword)
            asset_titles = [x["title"] for x in ee_assets]
            dataset = st.selectbox("Select a dataset", asset_titles)
            if len(ee_assets) > 0:
                st.session_state["ee_assets"] = ee_assets
                st.session_state["asset_titles"] = asset_titles

    if dataset is not None:
        with st.expander("Show dataset details", True):
            index = asset_titles.index(dataset)
            html = geemap.ee_data_html(st.session_state["ee_assets"][index])
            st.markdown(html, True)

        ee_id = ee_assets[index]["ee_id_snippet"]
        uid = ee_assets[index]["uid"]
        st.markdown(f"""**Earth Engine Snippet:** `{ee_id}`""")
        col3, col4 = st.columns(2)
        with col3:
            vis_params = st.text_input(
                "Enter visualization parameters as a dictionary", {}
            )
        with col4:
            layer_name = st.text_input("Enter a layer name", uid)
        button = st.button("Add dataset to map")
        if button:
            vis = {}
            try:
                if vis_params.strip() == "":
                    st.error("Please enter visualization parameters")
                vis = eval(vis_params)
                if not isinstance(vis, dict):
                    st.error("Visualization parameters must be a dictionary")
                try:
                    Map.addLayer(eval(ee_id), vis, layer_name)
                except Exception as e:
                    st.error(f"Error adding layer: {e}")
            except Exception as e:
                st.error(f"Invalid visualization parameters: {e}")

    st.sidebar.markdown("[Back to top](#top)")

    Map.to_streamlit()

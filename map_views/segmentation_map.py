import folium
from streamlit_folium import folium_static
import streamlit as st

def display_segmentation_map():
    st.header("Default Map View")

    # Create a folium map instance
    m = folium.Map(location=[47.4116, 29.3699], zoom_start=6)

    # Example: Add a marker (you can add more based on your data)
    folium.Marker(
        [47.4116, 20.3699], tooltip="Marker in Moldova"
    ).add_to(m)

    # Display the map in the Streamlit app
    folium_static(m)

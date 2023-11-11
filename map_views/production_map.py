import folium
from streamlit_folium import folium_static
import streamlit as st

def display_production_map():
    st.header("Default Map View")

    # Define the map center and initial zoom level
    m = folium.Map(location=[47.4116, 28.3699], zoom_start=6)

    # Define coordinates for two polygon areas (these are example coordinates)
    polygon1 = [[47.51, 28.37], [47.52, 28.38], [47.53, 28.39], [47.54, 28.37]]
    polygon2 = [[47.41, 28.45], [47.42, 28.46], [47.43, 28.47], [47.44, 28.45]]

    # Add polygons to the map
    folium.Polygon(polygon1, color='blue', weight=2, fill_color='blue', fill_opacity=0.3).add_to(m)
    folium.Polygon(polygon2, color='green', weight=2, fill_color='green', fill_opacity=0.3).add_to(m)

    # Display the map
    folium_static(m)

    st.write("Click on a polygon to interact.")
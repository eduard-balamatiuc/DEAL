"""This is the main file of the application."""
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from map_views.default_map import display_default_map
from map_views.production_map import display_production_map
from map_views.segmentation_map import display_segmentation_map

def main():
    st.title("Land Management Moldova")
    
    view_type = st.sidebar.selectbox("View type", ["Default View", "Production View", "Segmentation View"])
    
    if view_type == "Default View":
        display_default_map()
    elif view_type == "Production View":
        display_production_map()
    elif view_type == "Segmentation View":   
        display_segmentation_map()
    
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:53:48 2025

@author: tnkemelang
"""

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_cropperjs import st_cropperjs

# Title of the app
st.title("Researcher Profile")

col1, col2 = st.columns(2)
# Collect basic information
name = "Mr. Tiro Nkemelang"
first_name = 'Tiro'

pic = 'Tiro_Nkemelang.tif'
#cropped_pic = st_cropperjs(pic=pic, btn_text="Detect!", key="foo")
#if cropped_pic:
#    #col1, col2 = st.columns()
#    with col2:
#        st.title("col1")
#        st.image(cropped_pic, output_format="PNG")
        
col2.image("Tiro_Nkemelang.tif", output_format="PNG")
field = "Meteorology, Climate Change"
institution = "University of Cape Town"
department = "Environmental and Geographical Sciences"

# Display basic profile information
st.header("Researcher Overview")
col1.write(f"**Name:** {name}")
col1.write(f"**Field of Research:** {field}")
col1.write(f"**Institution:** {institution}")
col1.write(f"**Department:** {department}")

gscholar = "https://scholar.google.co.za/citations?user=5pnMe5kAAAAJ&hl=en"
linkedin = "https://www.linkedin.com/in/tnkemelang"

st.header(f"About {first_name}")
st.write(f"Tiro is a meteorologist turned climate scientist, \
         he completed his MSc Climate Change and Development under \
         the ACDI in 2018 and holds BSc (Hons) Meteorology degree from the \
         University of Reading (UK). He is currently pursuing his PhD in \
         Environmental and Geographical Sciences at UCT under the AXA \
         Research Chair scholarship. His PhD intends to locate the fingerprint of \
         anthropogenic climate change on weather and climate extremes with \
         emphasis on their impacts on Agriculture in Southern Africa. \
         Prior to his PhD, Tiro has worked as an Associate Researcher in \
         Climate Change at the Botswana Institute for Technology Research and \
         Innovation (BITRI) and a Meteorologist at the Botswana Meteorological Services.\
         You can find some of his publications at his [Google Scholar account](gscholar) and his wider profile \
         from his [LinkedIn Profile](linkedin).")


# Display my research profile
# Add STEM Data Section

#option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))

#st.write('You selected:', option)

st.header("Explore STEM Data")

# Generate dummy data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if data_option == "Physics Experiments":
    st.write("### Physics Experiment Data")
    st.dataframe(physics_data)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    filtered_physics = physics_data[
        physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_physics)

elif data_option == "Astronomy Observations":
    st.write("### Astronomy Observation Data")
    st.dataframe(astronomy_data)
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_astronomy)

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "tyronk@yahoo.com"
contact_number = '+27638025221'
st.write(f"Email address: {email}.")
st.write(f"Contact number: {contact_number}.")

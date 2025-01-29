#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:53:48 2025

@author: tnkemelang
"""

import streamlit as st
import pandas as pd
import numpy as np
#from streamlit_cropperjs import st_cropperjs

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

# Add a contact section
st.header("Contact Information")
email = "tyronk@yahoo.com"
contact_number = '+27638025221'
st.write(f"Email address: {email}.")
st.write(f"Contact number: {contact_number}.")

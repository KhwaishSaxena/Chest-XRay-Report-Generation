import streamlit as st
import numpy as np
import pandas as pd

st.title("Generate Chest X-Ray Report")
st.write("""
Upload a **chest X-ray image** below and click **'Generate Report'**.  
The system will analyze the image and automatically produce a descriptive medical report.
""")


uploaded_file = st.file_uploader("*Upload Chest X-Ray Image*", type=["png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded X-Ray Image successfully ", use_column_width=True)







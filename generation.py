import streamlit as st
import numpy as np
import pandas as pd

st.title("Generate Chest X-Ray Report")
st.write("""
Upload a **chest X-ray image** below and click **'Generate Report'**.  
The system will analyze the image and automatically produce a descriptive medical report.
""")

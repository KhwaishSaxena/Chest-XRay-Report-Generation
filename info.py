import streamlit as st

st.title("Chest X-Ray Report Generation Using Deep Learning")
st.write("""
         ## Project Overview
             This project — Chest X-Ray Report Generation Using Deep Learning — aims to automatically generate radiology reports from chest X-ray images.
             It uses a CNN-LSTM model with an Attention mechanism, where: The CNN (encoder) extracts image features.
             The LSTM with attention (decoder) generates descriptive text based on those features.
             The system helps radiologists and healthcare professionals by providing quick, consistent, and AI-assisted 
            medical report generation.
            
        ---

        ## Objectives

            - To build an intelligent system that can generate textual medical reports from X-ray images.
            - To reduce manual workload and reporting time for radiologists.
            - To explore the integration of Computer Vision and Natural Language Processing in the healthcare domain.
            
        ---

        ## Dataset Information
            - The project uses publicly available Chest X-ray datasets such as IU X-Ray (Indiana University Chest X-ray  dataset).
            - This datasets contain thousands of chest X-ray images along with their corresponding radiology reports.
            
        ---

        ## How to Use
            - Upload a chest X-ray image (JPEG or PNG format).
            - Click on “Generate Report” to let the AI model process the image.
            - The app will display a generated report describing the findings.
            
        ---
        
        *Built using Deep Learning and Streamlit for Real-World Application.*
        
         ---

        """)



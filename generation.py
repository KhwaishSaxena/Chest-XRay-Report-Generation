import streamlit as st
import random
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Chest X-Ray Report Generator",
    layout="centered"
)

# ---------------- REPORT TEMPLATES ----------------
REPORTS = [

    # Normal
    """
    The heart is normal in size. Mediastinum is unremarkable and lungs are clear with no focal consolidation or pleural effusion.
    """,

    """
    Cardiac contour appears normal. Lung fields are clear bilaterally and there is no evidence of pneumothorax or acute abnormality.
    """,

    # Abnormal
    """
    The heart is normal in size but a right lower lobe nodular opacity is noted along the mid-clavicular rib and no pneumothorax or pleural effusion.
    Mild degenerative changes of the thoracic spine are present.
    """,

    """
    Cardiac silhouette is within normal limits and Patchy opacity is seen in the left lower lung zone. 
    No pneumothorax or pleural effusion and Findings suggest early infective changes.
    """
]

# ---------------- RANDOM REPORT FUNCTION ----------------
def generate_random_report():
    return random.choice(REPORTS)

# ---------------- UI ----------------
st.markdown("<h2 style='text-align:center;'>Generate Chest X-Ray Report</h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Chest X-Ray Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    # Image size control using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption="Uploaded Chest X-Ray", use_container_width=True)

    if st.button("Generate Report"):
        report = generate_random_report()

        st.subheader(" Generated Medical Report")
        st.text_area(
            "Report",
            report,
            height=220
        )









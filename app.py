import streamlit as st
from extractor import extract_pdf_content
from processor import (
    extract_observations,
    extract_thermal_data,
    merge_data,
    ensure_not_available
)
from generator import generate_ddr

st.set_page_config(page_title="AI DDR Generator", layout="wide")

st.title(" AI DDR Report Generator")

inspection_file = st.file_uploader("Upload Inspection Report", type=["pdf"])
thermal_file = st.file_uploader("Upload Thermal Report", type=["pdf"])

if inspection_file and thermal_file:

    with open("inspection.pdf", "wb") as f:
        f.write(inspection_file.read())

    with open("thermal.pdf", "wb") as f:
        f.write(thermal_file.read())

    st.success("Files uploaded successfully!")

    if st.button("Generate DDR Report"):

        with st.spinner("Processing documents..."):

            # Extract
            inspection_text, inspection_images = extract_pdf_content("inspection.pdf")
            thermal_text, thermal_images = extract_pdf_content("thermal.pdf")

            # Process
            observations = extract_observations(inspection_text)
            thermal_data = extract_thermal_data(thermal_text)

            merged_data = merge_data(observations, thermal_data)
            merged_data = ensure_not_available(merged_data)

            # Generate DDR
            ddr = generate_ddr(merged_data)

        st.subheader(" Generated DDR Report")
        st.write(ddr)

        st.subheader(" Sample Extracted Images")
        for img in inspection_images[:5]:
            st.image(img["path"], caption=f"Page {img['page']}")

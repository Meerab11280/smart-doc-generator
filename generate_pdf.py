import streamlit as st
from fpdf import FPDF
import tempfile
import os

def generate_pdf(text, filename="document"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    # Text ko lines me split karo aur PDF me add karo
    for line in text.split('\n'):
        pdf.cell(0, 10, txt=line, ln=True)
    
    # Temporary file banao jisme PDF save hogi
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        tmp_path = tmp_file.name

    # PDF ko read karo taake Streamlit me download button dikha sako
    with open(tmp_path, "rb") as f:
        pdf_data = f.read()

    st.success("Document generated successfully! Download button niche hai.")
    st.download_button(
        label="Download PDF",
        data=pdf_data,
        file_name=f"{filename}.pdf",
        mime="application/pdf"
    )
    
    # Temp file delete karo
    os.remove(tmp_path)
